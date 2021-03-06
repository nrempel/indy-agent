"""
The conductor is responsible for coordinating messages that are received
over the network, communicating with the ledger, passing messages to handlers,
and storing data in the wallet.
"""

from ..transport.http import Http as HttpTransport
from ..transport import InvalidTransportException

from ..messages.message_converter import MessageConverter


class Conductor:
    def __init__(self, transport: str, host: str, port: int) -> None:
        self.transport = transport
        self.host = host
        self.port = port

    def start(self) -> None:
        if self.transport is "http":
            transport = HttpTransport(self.host, self.port, self.message_handler)
            transport.setup()
        else:
            raise InvalidTransportException()

    def message_handler(self, message_object: dict) -> None:
        message = MessageConverter.object_to_message(message_object)
        print(message)

