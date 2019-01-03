"""
A credential content message.
"""

from marshmallow import Schema, fields

from ..agent_message import AgentMessage
from ..message_types import MessageType


class Credential(AgentMessage):
    def __init__(self, credential_json: str, revocation_registry_id: str):
        self.credential_json = credential_json
        self.revocation_registry_id = revocation_registry_id

    def type(self):
        return MessageType.CREDENTIAL


class CredentialSchema(Schema):
    # Avoid clobbering builtin property
    _type = fields.Str(data_key="@type")
    credential_json = fields.Str()
    revocation_registry_id = fields.Str()
