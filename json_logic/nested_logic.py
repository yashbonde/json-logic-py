"""nested_logic.py

Uses the base jsonlogic and adds additional functionality like
auto generation of parse tree and additional features. There
should be a rise of methods that help very simple setting up
of business logic by the user so that he is powered to do what
he wants and not be limited by a programmer. A simple understanding
of rules should be enough, and it is the code that can automatically
structure it and use it as the data comes.

Take in the business rules, make sense of those, order them in which
to process and perform the end goal operations.

02.03.2020 - @yashbonde"""

class ProcessNode:
    pass

def make_tree(formula_objects):
    """
    This function takes in the formula obejcts and returns the processing tree

    :param formulas: List of formula objects like 
    form_obj = {
        "formula": json-formula as dictionary,
        "depends_on": list of variables it uses
        "dependents": list of variables that use it's value (relevant?)
    }
    """
    pass

def calculate_tree(tree, data):
    """takes in the tree object and performs calculation by traversing post-order"""
    pass
