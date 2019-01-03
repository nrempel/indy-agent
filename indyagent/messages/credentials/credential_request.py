from ..agent_message import AgentMessage
from ..message_types import MessageType


class CredentialRequest(AgentMessage):
    def type(self):
        return MessageType.CREDENTIAL_REQUEST
