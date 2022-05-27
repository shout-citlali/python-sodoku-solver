class Solver:
  def __init__(self, cells):
    self.cells = cells

  def determine_cell_possibilities(self):
    for cell in self.cells:
      candidates = list(range(1, 10))
      for association in cell.get_unique_associations():
        if association.number is not None:
          if association.number in candidates:
            candidates.remove(association.number)
      cell.possibilities = candidates

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

  def solution_alpha(self):
    while True:
      prelim_empty_cells = self.get_empty_cell_count()
      self.determine_cell_possibilities()
      self.assign_cells_having_single_possibility()
      has_changed = prelim_empty_cells > self.get_empty_cell_count()
      if not has_changed or self.get_empty_cell_count() == 0:
          break

  # def determine_single_option_in_row_for_number(self):
  #   for row_seed in range(0, 9): # Loop through each row
  #     for num in range(1, 10):     # Loop through each number 1-9
  #       options = []
  #       for row_iterator in range(row_seed * 9, row_seed * 9 + 8): # Loop through each cell in the row testing for the number
  #         if num in self.cells[row_iterator].possibilities:
  #           options.append(self.cells[row_iterator])
  #       if len(options) == 1:
  #         options[0].number = num

  # def solution_beta(self):
  #   self.determine_cell_possibilities()
  #   self.determine_single_option_in_row_for_number()

  def solve(self):
    self.solution_alpha()
    # if self.get_empty_cell_count() > 0:
    #   self.solution_beta()
