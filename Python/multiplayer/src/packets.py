from dataclasses import dataclass


@dataclass
class RequestPlayerUpdate:
    packet = 0

@dataclass
class PlayerUpdate:
    packet: 1
    id: int
    x: int
    y: int
