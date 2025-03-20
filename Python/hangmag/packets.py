from dataclasses import dataclass
from enum import Enum

class PacketID(Enum):
    HELLO = 0
    PHRASE = 1
    GUESS = 2
    

@dataclass
class Packet:
    id: PacketID
    payload: str

