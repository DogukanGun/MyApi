from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import llm

app = FastAPI(
    title="API Project",
    description="Work in progress",
    version='0.1',
    swagger_ui_parameters={"docExpansion": "none"},
)

routers = [
    llm.router,
]

for router in routers:
    app.include_router(router)

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"],
                   allow_credentials=True)

if __name__ == "__main__":
    """
    https://github.com/tiangolo/fastapi/issues/1508
    """
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
