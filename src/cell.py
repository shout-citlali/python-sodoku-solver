class Cell:
    def __init__(self, row_id, column_id):
        self.id = row_id * 9 + column_id
        self.row_id = row_id
        self.column_id = column_id
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.column_associations = []
        self.row_associations = []
        self.grid_associations = []
        self.number = None
        self.user_defined = False
        self.possibilities = []

    def get_unique_associations(self):
        unique_associations = self.column_associations + self.row_associations + self.grid_associations
        return list(set(unique_associations))

    def has_conflicts(self):
        conflict_count = 0
        for assoc in self.get_unique_associations():
            if self.number != None and self.number == assoc.number:
                conflict_count += 1
            
        return conflict_count


