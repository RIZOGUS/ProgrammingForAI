# Water Jug Problem - DFS Implementation

A Python implementation of the classic Water Jug Problem using **Depth-First Search (DFS)** algorithm.

## 📋 Problem Description

Given two jugs with different capacities and a target amount of water, find a sequence of operations to measure exactly the target amount.

### Available Operations

1. **Fill Jug 1** - Fill jug 1 to its full capacity
2. **Fill Jug 2** - Fill jug 2 to its full capacity
3. **Empty Jug 1** - Pour out all water from jug 1
4. **Empty Jug 2** - Pour out all water from jug 2
5. **Pour Jug 1 → Jug 2** - Transfer water from jug 1 to jug 2
6. **Pour Jug 2 → Jug 1** - Transfer water from jug 2 to jug 1

## 🚀 Features

- ✅ **DFS Algorithm** - Uses depth-first search to find solution
- ✅ **Step-by-Step Output** - Prints each rule applied
- ✅ **State Tracking** - Tracks visited states to avoid cycles
- ✅ **Multiple Examples** - Includes 3 different problem instances
- ✅ **Clear Visualization** - Easy-to-read output format

## 📦 Requirements

```bash
Python 3.x (No external dependencies required!)
```

## 🎯 Quick Start

1. **Navigate to Task-3 folder**:

   ```bash
   cd d:\Tasks\PFAI\Task-3
   ```

2. **Run the program**:

   ```bash
   python water_jug_dfs.py
   ```

## 📊 Example Output

```
======================================================================
Water Jug Problem - DFS Solution
======================================================================
Jug 1 Capacity: 4 liters
Jug 2 Capacity: 3 liters
Target Amount: 2 liters
======================================================================

✓ Solution Found! (6 steps)

Initial State: (0, 0)
----------------------------------------------------------------------
Step 1: Fill Jug 1: (0, 0) -> (4, 0)
Step 2: Pour Jug 1 -> Jug 2: (4, 0) -> (1, 3)
Step 3: Empty Jug 2: (1, 3) -> (1, 0)
Step 4: Pour Jug 1 -> Jug 2: (1, 0) -> (0, 1)
Step 5: Fill Jug 1: (0, 1) -> (4, 1)
Step 6: Pour Jug 1 -> Jug 2: (4, 1) -> (2, 3)
----------------------------------------------------------------------
Final State: (2, 3)

✓ Target of 2 liters achieved!
======================================================================
```

## 🔧 How It Works

### Algorithm: Depth-First Search (DFS)

1. **Start** with both jugs empty: `(0, 0)`
2. **Generate** all possible next states using the 6 operations
3. **Check** if any state achieves the target
4. **Recursively explore** unvisited states (DFS)
5. **Track** visited states to avoid infinite loops
6. **Return** the solution path when target is found

### State Representation

Each state is represented as a tuple: `(jug1_amount, jug2_amount)`

Example: `(4, 3)` means Jug 1 has 4 liters and Jug 2 has 3 liters

## 📝 Code Structure

```
water_jug_dfs.py
├── WaterJugDFS class
│   ├── __init__()          # Initialize problem parameters
│   ├── is_goal()           # Check if target reached
│   ├── get_next_states()   # Generate possible next states
│   ├── dfs()               # DFS algorithm implementation
│   └── solve()             # Main solver with output
└── main()                  # Example demonstrations
```

## 🎓 Learning Objectives

This implementation helps you understand:

- **Graph Search Algorithms** - DFS traversal
- **State Space Search** - Representing problems as states
- **Backtracking** - Exploring and backtracking in search
- **Problem Solving** - Breaking down complex problems
- **Python Programming** - Classes, recursion, and data structures

## 🔄 Customization

You can easily create your own water jug problems:

```python
# Create a custom problem
wj = WaterJugDFS(
    jug1_capacity=7,    # Jug 1 can hold 7 liters
    jug2_capacity=5,    # Jug 2 can hold 5 liters
    target=6            # We want to measure 6 liters
)

# Solve it
wj.solve()
```

## 📚 Included Examples

1. **Classic Problem**: 4L and 3L jugs, target = 2L
2. **Standard Problem**: 5L and 3L jugs, target = 4L
3. **Custom Problem**: 7L and 5L jugs, target = 6L

## 💡 Key Concepts

- **DFS (Depth-First Search)**: Explores as far as possible along each branch before backtracking
- **State Space**: All possible configurations of the jugs
- **Visited Set**: Prevents revisiting states and infinite loops
- **Path Tracking**: Records the sequence of operations to reach the goal

## 🎯 Complexity

- **Time Complexity**: O(m × n) where m and n are jug capacities
- **Space Complexity**: O(m × n) for visited states

## 🔍 Understanding the Rules

Each operation transforms the current state:

| Rule | Operation | Example |
|------|-----------|---------|
| 1 | Fill Jug 1 | `(0, 2) → (4, 2)` |
| 2 | Fill Jug 2 | `(2, 0) → (2, 3)` |
| 3 | Empty Jug 1 | `(4, 2) → (0, 2)` |
| 4 | Empty Jug 2 | `(2, 3) → (2, 0)` |
| 5 | Pour 1→2 | `(4, 0) → (1, 3)` |
| 6 | Pour 2→1 | `(0, 3) → (3, 0)` |

## 🚦 Next Steps

After understanding this implementation, you can:

1. Implement **BFS (Breadth-First Search)** for comparison
2. Add **A* Search** for optimal solutions
3. Visualize the search tree
4. Compare different search strategies
5. Extend to 3+ jugs

---