# 🧮 Simple Calculator

## 📌 Project Overview

This project is a **Simple Calculator** developed as part of my **CodSoft Python Programming Internship**. It performs basic arithmetic operations through both a **Command Line Interface (CLI)** and a **Graphical User Interface (GUI)** built with Python's Tkinter library.

The application is designed with reusable functions, input validation, and error handling to provide a smooth user experience.

---

## ✨ Features

* ➕ Addition
* ➖ Subtraction
* ✖️ Multiplication
* ➗ Division
* Input validation for numbers
* Division by zero handling
* Invalid operation detection
* User-friendly Tkinter GUI
* Clear button to reset inputs
* Reusable calculator logic shared between CLI and GUI

---

## 🛠️ Technologies Used

* Python 3
* Tkinter (GUI Library)

---

## 📂 Project Structure

```
Calculator-Project/
│
├── Calculator.py      # Calculator logic and CLI version
├── GUI.py             # Tkinter graphical interface
└── README.md
```

---

## 🚀 How to Run

### Method 1: Command Line Version

Run:

```bash
python Calculator.py
```

Follow the prompts to:

1. Enter the first number
2. Enter the second number
3. Select an operation
4. View the result
5. Continue or exit

---

### Method 2: GUI Version

Run:

```bash
python GUI.py
```

The graphical application allows you to:

* Enter two numbers
* Click an operation button (+, −, ×, ÷)
* View the result instantly
* Clear all fields using the **Clear** button

---


## ⚙️ Input Validation

The calculator checks for:

* Valid integer inputs
* Invalid operation choices
* Division by zero

If an invalid input is detected, an appropriate error message is displayed.

---

## 🎯 Learning Outcomes

Through this project, I learned:

* Python functions and modular programming
* Exception handling
* Input validation
* Building desktop applications using Tkinter
* Reusing business logic across multiple interfaces
* Creating clean and user-friendly Python applications
