import os
import uvicorn
from src.app import build_app

app = build_app()

if __name__ == '__main__':
    uvicorn.run("main:app", port=5000, log_level="debug", reload=True)
