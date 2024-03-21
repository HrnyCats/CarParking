from kivymd.uix.bottomsheet import MDListBottomSheet

class MarkerPopupMenu(MDListBottomSheet):
    def __init__(self, parkData):
        super().__init__()
        headers = "1,2,3"
        headers = headers.split(',')

        for i in range(len(headers)):
            attributeName = headers[i]
            attributeValue = parkData[i]
            setattr(self,attributeName,attributeValue)
