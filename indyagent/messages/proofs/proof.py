from ..agent_message import AgentMessage
from ..message_types import MessageType


class Proof(AgentMessage):
    def type(self):
        return MessageType.PROOF
