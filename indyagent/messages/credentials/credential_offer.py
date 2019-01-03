from ..agent_message import AgentMessage
from ..message_types import MessageType


class CredentialOffer(AgentMessage):
    def type(self):
        return MessageType.CREDENTIAL_OFFER
