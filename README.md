# AI Algorithms Repository

**Owner:** Soumit Das  
**Contact:** [1803063soumit@gmail.com](mailto:1803063soumit@gmail.com)

Welcome to the AI Algorithms Repository! This repository contains various search algorithms implemented in Python. These algorithms are fundamental to the field of Artificial Intelligence and are widely used in problem-solving and pathfinding scenarios.

## Table of Contents

- [Introduction](#introduction)
- [Algorithms Included](#algorithms-included)
- [Installation](#installation)
- [Usage](#usage)
- [Algorithm Groups](#algorithm-groups)
- [Complexity Comparison](#complexity-comparison)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This repository contains a collection of AI search algorithms grouped into three main categories: Uninformed Search Algorithms, Informed Search Algorithms, and Local Search Algorithms. Each algorithm is implemented in its own Python file, making it easy to study and understand the specifics of each method.

### Uninformed Search Algorithms

1. **Breadth-First Search (`bfs.py`)**: Explores all nodes at the present depth before moving on to nodes at the next depth level.
2. **Depth-First Search (`dfs.py`)**: Explores as far as possible along each branch before backtracking.
3. **Depth-Limited Search (`dls.py`)**: A DFS with a predetermined limit to avoid infinite paths.
4. **Iterative Deepening Search (`ids.py`)**: Repeatedly applies DLS with increasing depth limits.
5. **Uniform Cost Search (`unicost.py`)**: Expands the least cost node first.

### Informed Search Algorithms

1. **A* Search (`astar.py`)**: Combines the strengths of BFS and Dijkstra's algorithm to find the shortest path efficiently.
2. **Beam Search (`beamsearch.py`)**: A heuristic search algorithm that explores a graph by expanding the most promising nodes.
3. **Greedy Best-First Search (`gbfs.py`)**: Selects the path that appears to be the best at each step.
4. **Bidirectional Search (`bidirectional.py`)**: Runs two simultaneous searches—one from the start and one from the goal—until they meet.

### Local Search Algorithms

1. **Hill Climbing (`hill_climbing.py`)**: Iteratively makes small changes to the solution to find the best result.
2. **Simulated Annealing (`Simulated Annealing.py`)**: Probabilistic technique for approximating the global optimum of a given function.

### Complexity Comparison

| Algorithm                  | Time Complexity        | Space Complexity       | Optimal | Complete |
|----------------------------|------------------------|------------------------|---------|----------|
| Breadth-First Search (BFS) | O(b^d)                 | O(b^d)                 | Yes     | Yes      |
| Depth-First Search (DFS)   | O(b^m)                 | O(bm)                  | No      | No       |
| Depth-Limited Search (DLS) | O(b^l)                 | O(bl)                  | No      | No       |
| Iterative Deepening Search (IDS) | O(b^d)          | O(bd)                  | Yes     | Yes      |
| Uniform Cost Search        | O(b^(C*/ε))            | O(b^(C*/ε))            | Yes     | Yes      |
| A* Search                  | O(b^d)                 | O(b^d)                 | Yes     | Yes      |
| Beam Search                | O(bm)                  | O(bm)                  | No      | No       |
| Greedy Best-First Search   | O(b^m)                 | O(b^m)                 | No      | No       |
| Bidirectional Search       | O(b^(d/2))             | O(b^(d/2))             | Yes     | Yes      |
| Hill Climbing              | O(1)                   | O(1)                   | No      | No       |
| Simulated Annealing        | O(1)                   | O(1)                   | No      | No       |

- **b**: branching factor
- **d**: depth of the shallowest solution
- **m**: maximum depth of the search tree
- **C***: cost of the optimal solution
- **ε**: minimum cost step (for Uniform Cost Search)

### Comparison

- **Breadth-First Search (BFS)** is complete and optimal but can consume a lot of memory for large depths.
- **Depth-First Search (DFS)** is more memory efficient but neither complete nor optimal.
- **Iterative Deepening Search (IDS)** combines the benefits of BFS and DFS, providing completeness and optimality with reasonable memory usage.
- **Uniform Cost Search** guarantees finding the least cost path, but can be slow if the cost variance is high.
- **A* Search** is efficient with a good heuristic, providing optimal solutions quickly.
- **Beam Search** is less memory intensive but can miss the optimal solution.
- **Greedy Best-First Search** is fast but can get stuck in local optima.
- **Bidirectional Search** is efficient for certain problem spaces but requires a well-defined goal state.
- **Hill Climbing** and **Simulated Annealing** are suitable for optimization problems but don't guarantee finding the global optimum.

## Installation

To use the algorithms in this repository, you need to have Python installed on your machine. Clone this repository using the following command:

```bash
git clone https://github.com/soumit1803063/AI.git
```

## Usage

Each Python file can be run independently. For example, to run the A* Search algorithm, use the following command:

```bash
python astar.py
```

You can modify the input and parameters within each script to suit your specific needs.

### Required Packages

The algorithms in this repository make use of the following Python packages:

```python
from math import inf, e
from random import randint
from queue import PriorityQueue
from collections import deque
```

Ensure you have these packages available in your Python environment. Most of these are standard libraries that come with Python. If you are missing any, you can install them using pip.
