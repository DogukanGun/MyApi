import ollama
from fastapi import APIRouter, Depends
from app.data.starknet_data import Message
from utils.environment.environment_manager import EnvironmentManager, get_environment_manager
from utils.helper.regex import find_number_in_sentence, extract_hashes
from utils.voyager.api_caller import call_api

router = APIRouter(tags=["Starknet"], prefix="/starknet")


@router.post("")
def starknet_question(
        message: Message,
        env_manager: EnvironmentManager = Depends(get_environment_manager),
):
    response = ollama.chat(model='llama3', messages=[
        {
            'role': 'system',
            'content': '''If user asks you questions about block and without providing blockhash in the question, 
         then use function id 2 always otherwise if question is about block and has block hash then use function id 1.
            If the question is about the transaction and user doesn't specified any
            transaction hash then please use function id -1, otherwise if the question contains transaction hash and about
            transaction please use function id 3. If the question about the smart contracts and user doesn't specified
            any contract address, then please use function id 4. Otherwise if the question contains smart contract 
            address and about smart contracts please use function id 5.
            If a transaction hash or block hash or smart contract address is specified then please take it too.
            Your answer must be in this form => The answer is {function_id}. {transaction-hash/block-hash/smart-contract-address}
            '''
        },
        {
            "role": "user",
            "content": message.message
        },
    ])
    content = str(response['message']['content'])
    number = find_number_in_sentence(content.split(".")[0])
    apiKey = env_manager.get_key("VOYAGER_KEY")
    res = call_api(number, content, apiKey)
    response = ollama.chat(model='llama3', messages=[
        {
            'role': 'system',
            'content': "Please answer the question only using the json provided now but dont mention a json is provided"
                       "also make the answer understandable for everyone : " + res
        },
        {
            'role': 'user',
            'content': message.message
        }
    ])
    return response['message']['content']
