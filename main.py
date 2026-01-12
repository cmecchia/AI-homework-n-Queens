import matplotlib.pyplot as plt
from engine_queens import QueensBoard
import astar_engine as astar
from csp_logic import run_queens_csp

def start_experiment():
    
    test_sizes = [4, 6, 8, 10, 12, 13, 14]
    data_points = {"astar": [], "csp": []}

    print(f"{'N':<5} | {'A* (sec)':<10} | {'CSP (sec)':<10} | {'Nodes Exp':<10} | {'Mem Peak':<8}")
    print("-" * 55)

    for n in test_sizes:
        # A* execution
        env = QueensBoard(n)
        res_a = astar.execute_astar(env, astar.h_remaining_queens)
        
        # CSP execution
        res_c = run_queens_csp(n)
        
        data_points["astar"].append(res_a)
        data_points["csp"].append(res_c)

        print(f"{n:<5} | {res_a['duration']:<10.4f} | {res_c['exec_time']:<10.4f} | {res_a['nodes_expanded']:<10} | {res_a['memory_peak']:<8}")

    generate_plots(test_sizes, data_points)

def generate_plots(sizes, data):
    plt.style.use('ggplot')
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # Plot 1
    axes[0].plot(sizes, [d['duration'] for d in data["astar"]], marker='o', linewidth=2, label='A* Search')
    axes[0].plot(sizes, [d['exec_time'] for d in data["csp"]], marker='s', linewidth=2, label='CSP Solver')
    axes[0].set_yscale('log')
    axes[0].set_title("Execution Time Comparison (Log Scale)")
    axes[0].set_xlabel("Problem Size (N)")
    axes[0].set_ylabel("Seconds")
    axes[0].legend()
    axes[0].grid(True, which="both", ls="-", alpha=0.5)

    # Plot 2
    axes[1].bar(sizes, [d['memory_peak'] for d in data["astar"]], color='skyblue', alpha=0.8)
    axes[1].set_title("A* Memory Usage (Peak Nodes)")
    axes[1].set_xlabel("Problem Size (N)")
    axes[1].set_ylabel("Max Nodes in Memory")

    plt.tight_layout()
    plt.savefig('analysis_output.png')

if __name__ == "__main__":
    start_experiment()
