from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from kivy.app import App

class PaymentScreen(MDScreen):
    id_park = None
    link_numbersCard = ObjectProperty(None)
    link_expiryDateYears = ObjectProperty(None)
    link_expiryDateMonths = ObjectProperty(None)
    link_cv_code = ObjectProperty(None)
    link_screen = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(PaymentScreen, self).__init__(**kwargs)

    def setIdPark(self, id):
        self.id_park = id
    def payment(self):
        if not (self.link_numbersCard.text and self.link_expiryDateYears.text and self.link_expiryDateMonths.text and self.link_cv_code.text):
            return

        time = self.link_screen.link_reservation_screen.timeParking
        minutes = time.minute
        for i in range(time.hour):
            minutes += 60

        args = (self.id_park,
                int(self.link_screen.link_reservation_screen.numbersCar.text),
                minutes,
                int(self.link_numbersCard.text),
                self.link_expiryDateYears.text + "/" + self.link_expiryDateMonths.text,
                int(self.link_cv_code.text)
        )
        app = App.get_running_app()
        sqlStatement = f"INSERT INTO Payment (id_car_park, car_number, duration, card_numbers, expiry_date, CV_code) VALUES ({args[0]}, {args[1]}, {args[2]}, {args[3]}, {args[4]}, {args[5]})"
        app.cursor.execute(sqlStatement)
        app.connection.commit()

    def back(self):
        self.link_numbersCard.text = ""
        self.link_expiryDateYears = ""
        self.link_expiryDateMonths = ""
        self.link_cv_code.text = ""

        self.link_screen.link_screen_manager.current = "screen2"
