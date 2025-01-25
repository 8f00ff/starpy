#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
StarPy: A detailed spaceship systems simulator entry point.

Author: 8f00ff (Vi)
Version: 1.0.0
License: MIT
"""

from argparse import ArgumentParser, Namespace
from linecache import getline
from os import path
from sys import settrace

from starpy.game import run

def parse_args() -> Namespace:
  """Parse and validate command line arguments."""
  parser: ArgumentParser = ArgumentParser()
  parser.add_argument("-d", "--debug", action="store_true", help="show extra debug information")
  parser.add_argument("-n", "--name", type=str, help="set ship name", required=True)
  args: Namespace = parser.parse_args()
  return args

def trace_calls(frame, event, _):
  """Trace execution of code lines for debugging."""
  if event == "line":
    current_file = frame.f_code.co_filename
    main_dir = path.dirname(path.abspath(__file__))
    if current_file.startswith(main_dir):
      filename = path.basename(current_file)
      lineno = frame.f_lineno
      line = getline(filename, lineno).strip()
      print(f"{filename}:{lineno}: {line}")
  return trace_calls

def main() -> None:
  """Program entry point."""
  _args: Namespace = parse_args()
  if _args.debug:
    settrace(trace_calls)
  run(_args)
  settrace(None)

if __name__ == "__main__":
  main()
