from constraint import Problem, AllDifferentConstraint
import time

def run_queens_csp(n_size):
    timer_start = time.perf_counter()
    engine = Problem()
    
    # Variables: each column (0...N-1)
    # Domain: each possible row (0...N-1)
    cols = range(n_size)
    engine.addVariables(cols, range(n_size))
    
    # first constraint: each queen on a different row 
    engine.addConstraint(AllDifferentConstraint())
    
    # second constraint on the diagonals
    # r1, r2 are rows, c1, c2 are columns
    def diagonal_check(r1, r2, c1, c2):
        return abs(r1 - r2) != abs(c1 - c2)

    for c1 in range(n_size):
        for c2 in range(c1 + 1, n_size):
            engine.addConstraint(
                lambda r1, r2, col1=c1, col2=c2: diagonal_check(r1, r2, col1, col2), 
                (c1, c2)
            )
    
    res = engine.getSolution()
    return {
        "solution": res,
        "exec_time": time.perf_counter() - timer_start
    }
