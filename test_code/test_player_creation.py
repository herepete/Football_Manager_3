#!/usr/bin/python3
import sys
sys.path.append('..')
import pytest

def test_method():
    try:
        import player_creation
        #bla

    except:
        x=5
        y=6
        assert x == y,"test failed"
