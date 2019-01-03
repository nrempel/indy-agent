from ..agent_message import AgentMessage
from ..message_types import MessageType


class Credential(AgentMessage):
    def type(self):
        return MessageType.CREDENTIAL
