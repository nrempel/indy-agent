"""
A credential request content message.
"""

from marshmallow import Schema, fields, post_load

from ..agent_message import AgentMessage
from ..message_types import MessageTypes


class CredentialRequest(AgentMessage):
    def __init__(
        self, offer_json: str, credential_request_json: str, credential_values_json: str
    ):
        self.offer_json = offer_json
        self.credential_request_json = credential_request_json
        self.credential_values_json = credential_values_json

    def _type(self):
        return MessageTypes.CREDENTIAL_REQUEST.value


class CredentialRequestSchema(Schema):
    # Avoid clobbering builtin property
    _type = fields.Str(data_key="@type")
    offer_json = fields.Str()
    credential_request_json = fields.Str()
    credential_values_json = fields.Str()

    @post_load
    def make_model(self, data: dict) -> CredentialRequest:
        return CredentialRequest(**data)
