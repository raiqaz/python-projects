# 🏪 Hostel Budget Tracker

A simple, lightweight Python command-line tool built to manage daily hostel expenses and track remaining monthly budgets in real-time.

---

## 🚀 Features
* **Dynamic Budgeting:** Input your customizable starting monthly budget.
* **Continuous Logging:** Uses File Append mode (`"a"`) to log daily items (like tea, snacks, or milkshakes) without overwriting your history.
* **Automated Math:** Reads your saved transactions, sums them up, and instantly shows your remaining balance.
* **Persistent Storage:** Keeps all transaction data saved permanently in a clean `expenses.txt` file.

---

## 🛠️ How It Works (Concepts Applied)
This project was built to practice core Python fundamentals:
1. **File Input/Output:** Using `with open()` to securely read (`"r"`) and append (`"a"`) text files.
2. **String Manipulation:** Using `.split(":")` to parse logged data.
3. **Data Type Casting:** Converting string inputs into integers using `int()` to perform arithmetic operations.

---

## 🏃‍♂️ How to Run It
1. Clone this repository or download `budget_tracker.py`.
2. Open your terminal or Command Prompt in the project folder.
3. Run the script using:
   ```bash
   python budget_tracker.py
   
