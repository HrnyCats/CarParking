from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from kivy.app import App


class ReservationScreen(MDScreen):
    titleParking = ObjectProperty()
    addressParking = ObjectProperty()
    dateParking = ObjectProperty()
    time = ObjectProperty()
    numbersCar = ObjectProperty()

    def __init__(self,  **kwargs):
        super(ReservationScreen, self).__init__(**kwargs)

    def filling_in_the_data(self, dataPressedCarParking):
        self.titleParking.text = dataPressedCarParking["Name"]
        self.addressParking.text = dataPressedCarParking["address"]
        # self.timeStart.text = dataPressedCarParking["schedule_time_start"]
        # self.timeEnd.text = dataPressedCarParking["schedule_time_end"]
        self.numbersCar.text = "тут должен быть номер"
