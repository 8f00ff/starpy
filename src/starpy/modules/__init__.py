# -*- coding: utf-8 -*-
"""
Modules: Dynamic module loader for ship systems and components.

Author: 8f00ff (Vi)
Version: 1.0.0
License: MIT
"""

import os
import importlib

__all__ = []

module_dir = os.path.dirname(__file__)
for filename in os.listdir(module_dir):
  if filename.endswith(".py") and filename != "__init__.py":
    module_name = filename[:-3]
    imported_module = importlib.import_module(f"starpy.modules.{module_name}")
    for attr_name in dir(imported_module):
      attr = getattr(imported_module, attr_name)
      if isinstance(attr, type) and hasattr(attr, "register_presets"):
        attr.register_presets()

    for attr_name in dir(imported_module):
      attr = getattr(imported_module, attr_name)
      if isinstance(attr, type):
        globals()[attr_name] = attr
        __all__.append(attr_name)
