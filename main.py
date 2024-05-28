from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import llm, contact

app = FastAPI(
    title="API Project",
    description="Work in progress",
    version='0.1',
    swagger_ui_parameters={"docExpansion": "none"},
)
sub_app = FastAPI()

routers = [
    llm.router,
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
app.mount("/internal", sub_app)
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
