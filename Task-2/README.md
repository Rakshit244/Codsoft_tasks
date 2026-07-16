# 🔐 Password Generator - CodSoft Internship Project

## 📌 Project Overview

This project is a **Password Generator** developed using Python as part of my **CodSoft Internship**. It creates secure and customizable passwords based on user preferences, allowing users to choose the password length and the types of characters to include.

The application uses Python's built-in **random** and **string** modules to generate strong, randomized passwords while ensuring that at least one character from each selected category is included.

---

## ✨ Features

* 🔢 Custom password length
* 🔠 Include uppercase letters
* 🔡 Include lowercase letters
* 🔢 Include numbers
* 🔣 Include special characters
* Input validation for all user entries
* Ensures selected character types appear in the password
* Generate multiple passwords in one session
* Simple and interactive command-line interface

---

## 🛠️ Technologies Used

* Python 3
* `random` module
* `string` module

---

## 🚀 How to Run

Run the program using:

```bash
python PasswordGenerator.py
```

The program will:

1. Ask for the desired password length.
2. Ask whether to include:

   * Uppercase letters
   * Lowercase letters
   * Numbers
   * Special characters
3. Generate a secure password based on your choices.
4. Ask whether you want to generate another password.

---

## ⚙️ Input Validation

The application validates user input by:

* Ensuring the password length is at least **4 characters**
* Accepting only **y** or **n** for character type selections
* Ensuring at least one character type is selected
* Handling invalid numeric input gracefully

---

## 🔒 Password Generation Logic

The generator follows these steps:

* Builds a pool of characters based on the selected options.
* Guarantees at least one character from each selected category.
* Fills the remaining characters randomly.
* Shuffles the password to improve randomness and security.

---

## 🎯 Learning Outcomes

Through this project, I learned:

* Working with Python's `random` and `string` modules
* Generating secure random passwords
* Input validation and error handling
* Writing reusable functions
* Building interactive command-line applications
* Implementing logic for customizable password generation
