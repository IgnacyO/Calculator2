from kivy.properties import ObjectProperty, VariableListProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from theme import CustomTheme


class Display(MDBoxLayout):
    operation_label = ObjectProperty(None)
    argument_label = ObjectProperty(None)
    secondary_color = VariableListProperty(CustomTheme.GREY)
    primary_color = VariableListProperty(CustomTheme.DARK_GREY)

    def display_argument(self, value: str) -> None:
        self.argument_label.text = value

    def display_operation(self, value: str) -> None:
        self.operation_label.text = value
 
    @staticmethod
    def get_display():
        return MDApp.get_running_app().root.ids.display
