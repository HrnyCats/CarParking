from kivy.lang import Builder
from kivy.properties import StringProperty,ObjectProperty
from kivymd.app import MDApp
from ParksMapView import ParksMapView
from BottomSheet import BottomSheet
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

    def on_start(self):
        # Initialize GPS

        # Connect to database
        self.connection = sqlite3.connect("Parks.db")
        self.cursor = self.connection.cursor()
    
    def build(self):
        self.theme_cls.primary_palette = "Green"
        Builder.load_file("main.kv")
        return super().build()

main = MainApp().run()
