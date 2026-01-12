# AI Homework

## 1. Introduction
This project was developed for the **Artificial Intelligence** course (Autumn Term, AY 2025–26) at Sapienza University of Rome. 
The core objective is to solve the classic **n-Queens problem**—placing $n$ queens on an $n \times n$ chessboard such that no two queens threaten each other—using two distinct AI techniques. The project includes the entire pipeline: modeling, implementation, and experimental comparison.

## 2. Overview of Techniques Used
To solve the problem, two different approaches were implemented and compared:

*   **A* Search Algorithm**: A custom implementation of the A* algorithm. The search includes:
    *   **Duplicate Elimination**: Using an explored set to avoid redundant states.
    *   **No Reopening**: Ensuring that states are not re-processed once expanded.
    *   **Heuristic Search**: Utilizing an admissible "Remaining Queens" heuristic.
*   **Reduction to CSP**: The problem is modeled as a Constraint Satisfaction Problem (CSP).
    *   **Variables**: One variable per column.
    *   **Constraints**: All-different rows and non-attacking diagonals.
    *   **Solver**: Implementation using the `python-constraint` library.

## 3. Project Structure
The repository is organized as follows:
- `engine_queens.py`: The environment modeling (state representation, transition rules, and goal test).
- `astar_engine.py`: The core search logic for the A* algorithm and heuristic definitions.
- `csp_logic.py`: The reduction logic and integration with the CSP solver.
- `main.py`: The experiment runner that executes both algorithms, collects data, and generates plots.
- `requirements.txt`: A list of the Python dependencies required to run the project.

## 4. Installation
To set up the environment and install all necessary dependencies, run the following command in your terminal:

```bash
pip install -r requirements.txt
```

## 5. Results and Experiments
To run the experiments and generate the performance analysis, execute:

```bash
python main.py
```

### What to expect:
*   **Terminal Output**: A detailed table comparing A* and CSP performance across different values of $n$ (from 4 up to 14). It includes:
    *   Execution time (seconds).
    *   Number of nodes expanded and generated (A*).
    *   Memory peak (maximum nodes held in memory simultaneously).
    *   Average branching factor.
*   **Data Visualization**: 
    *   **Execution Time Comparison**: A chart (logarithmic scale) showing how both methods scale as the board size increases.
    *   **Memory Usage Chart**: A bar chart representing the peak number of nodes stored in memory during the A* search.