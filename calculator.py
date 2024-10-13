from decimal import Decimal


class Calculator:
    """Class that mimics calculator socket interface"""

    def __init__(self, PRECISION_N_DIGITS: int) -> None:
        self.PRECISION_N_DIGITS = PRECISION_N_DIGITS
        self.precision = pow(10, -PRECISION_N_DIGITS)
        self.argument_ptr = 0
        self.arguments: list[Decimal] = [Decimal(0), Decimal(0)]
        self.float_on: list[bool] = [False, False]
        self.operation = None
        
    def change_sign(self) -> None:
        self.arguments[self.argument_ptr] = -self.arguments[self.argument_ptr]

    def clear_all(self) -> None:
        self.argument_ptr = 0
        self.arguments = [Decimal(0), Decimal(0)]
        self.float_on = [False, False]
        self.operation = None
    
    def erase(self) -> None:
        self.set_value(Decimal(0))
        self.float_on[self.argument_ptr] = False
    
    def get_state(self) -> tuple:
        return self.arguments, self.argument_ptr, self.float_on, self.operation

    def get_value(self) -> Decimal:
        return self.arguments[self.argument_ptr]

    def set_value(self, value: Decimal) -> None:
        self.arguments[self.argument_ptr] = value 