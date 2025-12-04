# N-Queens Problem - Dynamic Backtracking with Pygame GUI

A beautiful interactive visualization of the classic N-Queens problem using dynamic backtracking algorithm with Pygame GUI.

## 📋 Problem Description

- **Chessboard Pattern** - Classic light/dark square pattern
- **Queen Pieces** - Beautiful red queens with white crowns
- **Info Panel** - Shows current solution and controls
- **Smooth Animation** - Watch backtracking in action

### Color Scheme

- Light Squares: Cream (#F0D9B5)
- Dark Squares: Brown (#B58863)
- Queens: Crimson Red (#DC143C)
- Info Panel: Lavender (#E6E6FA)

## 🧠 Algorithm: Dynamic Backtracking

### How It Works

1. **Place Queen**: Try placing a queen in each column of the current row
2. **Check Safety**: Verify no conflicts with previously placed queens
3. **Recurse**: Move to next row if placement is safe
4. **Backtrack**: If no safe placement, remove queen and try next column
5. **Solution Found**: When all N queens are placed successfully

### Time Complexity

- **Worst Case**: O(N!)
- **Average Case**: Much better due to pruning

### Space Complexity

- **O(N)** for the recursion stack

## 📊 Example Solutions

### 4-Queens (2 solutions)

```
Solution 1:    Solution 2:
. Q . .        . . Q .
. . . Q        Q . . .
Q . . .        . . . Q
. . Q .        . Q . .
```

### 8-Queens (92 solutions)

The classic problem has 92 distinct solutions!

## 🔧 Code Structure

```
n_queens.py
├── NQueens class
│   ├── __init__()        # Initialize board
│   ├── is_safe()         # Check if placement is valid
│   ├── solve()           # Find first solution
│   └── solve_all()       # Find all solutions
│
└── NQueensGUI class
    ├── __init__()        # Setup Pygame window
    ├── draw_board()      # Render chessboard
    ├── draw_info_panel() # Display information
    ├── solve_with_animation() # Animated solving
    └── run()             # Main game loop
```

## 🎓 Learning Objectives

This implementation teaches:

- **Backtracking Algorithms** - Classic problem-solving technique
- **Recursion** - Elegant recursive solution
- **Constraint Satisfaction** - Checking multiple constraints
- **Pygame Development** - GUI programming with Pygame
- **Algorithm Visualization** - Making algorithms visual and interactive

## 💡 Understanding the Safety Check

A queen is safe if no other queen can attack it:

```python
def is_safe(self, row, col):
    for i in range(row):
        # Same column check
        if self.board[i] == col:
            return False
        
        # Diagonal check
        if abs(self.board[i] - col) == abs(i - row):
            return False
    
    return True
```

## 📈 Number of Solutions by N

| N | Solutions |
|---|-----------|
| 4 | 2 |
| 5 | 10 |
| 6 | 4 |
| 7 | 40 |
| 8 | 92 |
| 9 | 352 |
| 10 | 724 |

## 🎯 Customization

### Adjust Animation Speed

```python
gui = NQueensGUI(n)
gui.animation_speed = 0.3  # Faster
gui.animation_speed = 1.0  # Slower
gui.run()
```

### Change Colors

```python
gui.QUEEN_COLOR = (0, 128, 255)  # Blue queens
gui.LIGHT_SQUARE = (255, 255, 255)  # White squares
```

## 🔍 Algorithm Variants

The code includes two solving methods:

1. **solve()** - Finds first solution only (faster)
2. **solve_all()** - Finds all possible solutions (complete)

## 🚦 Performance Tips

- **Smaller N (4-8)**: Very fast, great for learning
- **Medium N (9-12)**: Noticeable solving time
- **Large N (13+)**: May take significant time for all solutions

## 🎬 What to Expect

1. **Launch**: Beautiful chessboard appears
2. **Press SPACE**: Watch algorithm place queens
3. **See Backtracking**: Queens appear and disappear as algorithm searches
4. **Solution Found**: Final configuration displayed
5. **Navigate**: Use arrow keys to see other solutions

## 🔄 Next Steps

After mastering this, try:

1. Implement **iterative solution** (without recursion)
2. Add **solution counter** during solving
3. Implement **N-Queens completion** (given partial board)
4. Add **heuristics** for faster solving
5. Create **3D visualization** for larger boards

---

**Enjoy solving the N-Queens Problem! 👑**
