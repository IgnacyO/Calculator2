from decimal import Decimal


# Round trig functions up to the n digits
TRIG_PRECISION = 4

def factorial(n: int) -> int:
    """Calculates factorial of n.

    Args:
        n (int)

    Returns:
        int: Calculated factorial
    """
    total = 1
    while n > 1:
        total *= n
        n -= 1
    return total

def trig_derivative(trig_func: int, sign: int) -> list[int, int]:
    """Finds derivative of the given trigonometry function(sine or cosine).

    The Meaning of the values:
    - 1 - cosine(x)
    - 0 - sine(x)

    Args:
        trig_func (int): 1 or 0
        sign (int): sign of the fuction. 1 positive and -1 negative

    Returns:
        list[int, int]: Derivative of the given trig function and its sign
    """
    if trig_func == 1:
        return (0, -sign)
    else:
        return (1, sign) 

class Addition:
    """Addition operation class"""
    @staticmethod
    def do(arguments: list[Decimal], precision: float, precision_n_digits: int) -> None:
        return Decimal(arguments[0] + arguments[1])

    @staticmethod
    def format(arguments: list[Decimal], arguments_ptr: int) -> str:
        formatted_s = ""
        formatted_s += str(arguments[0])
        formatted_s += " + "
        formatted_s += "(" if arguments[1] < 0 else ""
        formatted_s += f"{arguments[1] if arguments_ptr == 1 or (arguments_ptr == 0 and arguments[1] != 0) else ''}"
        formatted_s += ")" if arguments[1] < 0 else ""
        return formatted_s


class Cosine:
    """Cos(x) operation class, where x is angle in radians."""
    @staticmethod
    def do(arguments: list[Decimal], precision: float, precision_n_digits: int) -> None:
        x_rad = arguments[0] % 2
        n = 1
        total_sum = 1
        sn = 1
        fn = (0, -1)
        while abs(sn) > precision or (sn == 0 and fn[0]):
            sn = fn[1]*fn[0]*pow(x_rad, n)/factorial(n)
            total_sum += sn
            fn = trig_derivative(*fn)
            n += 1
        total_sum = round(total_sum, TRIG_PRECISION)
        return Decimal(total_sum)

    @staticmethod
    def format(arguments: list[Decimal], arguments_ptr: int) -> str:
        return f"cos({arguments[0]})"


class Division:
    """Division operation class."""
    @staticmethod
    def do(arguments: list[Decimal], precision: float, precision_n_digits: int) -> None:
        return Decimal(arguments[0]/arguments[1])

    @staticmethod
    def format(arguments: list[Decimal], arguments_ptr: int) -> str:
        formatted_s = ""
        formatted_s += str(arguments[0])
        formatted_s += " / "
        formatted_s += "(" if arguments[1] < 0 else ""
        formatted_s += f"{arguments[1] if arguments_ptr == 1 or (arguments_ptr == 0 and arguments[1] != 0) else ''}"
        formatted_s += ")" if arguments[1] < 0 else ""
        return formatted_s


class EulerExponent:
    """e^x operation class.

    e - euler's constant.
    
    The sum of the functional series is being calculated with the set precision.

    For numbers bigger than 10^`precision_n_digits` returns error.
    """
    @staticmethod
    def do(arguments: list[Decimal], precision: float, precision_n_digits: int) -> None:
        exponent = arguments[0]
        n = 1
        total_sum = 1
        sn = 1
        while abs(sn) > precision:
            sn = pow(exponent, n)/factorial(n)
            total_sum += sn
            n += 1
        return Decimal(total_sum)

    @staticmethod
    def format(arguments: list[Decimal], arguments_ptr: int) -> str:
        return f"e^{'(' if arguments[0] < 0 else ''}{arguments[0]}{')' if arguments[0] < 0 else ''}"
    

class Exponent:
    """Power(x^y) operation class."""
    @staticmethod
    def do(arguments: list[Decimal], precision: float, precision_n_digits: int):
        return Decimal(pow(arguments[0], arguments[1]))

    @staticmethod
    def format(arguments: list[Decimal], arguments_ptr: int) -> str:
        formatted_s = ""
        formatted_s += str(arguments[0])
        formatted_s += "^"
        formatted_s += "(" if arguments[1] < 0 else ""
        formatted_s += f"{arguments[1] if arguments_ptr == 1 or (arguments_ptr == 0 and arguments[1] != 0) else ''}"
        formatted_s += ")" if arguments[1] < 0 else ""
        return formatted_s


class Multiplication:
    """Multiplication class."""
    @staticmethod
    def do(arguments: list[Decimal], precision: float, precision_n_digits: int) -> None:
        return Decimal(arguments[0]*arguments[1])

    @staticmethod
    def format(arguments: list[Decimal], arguments_ptr: int) -> str:
        formatted_s = ""
        formatted_s += str(arguments[0])
        formatted_s += " * "
        formatted_s += "(" if arguments[1] < 0 else ""
        formatted_s += f"{arguments[1] if arguments_ptr == 1 or (arguments_ptr == 0 and arguments[1] != 0) else ''}"
        formatted_s += ")" if arguments[1] < 0 else ""
        return formatted_s
    

class Sine:
    """Sin(x) operation class, where x is angle in radians."""
    @staticmethod
    def do(arguments: list[Decimal], precision: float, precision_n_digits: int) -> None:
        x_rad = arguments[0] % 2
        n = 1
        total_sum = 0
        sn = 0
        fn = (1, 1)
        while abs(sn) > precision or (sn == 0 and fn[0]):
            sn = fn[1]*fn[0]*pow(x_rad, n)/factorial(n)
            total_sum += sn
            fn = trig_derivative(*fn)
            n += 1
        total_sum = round(TRIG_PRECISION)
        return Decimal(total_sum)

    @staticmethod
    def format(arguments: list[Decimal], arguments_ptr: int) -> str:
        return f"sin({arguments[0]})"
    

class Substraction:
    """Substraction operation class"""
    @staticmethod
    def do(arguments: list[Decimal], precision: float, precision_n_digits: int) -> None:
        return Decimal(arguments[0] - arguments[1])

    @staticmethod
    def format(arguments: list[Decimal], arguments_ptr: int) -> str:
        formatted_s = ""
        formatted_s += str(arguments[0])
        formatted_s += " - "
        formatted_s += "(" if arguments[1] < 0 else ""
        formatted_s += f"{arguments[1] if arguments_ptr == 1 or (arguments_ptr == 0 and arguments[1] != 0) else ''}"
        formatted_s += ")" if arguments[1] < 0 else ""
        return formatted_s