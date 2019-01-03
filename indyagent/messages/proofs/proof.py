"""
A proof content message.
"""

from marshmallow import Schema, fields

from ..agent_message import AgentMessage
from ..message_types import MessageType


class Proof(AgentMessage):
    def __init__(self, proof_json: str, request_nonce: str):
        self.proof_json = proof_json
        self.request_nonce = request_nonce

    def type(self):
        return MessageType.PROOF


class ProofSchema(Schema):
    # Avoid clobbering builtin property
    _type = fields.Str(data_key="@type")
    proof_json = fields.Str()
    request_nonce = fields.Str()
