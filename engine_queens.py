class QueensBoard:
    """Modellazione del problema delle N-Regine come spazio degli stati."""
    def __init__(self, size):
        self.size = size

    def get_initial_config(self):
        # Stato: tupla di interi. L'indice rappresenta la colonna, il valore la riga.
        return () 

    def is_goal_reached(self, config):
        return len(config) == self.size

    def find_legal_placements(self, config):
        if len(config) >= self.size:
            return []
        
        current_col = len(config)
        candidates = []
        for row in range(self.size):
            if self._is_safe(config, current_col, row):
                candidates.append(row)
        return candidates

    def _is_safe(self, current_config, new_col, new_row):
        for col, row in enumerate(current_config):
            # Controllo riga e diagonali
            if row == new_row or abs(row - new_row) == abs(col - new_col):
                return False
        return True

    def apply_placement(self, config, row):
        return config + (row,)
