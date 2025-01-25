#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SignalManager: Centralized signal/event manager for application-wide event handling.

Author: 8f00ff (Vi)
Version: 1.0.0
License: MIT
"""

from typing import Callable, Dict, List

class SignalManager:
  """Provides a priority-based event system for application-wide signal handling."""
  
  _listeners: Dict[str, List[Callable]] = {}
  
  @classmethod
  def connect(cls, signal_name: str, callback: Callable, priority: int = 0) -> None:
    """Registers a callback function to respond to a named signal."""
    if signal_name not in cls._listeners:
      cls._listeners[signal_name] = []
    cls._listeners[signal_name].append((priority, callback))
    cls._listeners[signal_name].sort(reverse=True, key=lambda x: x[0])

  @classmethod
  def emit(cls, signal_name: str, *args, **kwargs) -> None:
    """Triggers all callbacks registered to a signal in priority order."""
    if signal_name in cls._listeners:
      for _, callback in cls._listeners[signal_name]:
        callback(*args, **kwargs)
