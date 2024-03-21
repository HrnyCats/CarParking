from kivymd.uix.bottomsheet import MDListBottomSheet

class MarkerPopupMenu(MDListBottomSheet):
    def __init__(self, parkData):
        super().__init__()

        headers = "id_car_parking,lon,lat,address,price,type_car_park,places_with_disabilities,schedule_time_start,schedule_time_end,schedule_weekday_start,schedule_weekday_end"
        headers = headers.split(',')
        
        for i in range(len(headers)):
            attributeName = headers[i]
            attributeValue = parkData[i]
            #setattr(self,attributeName,attributeValue)
