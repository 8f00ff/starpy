# -*- coding: utf-8 -*-
"""
Tests: Unit tests for ship identification module.

Author: 8f00ff (Vi)
Version: 1.0.0
License: MIT
"""

from starpy.modules.identificator import Identificator

def test_identificator_name():
  """Test ship name setting and getting."""
  name = "Serenity"
  id_module = Identificator(name)
  assert id_module.ship_name == name
  
  new_name = "Enterprise"
  id_module.ship_name = new_name
  assert id_module.ship_name == new_name

def test_serial_number_uniqueness():
  """Test that each module gets a unique serial number."""
  id1 = Identificator("Ship1")
  id2 = Identificator("Ship2")
  assert id1.serial_number != id2.serial_number
