from kivy.properties import ObjectProperty
from kivymd.uix.bottomsheet import MDBottomSheet

class BottomSheet(MDBottomSheet):
    link_button = ObjectProperty(None)
    link_list = ObjectProperty(None)
    link_screen = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(BottomSheet, self).__init__()
        self.dataPressedCarParking = None

    def Reservation(self):
        if not self.dataPressedCarParking:
            return
        self.set_state("close")
        self.link_screen.link_reservation_screen.filling_in_the_data(self.dataPressedCarParking)
        self.link_screen.link_screen_manager.current = "screen2"


