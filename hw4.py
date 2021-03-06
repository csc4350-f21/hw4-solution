# ASSIGNMENT: The below is a common design pattern that can be cleaned up.
# We have a lengthy mathematical operation that uses a few pieces of
# information several times in order to mutate a value. This code organization
# isn't inherently wrong, but it does result in some pretty messy callsites,
# especially once we introduce nested function calls in compound_op_it().
# 
# The goal of this assignment is to refactor the below into a class: 
# 1) Shared arguments between functions should become instance variables of the class
# in order to minimize clutter (because now they won't have to be arguments
# to each function). 
# 2) The class should have a function self.complicated_math_operation()
# that accomplishes everything complicated_math_operation() currently does.
# 3) There's a design decision lurking in here! Should we make the starting_value
# an instance variable of the class that each function call mutates, or should we
# keep the current structure where complicated_math_operation() accepts a starting value
# and repeatedly mutates it? Leave a comment explaining which one you chose
# and under what circumstances that might make sense. There's no right answer! 

import math

class MathOperation:
    def __init__(self, starting_value, min_value, max_value, coefficient):
        self.val = starting_value
        self.min_value = min_value
        self.max_value = max_value
        self.coefficient = coefficient
    
    def add_it(self):
        self.val = max(self.min_value, min(self.max_value, self.val + self.coefficient))

    def multiply_it(self):
        self.val = max(self.min_value, min(self.max_value, self.val * self.coefficient))

    def sqrt_it(self):
        self.val = max(self.min_value, min(self.max_value, math.pow(self.val, -self.coefficient)))

    def compound_op_it(self):
        self.multiply_it()
        self.add_it()

def complicated_math_operation(starting_value, min_value, max_value, coefficient):
    # Design decision: mutated starting_value under the hood in MathOperation. 

    # Possible justification: it cleans up the callsites a bit, so it's easier to chain
    # operations. Another possible reason is that it could conceivably let MathOperation
    # act as more of a black box in case we want to maintain some state in that class
    # and restrict the caller's ability to mutate `val`.

    # Possible counter-justifications: Maybe we want the caller to have more access
    # to `val` depending on how we're going to use MathOperation. Maybe we want to use
    # the MathOperation class to operate on multiple input values or branch which operation
    # we do based on some conditional logic. In either case, hiding `val` from the caller
    # slows us down a little bit.
    
    # Any minimal justification is an acceptable answer here.

    CMO = MathOperation(starting_value, min_value, max_value, coefficient)
    CMO.multiply_it()
    CMO.add_it()
    CMO.sqrt_it()
    CMO.compound_op_it()
    return CMO.val