# -*- coding: utf-8 -*-
"""
EnergyGenerator: Base system for energy production.

Author: 8f00ff (Vi)
Version: 1.0.0
License: MIT
"""

from abc import ABC, abstractmethod

from .energy import Energy

class EnergyGenerator(Energy, ABC):
  """Handles energy generation and production."""
  
  @classmethod
  def register_presets(cls) -> None:
    """Prevent the abstract class from registering itself."""
    if cls is EnergyGenerator:
      return
    super().register_presets()
  
  @abstractmethod
  def generate(self) -> None:
    """Produces energy based on generator capacity."""
    self._energy = self._capacity
