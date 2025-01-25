# -*- coding: utf-8 -*-
"""
Energy: Base functionality for energy-related modules.

Author: 8f00ff (Vi)
Version: 1.0.0
License: MIT
"""

from abc import ABC

from .module import Module

class Energy(Module, ABC):
  """Defines core energy handling capabilities."""
  
  def __init__(self, capacity: float, energy: float = 0) -> None:
    super().__init__()
    self._capacity: float = capacity
    self._energy: float = capacity * energy if energy <= 1 else energy
  
  @classmethod
  def register_presets(cls) -> None:
    """Prevent the abstract class from registering itself."""
    if cls is Energy:
      return
    super().register_presets()
  
  @property
  def capacity(self) -> float:
    """Returns combined capacity of all connected sources."""
    return self._capacity
  
  @property
  def energy(self) -> int:
    """Returns total energy available across all sources."""
    return self._energy
  
  def consume(self, amount: float) -> bool:
    """Attempts to consume specified amount of energy."""
    if self._energy < amount:
      return False
    self._energy = max(self._energy - amount, 0)
    return True
