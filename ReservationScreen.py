from datetime import timedelta
from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from kivy.app import App


class ReservationScreen(MDScreen):
    link_screen = ObjectProperty()
    titleParking = ObjectProperty()
    addressParking = ObjectProperty()
    dateParking = None
    timeParking = None
    numbersCar = ObjectProperty()
    id = 0

    def __init__(self,  **kwargs):
        super(ReservationScreen, self).__init__(**kwargs)

    def filling_in_the_data(self, dataPressedCarParking):
        self.id = dataPressedCarParking['id_car_parking']
        self.titleParking.text = dataPressedCarParking["Name"]
        self.addressParking.text = dataPressedCarParking["address"]

    def proceed_to_payment(self):
        if not self.timeParking or not self.dateParking or not self.numbersCar.text:
            return

        self.link_screen.link_payment_screen.setIdPark(self.id)
        self.link_screen.link_screen_manager.current = "screen3"

    def back(self):
        self.dateParking = None
        self.timeParking = None

        self.link_screen.link_screen_manager.current = "screen1"