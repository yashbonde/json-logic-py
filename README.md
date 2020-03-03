# JsonLogicPy2

This is an extension on top of original (json-logic-py)[https://github.com/nadirizr/json-logic-py], the original source code is still untouched. I merely add more functionality and build on top of it. 

I have a vision that non-technical business users must have power of doing what they want without having to depend on the programming style, only put in their business rules and code should be able to automanage the flow. There are three main things for any business user:

1. Can I configure the flow myself, without having dependencies?
2. How can I add more complicated logic and can I reuse those?
3. Can the logic automatically handle and tell me when issues arise, such as null values?
4. Can I just use this in my existing suite of sofware without having to get support?

This toolkit `jsonlogic2` aims to solve these problems, for this we have added the following:

1. Auto logic tree generation and processing `nested_logic.py`
2. Ability to add your own extensions in `extensions.py`
