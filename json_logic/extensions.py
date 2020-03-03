"""extensions.py

This has code to add your own operations and configure them according
your requirements

03.03.2020 - @yashbonde"""

from json_logic import operations

EXTENSIONS = {
    "mean": lambda *args: sum(a if a else 0 for a in args) / sum(1 if a else 0 for a in args),
    **operations
}

def add_your_operation(name, func):
    if name in EXTENSIONS:
        raise ValueError("operation with name: `{}` already exists in your extensions".format(name))
    else:
        EXTENSIONS[name] = func
