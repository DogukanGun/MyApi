import ollama
from fastapi import APIRouter

router = APIRouter(tags=["Admin"], prefix="/admin")


@router.post("/email")
async def respond_email(email: str):
    response = ollama.chat(model='llama3', messages=[
        {
            'role': 'user',
            'content': 'Hi now I will send you an email please'
                       'write me an answer. '
                       'I will directy copy the email that you wrote and send to the person.'
                       'Before this email write --- and at the end ----' +
                       '\n' + email,
        },
    ])
    return response['message']['content']
