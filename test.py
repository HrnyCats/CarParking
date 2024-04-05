from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.pickers import MDModalDatePicker

KV = '''
MDScreen:
    MDNavigationLayout:
        MDScreenManager:
            MDScreen:
               

                MDButton:
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    on_release: app.show_date_picker()

                    MDButtonText:
                        text: "Open modal date picker dialog"
'''


class Example(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Olive"
        self.theme_cls.theme_style = "Dark"
        print(self.theme_cls.backgroundColor)
        return Builder.load_file("test.kv")

    def show_date_picker(self):
        date_dialog = MDModalDatePicker()
        date_dialog.open()


Example().run()