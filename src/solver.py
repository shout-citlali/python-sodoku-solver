import math

class Solver:
  def __init__(self, cells):
    self.cells = cells


  def get_total_possibilities_count(self):
    count = 0
    for cell in self.cells:
      count += len(cell.possibilities)
    return count


  def get_row_list_by_seed(self, seed):
    row_cells = list(map(lambda c: self.cells[c], range(seed * 9, seed * 9 + 9)))
    return row_cells


  def get_col_list_by_seed(self, seed):
    col_cells = list(map(lambda c: self.cells[c], range(seed, 81, 9)))
    return col_cells


  def get_grid_list_by_seed(self, seed):
    grid_root = (seed % 3 * 3) + (math.floor(seed / 3) * 27) # Get top left of grid
    grid_group = list(map(lambda r: list(range(r, r + 3)), range(grid_root, grid_root + 27, 9))) # Get remainder of grid numbers as list of lists
    grid_list = [item for sublist in grid_group for item in sublist] # Flatten the list of lists
    grid_cells = list(map(lambda c: self.cells[c], grid_list))
    return grid_cells


  def eliminate_skewered_possibilities(self):
    for grid_seed in range(0, 9): # Loop through each grid
      grid_cells = self.get_grid_list_by_seed(grid_seed)
      for num in range(1, 10): # Loop through each number
        options = []
        for cell in grid_cells: # Loop through each cell id in grid
          if num in cell.possibilities: # Determine list of cells in grid having the given number
            options.append(cell)
        possibility_rows = []
        possibility_cols = []
        for option in options: # Loop over resulting Cell options
          if option.row_id not in possibility_rows: # Compile list of unique rows having the number
            possibility_rows.append(option.row_id)
          if option.column_id not in possibility_cols: # Compile list of unique cols having the number
            possibility_cols.append(option.column_id)
        if len(possibility_rows) == 1: # If there is only 1 row in the grid with cells having the number as a possibility
          for row_cell in self.get_row_list_by_seed(possibility_rows[0]):
            if row_cell.grid_id != grid_seed and num in row_cell.possibilities:
              row_cell.possibilities.remove(num)
        if len(possibility_cols) == 1:  # If there is only 1 col in the grid with cells having the number as a possibility
          for col_cell in self.get_col_list_by_seed(possibility_cols[0]):
            if col_cell.grid_id != grid_seed and num in col_cell.possibilities:
              col_cell.possibilities.remove(num)


  def determine_cell_possibilities(self):
    for cell in self.cells:
      if cell.number is not None:
        cell.possibilities = []
      else:
        candidates = list(range(1, 10))
        for association in cell.get_unique_associations():
          if association.number is not None:
            if association.number in candidates:
              candidates.remove(association.number)
        cell.possibilities = candidates
    while True:
      prelim_possibilities_count = self.get_total_possibilities_count()
      print(prelim_possibilities_count)
      self.eliminate_skewered_possibilities()
      has_changed = prelim_possibilities_count > self.get_total_possibilities_count()
      if not has_changed or prelim_possibilities_count == 0:
          break



  def assign_cells_having_single_possibility(self):
    for cell in self.cells:
      if len(cell.possibilities) == 1:
        cell.number = cell.possibilities[0]


  def get_empty_cell_count(self):
    empty = 0
    for cell in self.cells:
      if cell.number is None:
        empty += 1
    return empty





  def determine_single_option_in_row_for_number(self):
    for row_seed in range(0, 9): # Loop through each row
      for num in range(1, 10):     # Loop through each number 1-9
        options = []
        print()
        for cell in self.get_row_list_by_seed(row_seed): # Loop through each cell in the row testing for the number
          if num in cell.possibilities:
            options.append(cell)
        if len(options) == 1:
          options[0].number = num


  def determine_single_option_in_column_for_number(self):
    for col_seed in range(0, 9): # Loop through each column
      for num in range(1, 10):     # Loop through each number 1-9
        options = []
        for cell in self.get_col_list_by_seed(col_seed): # Loop through each cell in the column testing for the number
          if num in cell.possibilities:
            options.append(cell)
        if len(options) == 1:
          options[0].number = num


  def determine_single_option_in_grid_for_number(self):
    for grid_seed in range(0, 9): # Loop through each grid
      for num in range(1, 10):     # Loop through each number 1-9
        options = []
        for cell in self.get_grid_list_by_seed(grid_seed): # Loop through each cell in the grid testing for the number
          if num in cell.possibilities:
            options.append(cell)
        if len(options) == 1:
          options[0].number = num


  def solve(self):
    while True:
      prelim_empty_cells = self.get_empty_cell_count()
      self.determine_cell_possibilities()
      self.determine_single_option_in_row_for_number()
      self.determine_cell_possibilities()
      self.determine_single_option_in_column_for_number()
      self.determine_cell_possibilities()
      self.determine_single_option_in_grid_for_number()
      self.determine_cell_possibilities()
      self.assign_cells_having_single_possibility()
      has_changed = prelim_empty_cells > self.get_empty_cell_count()
      if not has_changed or self.get_empty_cell_count() == 0:
          break

    return self.get_empty_cell_count() == 0

      
