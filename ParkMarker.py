from kivy_garden.mapview import MapMarkerPopup
from MarkerPopupMenu import MarkerPopupMenu


class ParkMarker(MapMarkerPopup):
    source = "marker.png"
    parkData = []

    def on_release(self):
        MarkerPopupMenu.ShowParkData(self.parkData)
