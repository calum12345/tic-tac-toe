#!/usr/bin/env python3

import curses as crs
from ticTacToe import ticTacToe

def main():
    crs.refresh()

crs.wrapper(main)