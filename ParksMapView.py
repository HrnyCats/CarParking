from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from kivy.uix.label import Label
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.boxlayout import MDBoxLayout
from ParkMarker import ParkMarker
from kivymd.uix.behaviors import TouchBehavior
from kivy.properties import StringProperty,ObjectProperty
from BottomSheet import BottomSheet
from kivymd.uix.bottomsheet import MDBottomSheet
from kivymd.uix.list.list import MDList, MDListItem
from Singleton import Singleton


class ParksMapView(MapView, TouchBehavior, Singleton):
    gettingParksTimer = None
    bottom_sheet = BottomSheet
    parkAdresses = []
    flag = False

    def __init__(self,**kwargs, ):
        super(ParksMapView, self).__init__(**kwargs)

    # def buildBottomSheet(self):
    #     self.bottom_sheetLayout = MDBoxLayout(orientation="vertical")
    #     self.listData = MDList()
    #     self.bottom_sheetLayout.add_widget(self.listData)
    #
    #     buttonBox = MDBoxLayout()
    #     buttomReservation = MDButton(MDButtonText(text="Бронировать"))
    #     buttonBox.add_widget(buttomReservation)
    #     buttomPay = MDButton(MDButtonText(text="Оплата"), md_bg_color="Green")
    #     buttonBox.add_widget(buttomPay)
    #     self.bottom_sheetLayout.add_widget(buttonBox)



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
        # if self.bottom_sheet:
        #     self.bottom_sheet.set_state("toggle")
        # return
        self.bottom_sheet.link_list.clear_widgets()

        headers = "id_car_parking,lon,lat,address,price,type_car_park,places_with_disabilities,schedule_time_start,schedule_time_end,schedule_weekday_start,schedule_weekday_end,Name"
        headers = headers.split(',')

        dataPressedCarParking = args[0].parkData

        dataParking = {}
        labels = []
        for i in range(2, len(headers)):
            attributeName = headers[i]
            attributeValue = dataPressedCarParking[i]

            dataParking[attributeName] = attributeValue

            labels.append(Label(text=f"{attributeName}: {attributeValue}"))
            labels[-1].color = (0,0,0,1)
            listitem = MDListItem(labels[-1])
            listitem.padding = [0,0,0,0]
            #listitem.height = 50
            #listitem.size_hint = 1, None
            #listitem.height = self.bottom_sheet.height / len(headers)
            self.bottom_sheet.link_list.add_widget(listitem)

        self.bottom_sheet.dataPressedCarParking = dataParking

        if self.bottom_sheet:
            self.bottom_sheet.set_state("toggle")

        

