from dataclasses import dataclass
from enum import Enum
from typing import Any


class NetworkState(Enum):
    OFF = 0
    WAITING = 1
    CONNECTED = 2
    DISCONNECTED = 3


class MessageTypes(Enum):
    ERROR = 0
    MESSAGE = 1
    WARNING = 2

class PacketID(Enum):
    CLIENT_HELLO = 0
    SERVER_HELLO = 1
    CLIENT_READY = 2
    SERVER_READY = 3
    SERVER_START = 4
    PLAYER_MOVE = 5


class Payload:
    def __init__(self, data):
        self._data = data

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

@dataclass
class Packet:
    id: PacketID
    payload: Payload

