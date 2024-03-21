from kivymd.app import MDApp


import sqlite3

class MainApp(MDApp):
    connection = None
    cursor = None

    def on_start(self):
        # Initialize GPS

        # Connect to database
        self.connection = sqlite3.connect("Parks.db")
        self.cursor = self.connection.cursor()


MainApp().run()
    