from fastapi import FastAPI
import ollama
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/email")
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


app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"],
                   allow_credentials=True)

if __name__ == "__main__":
    """
    https://github.com/tiangolo/fastapi/issues/1508
    """
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
