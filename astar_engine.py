import heapq
import time
from dataclasses import dataclass, field
from typing import Any, Optional

@dataclass(order=True)
class SearchNode:
    priority: int
    h_val: int = field(compare=False)
    state: Any = field(compare=False)
    parent: Optional['SearchNode'] = field(default=None, compare=False)
    g_val: int = field(default=0, compare=False)

def execute_astar(environment, heuristic_fn):
    start_ts = time.perf_counter()
    init_state = environment.get_initial_config()
    
    stats = {
        "generated": 1,
        "expanded": 0,
        "max_mem": 0,
        "branching": []
    }

    start_h = heuristic_fn(init_state, environment.size)
    root = SearchNode(priority=start_h, h_val=start_h, state=init_state)
    
    open_list = [root]
    closed_set = set() # Per Duplicate Elimination
    # frontier_tracker tiene traccia del miglior costo f trovato per stati in Open List
    frontier_tracker = {init_state: root.priority}

    while open_list:
        # Calcolo memoria: Open List + Closed Set
        stats["max_mem"] = max(stats["max_mem"], len(open_list) + len(closed_set))
        
        current_node = heapq.heappop(open_list)
        curr_state = current_node.state

        # No Reopening: Se lo stato è già stato espanso, lo saltiamo
        if curr_state in closed_set:
            continue
            
        if environment.is_goal_reached(curr_state):
            return {
                "status": "success",
                "duration": time.perf_counter() - start_ts,
                "nodes_expanded": stats["expanded"],
                "nodes_generated": stats["generated"],
                "memory_peak": stats["max_mem"],
                "avg_b": sum(stats["branching"])/len(stats["branching"]) if stats["branching"] else 0
            }

        closed_set.add(curr_state)
        stats["expanded"] += 1
        
        possible_moves = environment.find_legal_placements(curr_state)
        stats["branching"].append(len(possible_moves))

        for move in possible_moves:
            child_state = environment.apply_placement(curr_state, move)
            stats["generated"] += 1

            # Duplicate Elimination: se è già chiuso, non riaprire
            if child_state in closed_set:
                continue

            new_g = current_node.g_val + 1
            new_h = heuristic_fn(child_state, environment.size)
            f_total = new_g + new_h
            child_node = SearchNode(priority=f_total, h_val=new_h, state=child_state, parent=current_node, g_val=new_g)

            # Aggiungi alla frontiera solo se è un nuovo stato o se il nuovo percorso è migliore
            if child_state not in frontier_tracker or f_total < frontier_tracker[child_state]:
                heapq.heappush(open_list, child_node)
                frontier_tracker[child_state] = f_total

    return {"status": "failure", "duration": time.perf_counter() - start_ts}

def h_remaining_queens(state, n):
    """Euristica: numero di regine ancora da piazzare."""
    return n - len(state)
