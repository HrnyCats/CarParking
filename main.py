import sqlite3
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivymd.app import MDApp
from kivy.clock import Clock
from kivymd.uix.pickers import MDModalInputDatePicker, MDModalDatePicker
from kivymd.uix.pickers import MDTimePickerInput
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarSupportingText, MDSnackbarText
from kivymd.theming import ThemeManager
from kivy.metrics import dp
from ParksMapView import ParksMapView
from BottomSheet import BottomSheet
from MainScreen import MainScreen
from ReservationScreen import ReservationScreen
from PaymentScreen import PaymentScreen
from TextInputField import TextInputField

class MainApp(MDApp):
    screen = None #эта переменная чтобы запоминать окно бронирования, по факту костыль(времени мало)
    connection = None
    cursor = None
    map_sources = {
        "street": "https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}",
        "sputnik": "https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}",
        "hybrid": "https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
    }
    current_map = StringProperty("street")

    def __init__(self, **kwargs):
        super(MainApp, self).__init__()
        # self.connection = sqlite3.connect("Parks.db")
        # self.cursor = self.connection.cursor()

    def on_start(self):
        super().on_start()
        # Initialize GPS
        
        

        # Connect to database
        self.connection = sqlite3.connect("Parks.db")
        self.cursor = self.connection.cursor()
        

    def build(self):
        return Builder.load_file("main.kv")

    def show_modal_input_date_picker(self, *args):
        def on_edit(*args):
            self.date_dialog.dismiss()
            Clock.schedule_once(self.show_date_picker, 0.2)

        self.date_dialog = MDModalDatePicker()
        self.date_dialog.bind(on_edit=on_edit)
        self.date_dialog.bind(on_ok=self.on_ok)
        self.date_dialog.bind(on_cancel=self.on_cancel)
        self.date_dialog.bind(on_select_day=self.on_select_day)
        self.date_dialog.bind(on_select_month=self.on_select_month)
        self.date_dialog.bind(on_select_year=self.on_select_year)
        self.date_dialog.open()

    #методы для красивой даты
    def on_edit(self, instance_date_picker):
        instance_date_picker.dismiss()
        Clock.schedule_once(self.show_modal_input_date_picker, 0.2)

    def on_select_day(self, instance_date_picker, number_day):
        instance_date_picker.dismiss()

        MDSnackbar(
            MDSnackbarSupportingText(
                text=f"Выбранный день - {number_day}",
            ),
            y=dp(24),
            orientation="horizontal",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
            background_color="olive"
        ).open()

    def on_select_month(self, instance_date_picker, number_month):
        #instance_date_picker.dismiss()

        MDSnackbar(
            MDSnackbarSupportingText(
                text=f"Выбранный месяц - {number_month}",
            ),
            y=dp(24),
            orientation="horizontal",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
            background_color="olive"
        ).open()

    def on_cancel(self, instance_date_picker):
        instance_date_picker.dismiss()

    def on_ok(self, instance_date_picker):
        self.screen.dateParking = instance_date_picker.get_date()

        MDSnackbar(
            MDSnackbarText(
                text="Выбранная дата:",
            ),
            MDSnackbarSupportingText(
                text="\n".join(str(date) for date in instance_date_picker.get_date()),
                padding=[0, 0, 0, dp(12)],
            ),
            y=dp(124),
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
            padding=[0, 0, "8dp", "8dp"],
        ).open()

        instance_date_picker.dismiss()

    def on_select_year(self, instance_date_picker, number_year):
        MDSnackbar(
            MDSnackbarSupportingText(
                text=f"Выбранный год - {number_year}",
            ),
            y=dp(24),
            orientation="horizontal",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
            background_color="olive"
        ).open()

    def show_date_picker(self, screen):
        self.date_dialog = MDModalInputDatePicker()
        if not self.screen:
            self.screen = screen
        self.date_dialog.bind(on_edit=self.on_edit)
        self.date_dialog.bind(on_ok=self.on_ok)
        self.date_dialog.bind(on_cancel=self.on_cancel)
        self.date_dialog.open()

    def on_cancel_time(self, time_picker_vertical):
        time_picker_vertical.dismiss()

    def on_ok_time(self, time_picker_vertical):
        self.screen.timeParking = time_picker_vertical.time

        MDSnackbar(
            MDSnackbarSupportingText(
                text=f"Time is `{time_picker_vertical.time}`",
            ),
            y=dp(24),
            orientation="horizontal",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
        ).open()

        time_picker_vertical.dismiss()

    def show_time_picker(self, screen):
        if not self.screen:
            self.screen = screen
        time_dialog = MDTimePickerInput()
        time_dialog.bind(on_cancel=self.on_cancel_time)
        time_dialog.bind(on_ok=self.on_ok_time)
        time_dialog.open()

MainApp().run()
