from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from kivymd.uix.pickers import MDDockedDatePicker


class MainScreen(MDScreen):
    link_screen_manager = ObjectProperty(None)
    link_reservation_screen = ObjectProperty(None)
    link_payment_screen = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

    def setDate(self, dobj):
        self.ids.set_date.text = str(dobj)
        pass

    def fromDate(self):
        self.foc = self.ids.set_date.focus
        if (self.foc == True):
            MDDockedDatePicker(self.setFDate).open()
        else:
            print("not")

