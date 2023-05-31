import asyncio
import websockets
import ssl
import os
import dotenv
import sys

PARENT_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.dirname(PARENT_DIR)

# # Add the parent folder's path to sys.path
# sys.path.append(ROOT_DIR)

from utils.logger import Logger
logger = Logger(__name__)

dotenv.load_dotenv(os.path.join(ROOT_DIR, 'configs/.env'))

WSS_HOST = os.getenv('WSS_HOST')
WSS_PORT = os.getenv('WSS_PORT')

async def handle_websocket(websocket, path):
    # Perform any necessary setup or validation for the incoming connection

    try:
        # Handle incoming messages from the WebSocket client
        async for message in websocket:
            # Process the received message or perform any required actions
            # You can also send a response back to the client if needed
            await websocket.send("Received: " + message)
    except websockets.exceptions.ConnectionClosedOK:
        # Connection is closed by the client
        pass
    finally:
        # Clean up or perform any necessary tasks when the connection is closed
        pass


class WssServer:
    def init_ssl_context(self):
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        ssl_context.load_cert_chain(os.path.join(ROOT_DIR, 'certs/cert.pem'), os.path.join(ROOT_DIR, 'certs/key.pem'))
        return ssl_context

    def run(self):
        ssl_context = self.init_ssl_context()

        asyncio.set_event_loop(asyncio.new_event_loop())

        start_server = websockets.serve(handle_websocket, WSS_HOST, WSS_PORT, ssl=ssl_context)
        logger.info(f"Websocket server started at wss://{WSS_HOST}:{WSS_PORT}")
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

app = WssServer()