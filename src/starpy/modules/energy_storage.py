# -*- coding: utf-8 -*-
"""
EnergyStorage: Energy storage and battery management.

Author: 8f00ff (Vi)
Version: 1.0.0
License: MIT
"""

from typing import Dict

from .energy import Energy

class EnergyStorage(Energy):
  """Manages energy storage and retrieval."""
  
  def store(self, amount: float) -> float:
    """Stores energy and returns any excess beyond capacity."""
    leftover = max(0, self._energy + amount - self._capacity)
    self._energy = min(self._capacity, self._energy + amount)
    return leftover
  
  @classmethod
  def register_presets(cls) -> None:
    """Registers standard battery configurations."""
    cls.register("SmallBattery", lambda energy=0: cls(capacity=128, energy=energy))
    cls.register("MediumBattery", lambda energy=0: cls(capacity=256, energy=energy))
    cls.register("LargeBattery", lambda energy=0: cls(capacity=512, energy=energy))
  
  def status(self) -> Dict:
    """Returns current storage state."""
    return {
      **super().status(),
      "capacity": self.capacity,
      "energy": self.energy,
    }
