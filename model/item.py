class Item:
    def __init__(self, acad_item) -> None:
        self._coordinates = acad_item.Coordinates
        self._area = acad_item.Area

    @property
    def coordinates(self):
        return self._coordinates

    @property
    def area(self):
        return self._area
