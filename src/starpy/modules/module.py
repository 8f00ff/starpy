# -*- coding: utf-8 -*-
"""
Module: Base factory system for creating and managing ship modules.

Author: 8f00ff (Vi)
Version: 1.0.0
License: MIT
"""

from abc import abstractmethod
from typing import Callable, Dict

class Module:
  """Provides factory pattern and core functionality for all ship modules."""
  
  _registry = {}
  
  def __init__(self) -> None:
    self.__module_type: str = None
  
  @property
  def module_type(self) -> str:
    """Returns the unique identifier for this module type."""
    return self.__module_type
  
  @module_type.setter
  def module_type(self, value: str) -> None:
    """Sets the module type identifier, only allowing one-time initialization."""
    if self.__module_type is None:
      self.__module_type = value
  
  @classmethod
  def register(cls, module_type: str, factory: Callable[..., 'Module']) -> None:
    """Registers a new module factory for creating module instances."""
    if module_type in cls._registry:
      return
    def wrapped_factory(*args, **kwargs):
      instance = factory(*args, **kwargs)
      instance.module_type = module_type
      return instance
    cls._registry[module_type] = wrapped_factory
  
  @classmethod
  def create(cls, module_type: str, *args, **kwargs) -> 'Module':
    """Creates a new module instance using the registered factory."""
    if module_type not in cls._registry:
      raise ValueError(f"Module type '{module_type}' is not registered.")
    return cls._registry[module_type](*args, **kwargs)
  
  @classmethod
  def register_presets(cls):
    """Registers default module configurations."""
    if cls is Module:
      return
    cls.register(cls.__name__, cls)
  
  @abstractmethod
  def status(self) -> Dict:
    """Returns the current state of the module."""
    return {
      "type": self.module_type
    }
