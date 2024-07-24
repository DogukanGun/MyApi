from typing import List, Dict, Any

import ollama
from fastapi import APIRouter, Request
from ollama import Message

from app.data.llm_data import DonationMessage

router = APIRouter(tags=["LLM"], prefix="/llm")


@router.post("/email")
async def respond_email(
        email: str
):
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


@router.post("/chat/donation")
async def chat_for_donation(
        messages: List[DonationMessage]
):
    system_message: Dict[str, Any] = {
        "role": "system",
        "content": "After this message you will have a user who is trying to create a donation in blockchain. The system has the smart contracts which will be called after the conversation with you. You are trying to get information, user name, and user wallet address to deposit money after the donation and an image. Now answer all questions by talking with the user; do not write as if talking to me. Also, while getting answers, control them. If any field is dummy or the wallet address is not fitting the rules of Ethereum-type wallets, then after all information is taken from the user, tell the user 'thanks, contract will be deployed.' Then return me a message in this format: {\"name\": string, \"wallet\": string, \"reason\": string}"
    }
    messages_history: List[Message] = [
        Message(**system_message) if i == 0 else Message(**messages[i-1].__dict__) for i in
        range(len(messages) + 1)]
    response = ollama.chat(model='llama3', messages=messages_history)
    return response['message']['content']
