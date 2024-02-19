import hashlib
import json
from dataclasses import dataclass, asdict


@dataclass()
class Block:
    index: str
    timestamp: str
    proof: int
    previous_hash: str

    def get_block_dict(self):
        return asdict(self)

    def __getitem__(self, item):
        return getattr(self, item)
