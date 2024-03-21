from kivy_garden.mapview import MapMarkerPopup
from MarkerPopupMenu import MarkerPopupMenu

class ParkMarker(MarkerPopupMenu):
    source = "marker.png"
    marketData = []

    def on_release(self):
        menu = MarkerPopupMenu(self.marketData)
        menu.open()