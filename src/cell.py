class Cell:
    def __init__(self, row_id, column_id):
        self.row_id = row_id
        self.column_id = column_id
        self.north = None
        self.south = None
        self.east = None
        self.west = None