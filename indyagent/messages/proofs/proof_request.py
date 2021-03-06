"""
A proof request content message.
"""

from marshmallow import Schema, fields, post_load

from ..agent_message import AgentMessage
from ..message_types import MessageTypes


class ProofRequest(AgentMessage):
    def __init__(self, proof_request_json: str):
        self.proof_request_json = proof_request_json

    def _type(self):
        return MessageTypes.PROOF_REQUEST.value


class ProofRequestSchema(Schema):
    # Avoid clobbering builtin property
    _type = fields.Str(data_key="@type")
    proof_request_json = fields.Str()

    @post_load
    def make_model(self, data: dict) -> ProofRequest:
        return ProofRequest(**data)
