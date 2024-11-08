import webview
from utils import configuration, context
from api import Api
from fastapi import FastAPI
from server import router as http_router
import threading
import uvicorn
from sql import queries
from logger import log
api = Api()
app = FastAPI()
app.include_router(http_router)

def run_server():
  log("Starting GUI server")
  uvicorn.run(app, host="127.0.0.1", port=8000)

def main():
  server_thread = threading.Thread(target=run_server, daemon=True)
  server_thread.start()
  
  context['queries'] = queries

  server_url = "http://127.0.0.1:8000/index.html"

  webview.create_window(
    f"{configuration.get_info()['name']} ({configuration.get_info()['version']})",
    url=server_url,
    js_api=api,
    width=configuration.window_width,
    height=configuration.window_height
  )
  webview.start(lambda: api.on_load())

if __name__ == "__main__":
  main()