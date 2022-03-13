# This file is responsible for saving variables between files.
# Not for the actual implementation of variables in Skate
# For that, see parse.py on L78

def init():
    global config
    config = {
        "variables": {},
        "functions": {},
        "line": 0,
        "current_scope": None
    }