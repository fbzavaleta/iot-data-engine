from dataclasses import dataclass
from typing import Optional
"""
Author: Francis Benjamin Zavaleta, Eng
Copyright © fbzavaleta. All rights reserved.
"""

@dataclass(frozen=False)
class EngineEndpoint:
    channel: str
    token: str