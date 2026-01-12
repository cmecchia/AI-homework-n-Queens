from constraint import Problem, AllDifferentConstraint
import time

def run_queens_csp(n_size):
    timer_start = time.perf_counter()
    engine = Problem()
    
    # Variabili: ogni colonna (0...N-1)
    # Dominio: ogni riga possibile (0...N-1)
    cols = range(n_size)
    engine.addVariables(cols, range(n_size))
    
    # Vincolo 1: Ogni regina su una riga diversa
    engine.addConstraint(AllDifferentConstraint())
    
    # Vincolo 2: Diagonali
    # r1, r2 sono i valori (righe), c1, c2 sono gli indici (colonne)
    def diagonal_check(r1, r2, c1, c2):
        return abs(r1 - r2) != abs(c1 - c2)

    for c1 in range(n_size):
        for c2 in range(c1 + 1, n_size):
            # Usiamo parametri di default nella lambda per catturare c1 e c2 correnti
            engine.addConstraint(
                lambda r1, r2, col1=c1, col2=c2: diagonal_check(r1, r2, col1, col2), 
                (c1, c2)
            )
    
    res = engine.getSolution()
    return {
        "solution": res,
        "exec_time": time.perf_counter() - timer_start
    }
