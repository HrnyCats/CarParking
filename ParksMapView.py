from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from kivy.uix.label import Label
from ParkMarker import ParkMarker
from kivymd.uix.behaviors import TouchBehavior
from kivy.properties import StringProperty,ObjectProperty
from kivymd.uix.bottomsheet import MDBottomSheet
from kivymd.uix.list.list import MDList, MDListItem
from Singleton import Singleton


class ParksMapView(MapView, TouchBehavior, Singleton):
    gettingParksTimer = None
    bottom_sheet = MDBottomSheet
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
        marker.bind(on_release = self.release)
        # Добавляет маркер на карту
        self.add_widget(marker)
        adress = park[3]
        self.parkAdresses.append(adress)


    def release(self, *args):
        headers = "id_car_parking,lon,lat,address,price,type_car_park,places_with_disabilities,schedule_time_start,schedule_time_end,schedule_weekday_start,schedule_weekday_end"
        headers = headers.split(',')

        dataPressedCarParking = args[0].parkData

        listData = MDList()
        labels = []
        for i in range(2, len(headers)):
            attributeName = headers[i]
            attributeValue = dataPressedCarParking[i]

            labels.append(Label(text=f"{attributeName}: {attributeValue}"))
            labels[-1].color = (0,0,0,1)
            listData.add_widget(MDListItem(labels[-1]))

        self.bottom_sheet.add_widget(listData)

        if self.bottom_sheet:
            self.bottom_sheet.set_state("toggle")
        

