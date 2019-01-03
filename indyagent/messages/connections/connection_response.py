from ..agent_message import AgentMessage
from ..message_types import MessageType


class ConnectionResponse(AgentMessage):
    def type(self):
        return MessageType.CONNECTION_RESPONSE
