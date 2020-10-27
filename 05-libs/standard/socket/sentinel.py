import threading
import logging


logger = loggign.getLogger(__name__)


class Sentinel(threading.Thread):

    def __init__(self, port, callback):
        self.callback = callback
        self.control_socket = socket.socket(
            family=socket.AF_INET,
            type=socket.SOCK_DGRAM,
        )
        self.control_socket.bind(('0.0.0.0', PORT))
        logger.info("Sentinel UDP server up and listening on port %s", PORT)

    def run(self):
        message, client_address = server_socket.recvfrom(BUFFER_SIZE)
        self.


