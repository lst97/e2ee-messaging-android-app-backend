from utils.logger import Logger
from dotenv import load_dotenv
import os
import threading

from api.api_server import app as api_server
from websocket.wss_server import app as wss_server


logger = Logger(__name__)

load_dotenv(os.path.join(os.path.dirname(__file__), 'configs/.env'))

def main():
    logger.info("Starting API server...")
    api_thread = threading.Thread(target=api_server.run)
    api_thread.start()

    logger.info("Starting Websocket server...")
    wss_thread = threading.Thread(target=wss_server.run)
    wss_thread.start()

    api_thread.join()
    wss_thread.join()

    
if __name__ == '__main__':
    main()