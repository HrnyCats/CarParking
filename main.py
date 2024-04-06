from kivy.lang import Builder
from kivy.properties import StringProperty,ObjectProperty
from kivymd.app import MDApp
from ParksMapView import ParksMapView
from BottomSheet import BottomSheet
from MainScreen import MainScreen
from ReservationScreen import ReservationScreen
from kivymd.uix.pickers import MDModalInputDatePicker
from kivymd.theming import ThemeManager
from kivy.metrics import dp
import sqlite3


class MainApp(MDApp):
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

    def show_date_picker(self):
        date_dialog = MDModalInputDatePicker()
        date_dialog.open()

MainApp().run()
