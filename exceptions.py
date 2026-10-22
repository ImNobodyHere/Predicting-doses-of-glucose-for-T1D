import math as math

HARD_LIMIT = 300
SOFT_LIMIT = 150

class InvalidCarbsError(ValueError):
    pass


def validate_carbs(value):
    if value <= 0 or value > HARD_LIMIT:
        raise InvalidCarbsError("Invalid carbohydrate value")
    if math.isinfinity(value):
        raise InvalidCarbsError("Invalid carbohydrate value") 
    if value is not isinstance(value, (int, float)):
        return False
    else:
        return True
    
    
    
    
    # 1. type check: reject anything that is not an int or float
    #    gotcha: True and False count as ints in Python, reject bool first
    # 2. reject NaN and infinity
    #    gotcha: float("nan") <= 0 is False, so it slips past your range checks
    #    hint: the math module has a function for each
    # 3. reject value <= 0
    # 4. reject value > HARD_LIMIT
    # 5. set needs_confirmation = value > SOFT_LIMIT
    # return value, needs_confirmation