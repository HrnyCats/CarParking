from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from ParkMarker import ParkMarker

from kivymd.uix.behaviors import TouchBehavior

class ParksMapView(MapView, TouchBehavior):
    gettingParksTimer = None
    parkAdresses = []

    def StartGettingParksInFov(self):
        # Каждую секунду, получаем маркеты в поле зрении
        try:
            self.gettingParksTimer.cancel()
        except:
            pass
        
        self.gettingParksTimer = Clock.schedule_once(self.GetParksInFov, 1)

    def GetParksInFov(self, *args):
        minLat, minLon, maxLat, maxLon = self.get_bbox()
        app = App.get_running_app()
        sqlStatement = "Select * FROM Parks WHERE lon > %s AND lon < %s AND lat > %s AND lat < %s "%(minLon, maxLon, minLat, maxLat)
        app.cursor.execute(sqlStatement)
        parks = app.cursor.fetchall()
        print(parks)
        for park in parks:
            adress = park[3]
            if adress in self.parkAdresses:
                continue
            else:
                self.AddPark(park)

    def AddPark(self, park):
        lon, lat = park[1], park[2]
        marker = ParkMarker(lon = lon, lat = lat)
        marker.parkData = park
        # Добавляет маркер на карту
        self.add_widget(marker)

        adress = park[3]
        self.parkAdresses.append(adress)
