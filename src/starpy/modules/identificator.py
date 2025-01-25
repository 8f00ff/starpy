# -*- coding: utf-8 -*-
"""
Identificator: Manages identification and registration data storage.

Author: 8f00ff (Vi)
Version: 1.0.0
License: MIT
"""

from random import getrandbits

from .module import Module

class Identificator(Module):
  """Stores and manages identification data."""
  
  def __init__(self, name: str) -> None:
    super().__init__()
    self.name: str = name
    self._serial_number: int = getrandbits(64)
  
  @property
  def serial_number(self) -> str:
    """Returns the unique hardware identifier."""
    return self._serial_number
  
  @property
  def ship_name(self) -> str:
    """Returns the registered name."""
    return self.name
  
  @ship_name.setter
  def ship_name(self, value: str):
    """Updates the registered name."""
    self.name = value
  
  def status(self) -> dict:
    """Returns all identification data."""
    return {
      **super().status(),
      "name": self.ship_name,
      "serial_number": f"{self.serial_number:016X}",
    }
