from parse import parse

import sys

config = {
    "current_scope": None
}
functions = {}
variables = {}

filename = None
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    print("You must provide a filename")
    sys.exit()

with open(filename, 'r') as f:
    parse(f.read(), config, functions, variables)
