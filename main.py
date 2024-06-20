import sys

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import llm, contact, starknet
import subprocess

app = FastAPI(
    title="API Project",
    description="Work in progress",
    version='0.1',
    swagger_ui_parameters={"docExpansion": "none"},
)
sub_app = FastAPI()

routers = [
    llm.router,
    starknet.router,
]
internal_routers = [
    contact.router,
]
origins = ['http://localhost:3000']

for router in routers:
    app.include_router(router)
for router in internal_routers:
    sub_app.include_router(router)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["POST", "GET"], allow_headers=["*"],
                   allow_credentials=True)
sub_app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=["*"],
                       allow_headers=["*"],
                       allow_credentials=True)

# Define command to run FastAPI servers
main_command = [
    sys.executable, "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"
]

sub_command = [
    sys.executable, "-m", "uvicorn", "main:sub_app", "--host", "0.0.0.0", "--port", "8081"
]

if __name__ == "__main__":
    # Start FastAPI servers as separate subprocesses
    main_server = subprocess.Popen(main_command)
    sub_server = subprocess.Popen(sub_command)

    # Wait for both servers to finish
    main_server.wait()
    sub_server.wait()