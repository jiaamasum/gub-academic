# N-Rooks Problem Solver 🏰♜

A simple Python script to solve the classic **N-Rooks** problem: placing `N` rooks on an `N×N` chessboard such that no two rooks attack each other. Rooks attack in straight lines — horizontally and vertically — so this solution ensures one rook per row and per column.

---

## 🔍 Problem Statement

Place **N rooks** on an **N×N** chessboard so that:
- No two rooks are in the same row
- No two rooks are in the same column

Output a valid configuration using `1`s (for rooks) and `0`s (for empty cells).

---

## 🧠 Approach

We place a rook at position `(i, i)` for all rows `i`. This ensures:
- Each row has exactly one rook
- Each column has exactly one rook  
This is one of many valid solutions.
