# 🔐 Shamir Secret Sharing Solver

This Python script reconstructs the **original secret** using Shamir’s Secret Sharing Scheme. Given a list of share points, it finds the constant term (i.e., the secret) using **Lagrange Interpolation**.

---

## 📁 Files Included

| File Name              | Description |
|------------------------|-------------|
| `shamir_secret_solver.py` | Main Python script to solve for the secret |
| `shamir_input.json`       | Input data (list of share points) |
| `shamir_secret_output.json` | Output file with reconstructed secret |
| `README.md`               | This readme file |

---

## 🧠 How It Works

- Takes at least 3 `(x, y)` share points from `shamir_input.json`
- Computes all combinations of 3 points
- Applies **Lagrange interpolation** on each combination
- Tracks which secret (`C`) appears most frequently
- Outputs the most likely value of the **original secret**

---

## ▶️ How to Run

### 1. Install Python and dependencies
Make sure you have Python installed:  
[https://www.python.org/downloads](https://www.python.org/downloads)

Install required library:
```bash
pip install sympy
