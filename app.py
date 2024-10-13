from kivymd.app import MDApp, Builder
from kivymd.theming import ThemeManager
from calculator import Calculator
from interface import Interface
from utils.loaders import load_kv_files, load_settings
from view.display import Display


class CalculatorApp(MDApp):

    def build(self):
        self.theme_cls = ThemeManager()

        import view

        load_kv_files()
        self.settings = load_settings()
        
        return Builder.load_file("view/main.kv")
    
    def on_start(self):
        calculator = Calculator(self.settings.get("precision_n_digits"))
        display: Display = Display.get_display()
        self.interface = Interface(calculator, display, self.settings.get("precision_n_digits"))
        return super().on_start()
    

if __name__ == "__main__":
    CalculatorApp().run()