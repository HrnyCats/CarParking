from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from kivy.uix.label import Label
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from ParkMarker import ParkMarker
from kivymd.uix.behaviors import TouchBehavior
from kivy.properties import StringProperty,ObjectProperty
from BottomSheet import BottomSheet
from kivymd.uix.bottomsheet import MDBottomSheet
from kivymd.uix.list.list import MDList, MDListItem, MDListItemHeadlineText, MDListItemSupportingText
from Singleton import Singleton
from kivymd.uix.pickers import MDModalDatePicker

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

        headers = "id_car_parking,lon,lat,address,price,type_car_park,places,places_with_disabilities,schedule_time_start,schedule_time_end,schedule_weekday_start,schedule_weekday_end,Name"
        headers = headers.split(',')

        dataPressedCarParking = args[0].parkData

        dataParking = {}
        labels = []
        for i in range(len(headers)):
            attributeName = headers[i]
            attributeValue = dataPressedCarParking[i]

            dataParking[attributeName] = attributeValue
        self.bottom_sheet.dataPressedCarParking = dataParking
        
        #Name, Type
        listItem = MDListItem(
                MDListItemHeadlineText(
                    text = str(dataParking["Name"]),
                    theme_text_color = "Custom",
                    text_color = "#000000",
                    font_style = "Title",
                    role = "medium",
                    font_size = 20,
                ),
                MDListItemSupportingText(
                    text = str(dataParking["type_car_park"]),
                    font_style = "Title",
                    role = "medium",
                    font_size = 13,
                ),
                theme_bg_color = "Custom",
                md_bg_color = self.bottom_sheet.md_bg_color,
            )
        listItem.height = 60
        self.bottom_sheet.link_list.add_widget(listItem)

        #Adress
        listItem = MDListItem(
                MDListItemHeadlineText(
                    text = "Адрес",
                    theme_text_color = "Custom",
                    text_color = "#AAAAAA",
                    font_style = "Title",
                    role = "medium",
                    font_size = 12,
                    #md_bg_color = self.bottom_sheet.md_bg_color,
            ),
                MDListItemSupportingText(
                    text = str(dataParking["address"]),
                    font_style = "Title",
                    role = "medium",
                    font_size = 14,
                    #md_bg_color=self.bottom_sheet.md_bg_color,
                ),
                theme_bg_color = "Custom",
                md_bg_color = self.bottom_sheet.md_bg_color,
            )
        listItem.height = 52
        self.bottom_sheet.link_list.add_widget(listItem)

        #Price
        listItem = MDListItem(
                MDListItemHeadlineText(
                    text = "Цена за час",
                    theme_text_color = "Custom",
                    text_color = "#AAAAAA",
                    font_style = "Title",
                    role = "medium",
                    font_size = 12,
                ),
                MDListItemSupportingText(
                    text = str(dataParking["price"]),
                    font_style = "Title",
                    role = "medium",
                    font_size = 14,
                ),
                theme_bg_color = "Custom",
                md_bg_color = self.bottom_sheet.md_bg_color,
            )
        listItem.height = 52
        self.bottom_sheet.link_list.add_widget(listItem)

        #Places
        listItem = MDListItem(
                MDListItemHeadlineText(
                    text = "Мест всего",
                    theme_text_color = "Custom",
                    text_color = "#AAAAAA",
                    font_style = "Title",
                    role = "medium",
                    font_size = 12,
                ),
                MDListItemSupportingText(
                    text = str(dataParking["places"]),
                    font_style = "Title",
                    role = "medium",
                    font_size = 14,
                ),
                theme_bg_color = "Custom",
                md_bg_color = self.bottom_sheet.md_bg_color,
            )
        listItem.height = 52
        self.bottom_sheet.link_list.add_widget(listItem)

        #Places disabilities
        listItem = MDListItem(
                MDListItemHeadlineText(
                    text = "Мест для инвалидов",
                    theme_text_color = "Custom",
                    text_color = "#AAAAAA",
                    font_style = "Title",
                    role = "medium",
                    font_size = 12,
                ),
                MDListItemSupportingText(
                    text = str(dataParking["places_with_disabilities"]),
                    font_style = "Title",
                    role = "medium",
                    font_size = 14,
                ),
                theme_bg_color = "Custom",
                md_bg_color = self.bottom_sheet.md_bg_color,
            )
        listItem.height = 52
        self.bottom_sheet.link_list.add_widget(listItem)

        #Additional
        listItem = MDListItem(
                MDListItemHeadlineText(
                    text = "Дополнительно",
                    theme_text_color = "Custom",
                    text_color = "#AAAAAA",
                    font_style = "Title",
                    role = "medium",
                    font_size = 12,
                ),
                MDListItemSupportingText(
                    text = "Пн-Вс: 00.00-24.00",
                    font_style = "Title",
                    role = "medium",
                    font_size = 14,
                ),
                theme_bg_color = "Custom",
                md_bg_color = self.bottom_sheet.md_bg_color,
            )
        listItem.height = 52
        self.bottom_sheet.link_list.add_widget(listItem)
        if self.bottom_sheet:
            self.bottom_sheet.set_state("toggle")

        

