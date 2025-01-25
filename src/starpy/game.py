#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Game: Core game initialization and runtime management.

Author: 8f00ff (Vi)
Version: 1.0.0
License: MIT
"""

from argparse import Namespace
from json import dumps

from starpy.ship import Ship
from starpy.modules.module import Module

def run(args: Namespace) -> None:
  """Initializes ship systems and starts the game."""
  
  ship: Ship = Ship([
    Module.create("Identificator", name=args.name),
    Module.create("SmallBattery", energy=1)
  ])
  
  print(dumps(ship.status(), indent=2))
