from utils.logger import Logger
from dotenv import load_dotenv
import os
import threading

from api.api_server import app as api_server, SSL_CONTEXT
from websocket.wss_server import app as wss_server


logger = Logger(__name__)

load_dotenv(os.path.join(os.path.dirname(__file__), 'configs/.env'))

WSS_HOST = os.getenv('WSS_HOST')
WSS_PORT = os.getenv('WSS_PORT')

API_HOST = os.getenv('API_HOST')
API_PORT = os.getenv('API_PORT')

def start_api_server():
    api_server.run(host=API_HOST, port=API_PORT, ssl_context=SSL_CONTEXT)

def start_wss_server():
    wss_server.run(WSS_HOST, WSS_PORT)

def main():
    logger.info("Starting API server...")
    api_thread = threading.Thread(target=start_api_server)
    api_thread.start()

    logger.info("Starting Websocket server...")
    wss_thread = threading.Thread(target=start_wss_server)
    wss_thread.start()

    api_thread.join()
    wss_thread.join()

    
if __name__ == '__main__':
    main()