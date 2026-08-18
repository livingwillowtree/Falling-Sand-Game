# FuckAssSandGame69420 

This entire README is written by Gemini, cuz I'm lazy asf, code itself is self study.

A modular, real-time Falling Sand simulation engine built from scratch in Python and Pygame. 

It features custom grid physics for multiple particle types, decoupled rendering, and an custom **8-octant Bresenham Line Interpolation** algorithm to ensure continuous particle painting during rapid mouse movements.

---

## Key Features

* **Simple Physics Engine:** Custom simulation loop supporting gravity, diagonal sliding, and fluid displacement.
* **Continuous Line Interpolation:** Integrates Bresenham's line algorithm to bridge mouse frame gaps during fast dragging — no air gaps between mouse points.
* **Decoupled Architecture:** Clean separation of concerns across input/engine orchestration, physics logic, and screen rendering.
* **FPS-Independent Controls:** Implements `pygame.time.get_ticks()` continuous placement cooldowns rather than frame-locked delays.

---

## Included Particle Types

| Key | Particle | Behavior / Physics Rules |
| :---: | :--- | :--- |
| **`1`** | **Water** | Affected by gravity, slides diagonally, and flows horizontally. |
| **`2`** | **Sand** | Affected by gravity and cascades diagonally off edges/slopes. |
| **`3`** | **Stone** | Heavy solid affected strictly by downward gravity. |
| **`4`** | **Steel** | Fixed structural solid; unaffected by gravity. |
| **`C`** | **Clear** | Resets the grid array to empty cells. |

---

## Controls

* **Left Click + Drag:** Paint active particle into the grid
* **`1` / `2` / `3` / `4`:** Switch active particle (Water / Sand / Stone / Steel)
* **`C`:** Clear the entire grid
* **`ESC`:** Exit game

---

## How To Set Up

* Lmao, no I'm not teaching you. Go download this figure it out, its literally one venv and pip install
