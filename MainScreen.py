from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen

class MainScreen(MDScreen):
    link_screen_manager = ObjectProperty(None)
    link_reservation_screen = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)