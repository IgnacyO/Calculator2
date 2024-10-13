from decimal import Decimal
from kivymd.app import MDApp
from calculator import Calculator


class Interface:
    """Interface between calculator and display."""
    def __init__(self, calculator: Calculator, display, PRECISION_N_DIGITS: int) -> None:
        self.calculator = calculator
        self.display = display
        self.PRECISION_N_DIGITS = PRECISION_N_DIGITS

    @staticmethod
    def get_interface():
        return MDApp.get_running_app().interface

    def backspace(self) -> None:
        """Pops the last prompted digit from the argument"""
        old_value_s = str(self.calculator.get_value())
        if old_value_s != "0":
            new_value = old_value_s[:-1]
            if new_value == "": new_value = "0"
            self.calculator.set_value(Decimal(new_value))
        self.update_display()

    def change_sign(self) -> None:
        """Changes sign of the argument to opposite"""
        self.calculator.change_sign()
        self.update_display()
    
    def clear_all(self) -> None:
        """Clears all memory"""
        self.calculator.clear_all()
        self.update_display()

    def equals(self) -> None:
        """Executes set operation class and displays result"""
        try:
            if self.calculator.operation is None:
                return
            self.update_display(show_result=True)
            operation = getattr(self.calculator.operation, "do", print)
            result_number = operation(self.calculator.arguments, self.calculator.precision, self.calculator.PRECISION_N_DIGITS)
            max_number = pow(10, self.calculator.PRECISION_N_DIGITS)
            if result_number > max_number:
                self.calculator.clear_all()
                self.display.display_argument("Error: Too big number")
            else:
                rounded_result_number = round(result_number, self.calculator.PRECISION_N_DIGITS)
                self.calculator.argument_ptr = 0
                self.calculator.set_value(rounded_result_number)
                self.update_display(omit_operation=True, show_result=True)
        except ZeroDivisionError:
            self.calculator.clear_all()
            self.display.display_argument("Error: Division by 0")

    def erase(self) -> None:
        """Erases the current argument"""
        self.calculator.erase()
        self.update_display()

    def float_on(self) -> None:
        """Sets the current argument input as float part"""
        self.calculator.float_on[self.calculator.argument_ptr] = True
        self.update_display()

    def format_argument_s(self, argument: Decimal, float_on: bool) -> str:
        formatted_s = ""
        formatted_s += str(argument.normalize())
        formatted_s += "." if float_on and (str(argument) == "0" or "." not in str(argument)) else ""
        return formatted_s
    
    def format_operation_s(self, arguments: list[Decimal], argument_ptr: int, operation, show_result) -> str:
        if operation is None: return ""
        formatted_s = ""
        formatted_s += f" {getattr(operation, "format", print)(arguments, argument_ptr)} "
        formatted_s += "=" if show_result else ""
        return formatted_s

    def numeric_input(self, value: str) -> None:
        """Writes the given digit value to the current argument."""
        current_val = str(self.calculator.get_value())
        int_part, float_part = current_val.split(".") if "." in current_val else (current_val, "")
        if len(int_part) >= self.precision or len(float_part) >= self.precision:
            return
        new_value_s = str(self.calculator.get_value())
        if not self.calculator.float_on[self.calculator.argument_ptr] and new_value_s == "0":
            new_value_s = value
        else:
            new_value_s += "." + value if self.calculator.float_on[self.calculator.argument_ptr] and "." not in new_value_s else value
        self.calculator.set_value(Decimal(new_value_s))
        self.update_display()

    def operation(self, operation_cls, execute_immediately: bool = False) -> None:
        """Sets the given operation class as the operator. Can force immediate equals execution."""
        self.calculator.operation = operation_cls
        if execute_immediately:
            self.equals()
        else:
            self.calculator.argument_ptr = 1
            self.calculator.float_on[1] = False
            self.calculator.set_value(0)

    def update_display(self, omit_operation: bool = False, show_result: bool = False) -> None:
        """Updates display based on calculator state."""
        arguments, argument_ptr, float_on, operation = self.calculator.get_state()
        formatted_argument_s = self.format_argument_s(arguments[argument_ptr], float_on[argument_ptr])
        self.display.display_argument(formatted_argument_s)
        if omit_operation: return
        formatted_operation_s = self.format_operation_s(arguments, argument_ptr, operation, show_result)
        self.display.display_operation(formatted_operation_s)
