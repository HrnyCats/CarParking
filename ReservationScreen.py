from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from kivy.app import App


class ReservationScreen(MDScreen):
    link_screen = ObjectProperty()
    titleParking = ObjectProperty()
    typePark = ObjectProperty()
    addressParking = ObjectProperty()
    dateParking = ObjectProperty()
    time = ObjectProperty()
    numbersCar = ObjectProperty()
    id = 0

    def __init__(self,  **kwargs):
        super(ReservationScreen, self).__init__(**kwargs)

    def filling_in_the_data(self, dataPressedCarParking):
        self.id = dataPressedCarParking['id_car_parking']
        self.titleParking.text = dataPressedCarParking["Name"]
        self.typePark.text = dataPressedCarParking["type_car_park "]
        self.addressParking.text = dataPressedCarParking["address"]
        # self.timeStart.text = dataPressedCarParking["schedule_time_start"]
        # self.timeEnd.text = dataPressedCarParking["schedule_time_end"]

    def proceed_to_payment(self):
        self.link_screen.link_payment_screen.setIdPark(self.id)
        self.link_screen.link_screen_manager.current = "screen3"