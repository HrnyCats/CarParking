from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from kivy.app import App

class PaymentScreen(MDScreen):
    id_park = None
    link_numbersCard = ObjectProperty(None)
    link_expiryDateYears = ObjectProperty(None)
    link_expiryDateMonths = ObjectProperty(None)
    link_cv_code = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(PaymentScreen, self).__init__(**kwargs)

    def setIdPark(self, id):
        self.id_park = id
    def payment(self):
        if not self.link_numbersCard.text and not self.link_expiryDateYears.text and not self.link_expiryDateMonths.text and self.link_cv_code.text:
            return

        app = App.get_running_app()
        sqlStatement = "INSERT INTO Payment (id_car_park, car_number, duration, card_numbers, expiry_date, CV_code) VALUES "%()
        # app.cursor.execute(sqlStatement)
        # parks = app.cursor.fetchall()

