# -*- coding: utf-8 -*-
"""
EnergyDistributor: Multi-source energy management and routing.

Author: 8f00ff (Vi)
Version: 1.0.0
License: MIT
"""

from typing import List

from .energy import Energy

class EnergyDistributor(Energy):
  """Controls energy flow between multiple sources."""
  
  def __init__(self, sources: List[Energy]) -> None:
    super().__init__(0)
    self._sources: List[Energy] = sources
  
  @property
  def capacity(self) -> int:
    """Total capacity is the sum of all sources' capacities."""
    return sum(source.capacity for source, _ in self._sources)

  @property
  def energy(self) -> int:
    """Total energy is the sum of all sources' energy."""
    return sum(source.energy for source, _ in self._sources)
  
  def consume(self, amount: int) -> bool:
    """Draws requested energy from available sources."""
    if self.energy < amount:
      return False
    
    remaining = amount
    for source, _ in self._sources:
      if remaining <= 0:
        break
      draw = min(remaining, source.energy)
      if source.consume(draw):
        remaining -= draw
    return remaining == 0
  
  def store(self, amount: int) -> int:
    """Distributes energy across available storage."""
    remaining = amount
    for source, _ in self._sources:
      if remaining <= 0:
        break
      remaining = source.store(remaining)
    return remaining
