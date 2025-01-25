# -*- coding: utf-8 -*-
"""
Ship: Core class managing modular ship systems.

Author: 8f00ff (Vi)
Version: 1.0.0
License: MIT
"""

from typing import List, Type, Optional, TypeVar

from starpy.modules.module import Module

T = TypeVar("T", bound=Module)

class Ship:
  """Manages a collection of ship modules and their interactions."""
  
  def __init__(self, modules: Optional[List[Module]] = None):
    self._modules: List[Module] = modules
  
  def add_module(self, module: Module) -> None:
    """Adds a new module to the ship's systems."""
    self._modules.append(module)
  
  def remove_module(self, module: Module) -> None:
    """Removes an existing module from the ship's systems."""
    self._modules.remove(module)
  
  def get_module(self, module_type: Type[Module]) -> Module:
    """Returns the first module matching the specified type."""
    return next((m for m in self._modules if isinstance(m, module_type)), None)
  
  def get_modules(self, module_type: Type[T]) -> List[T]:
    """Returns all modules matching the specified type."""
    return [m for m in self._modules if isinstance(m, module_type)]
  
  def status(self) -> dict:
    """Returns the current status of all ship systems."""
    return {
      "modules": [module.status() for module in self._modules]
    }
