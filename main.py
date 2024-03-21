from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# Map Libs
from kivy_garden.mapview import MapView, MapMarker, MapMarkerPopup
from kivy_garden.mapview.clustered_marker_layer import ClusteredMarkerLayer  


from kivy.core.window import Window
from random import randint, random

Window.size = (800,600)
Window.title = "CarParks"

class MainApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = Label(text="Живем, живем")

    def btnPressed(self, *args):
        self.label.color = (randint(0,255)/255, randint(0,255)/255, randint(0,255)/255, 1)

    def build(self):
        box = BoxLayout()
        btn = Button(text="press")
        btn.bind(on_press = self.btnPressed)
        box.add_widget(self.label) 
        box.add_widget(btn)

        # Map
        layer = ClusteredMarkerLayer()
        for i in range(20):
            lat = random()*0.1 + 53.3
            lon = random()*0.1 + 58.9
            m = MapMarkerPopup(lat=lat,lon=lon)
             #m.add_widget(box)
            #layer.add_marker(m)
        m = MapMarkerPopup(lat=53.414417,lon=58.920551)
        m.add_widget(box)
        m2 = MapMarker(lat = 53.414417, lon=58.920551)
        map = MapView(zoom = 10,  lat= 53.413417, lon=58.920551)
        map.add_marker(m)
         #map.add_widget(layer)

        return map

def print_hi(name):
    print(f'Hi, {name}') 


if __name__ == '__main__':
    MainApp().run()


