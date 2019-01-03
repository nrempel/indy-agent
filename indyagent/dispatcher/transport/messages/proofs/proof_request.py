from ..agent_message import AgentMessage
from ..message_types import MessageType


class ProofRequest(AgentMessage):
    def type(self):
        return MessageType.PROOF_REQUEST
