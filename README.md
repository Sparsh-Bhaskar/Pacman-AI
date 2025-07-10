# Pac-Man AI Project 🎮👻

In this game, **you control Pac-Man**, who must navigate a maze, eat all the dots, and avoid being caught by **AI-controlled ghosts**. Each ghost uses a different classic pathfinding algorithm to intelligently chase Pac-Man through the maze.

---

## 🧩 Key Features

- 2D grid-based maze with walls and collectible dots
- Pac-Man moves using arrow keys (Up, Down, Left, Right)
- Ghosts can't pass through walls and use AI to chase Pac-Man

---

## 🧠 AI Pathfinding Algorithms Used

- **BFS (Breadth-First Search)**: Explores all possible moves step-by-step to find the shortest path  
- **DFS (Depth-First Search)**: Explores a single path as far as possible before backtracking  
- **A\***: Uses a heuristic to find the shortest path efficiently  
- **Hill Climbing**: Always moves toward the direction closest to Pac-Man, but may get stuck  
- **DFS-ID**: Repeated DFS with increasing depth limits, using minimal memory  

🔄 You can switch between these ghost AI algorithms in real time by pressing keys `1` to `5`.

---

## 🎮 Game Flow

1. Launch the game and control Pac-Man using arrow keys  
2. Ghosts calculate a path to Pac-Man using the selected algorithm  
3. Pac-Man eats dots while avoiding ghosts  
4. Game ends if:
   - A ghost catches Pac-Man (**Game Over**)  
   - All dots are eaten (**You Win!**)  

---

## ▶️ How to Play

```bash
1. Install Python and Pygame
2. Open terminal in this folder
3. Run: python main.py
4. Move Pac-Man with arrow keys
5. Press 1-5 to switch ghost AI
```

---

## 🛠 Technology Stack

- **Language:** Python  
- **Library:** Pygame (for graphics and input)  
- **AI Techniques:** BFS, DFS, A\*, Hill Climbing, DFS-ID  

---

> Created using Python & Pygame | Demonstrates classic AI pathfinding algorithms in a maze game.
