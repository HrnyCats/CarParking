from kivymd.uix.textfield import MDTextField
from kivy.properties import NumericProperty

class TextInputField(MDTextField):
    max_characters = 0
    def insert_text(self, substring, from_undo=False):
        if len(self.text) > self.max_characters and self.max_characters > 0:
            substring = ""
        MDTextField.insert_text(self, substring, from_undo)
