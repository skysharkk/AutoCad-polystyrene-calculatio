class Item:
    def __init__(self, acad_item) -> None:
        self._coordinates = acad_item.Coordinates

    @property
    def coordinates(self):
        return self._coordinates
