import configparser
import os
from kivy.lang import Builder


def load_kv_files(view_directory: str = "view") -> None:
    for filename in os.listdir(view_directory):
        if filename.endswith(".kv") and not filename == "main.kv":
            kv_path = os.path.join(view_directory, filename)
            Builder.load_file(kv_path)

def load_settings(settings_file: str = "settings.ini") -> dict:
    settings = configparser.ConfigParser()
    settings.read(settings_file)
    return settings['DEFAULT']