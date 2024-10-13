from kivy.properties import StringProperty, VariableListProperty
from kivymd.uix.button import MDButton
from interface import Interface
from maths import *
from theme import CustomTheme


class FunctionalKey:
    bg_color = CustomTheme.LIGHT_GREY


class Key(MDButton):
    primary_color = VariableListProperty(CustomTheme.DARK_GREY)


class KeyIcon(Key):
    display_icon = StringProperty("")


class KeyText(Key):
    display_text = StringProperty("B")


class NumericKey(KeyText):
    numeric_val = StringProperty("")
    display_text = numeric_val

    def on_press(self, *args) -> None:
        interface: Interface = Interface.get_interface()
        interface.numeric_input(self.numeric_val)


class AdditionKey(FunctionalKey, KeyIcon):
    display_icon = "plus"

    def on_press(self, *args) -> None:
        interface: Interface = Interface.get_interface()
        interface.operation(Addition)


class BackspaceKey(FunctionalKey, KeyIcon):
    display_icon = "backspace-outline"

    def on_press(self, *args) -> None:
        interface: Interface = Interface.get_interface()
        interface.backspace()


class ClearAllKey(FunctionalKey, KeyText):
    display_text = "C"

    def on_press(self, *args) -> None:
        interface: Interface = Interface.get_interface()
        interface.clear_all()


class CosineKey(FunctionalKey, KeyText):
    display_text = "cos(x)"

    def on_press(self, *args) -> None:
        interface: Interface = Interface.get_interface()
        interface.operation(Cosine, execute_immediately=True)


class DivisionKey(FunctionalKey, KeyIcon):
    display_icon = "division"

    def on_press(self, *args) -> None:
        interface: Interface = Interface.get_interface()
        interface.operation(Division)


class EqualsKey(KeyIcon):
    bg_color = CustomTheme.BLUE
    display_icon = "equal"

    def on_press(self, *args) -> None:
        interface: Interface = Interface.get_interface()
        interface.equals()


class EraseKey(FunctionalKey, KeyText):
    display_text = "CE"

    def on_press(self, *args) -> None:
        interface: Interface = Interface.get_interface()
        interface.erase()


class EulerExponentKey(FunctionalKey, KeyText):
    display_text = "e[sup]x[/sup]"

    def on_press(self, *args) -> None:
        interface: Interface = Interface.get_interface()
        interface.operation(EulerExponent, execute_immediately=True)


class ExponentKey(FunctionalKey, KeyIcon):
    display_icon = "exponent"

    def on_press(self, *args) -> None:
        interface: Interface = Interface.get_interface()
        interface.operation(Exponent)


class FloatKey(FunctionalKey, KeyIcon):
    display_icon = "circle-small"
    
    def on_press(self, *args) -> None:
        interface: Interface = Interface.get_interface()
        interface.float_on()


class MultiplicationKey(FunctionalKey, KeyIcon):
    display_icon = "close"

    def on_press(self, *args) -> None:
        interface: Interface = Interface.get_interface()
        interface.operation(Multiplication)


class SignKey(FunctionalKey, KeyIcon):
    display_icon = "plus-minus-variant"

    def on_press(self, *args) -> None:
        interface: Interface = Interface.get_interface()
        interface.change_sign()
        return super().on_press(*args)


class SineKey(FunctionalKey, KeyText):
    display_text = "sin(x)"

    def on_press(self, *args) -> None:
        interface: Interface = Interface.get_interface()
        interface.operation(Sine, execute_immediately=True)


class SubstractionKey(FunctionalKey, KeyIcon):
    display_icon = "minus"

    def on_press(self, *args) -> None:
        interface: Interface = Interface.get_interface()
        interface.operation(Substraction)