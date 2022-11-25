import socket

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import secure


app = FastAPI(
    title="FastAPI Kubernetes example",
    description="Example FastAPI application running in Kubernetes",
    version="1.0.0",
)
secure_headers = secure.Secure()

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def set_secure_headers(request, call_next):
    response = await call_next(request)
    secure_headers.framework.fastapi(response)
    return response


@app.get("/", status_code=200, tags=["test"])
async def index(welcome_message: str = "Hello World!"):
    hostname = socket.gethostname()
    return {"message:": welcome_message, "served from server": hostname}
