from kivy.properties import ObjectProperty
from kivymd.uix.bottomsheet import MDBottomSheet

class BottomSheet(MDBottomSheet):
    link_button = ObjectProperty(None)
    link_list = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(BottomSheet, self).__init__()