# 🏦 Banking Management System

A console-based Banking Management System developed using **Python**. The application demonstrates basic banking operations, role-based access, customer account management, and persistent data storage using JSON.

This project was developed as a practical demonstration of Python programming, modular software development, file handling, and basic banking application logic.

## 📌 Table of Contents

* [Project Overview](#-project-overview)
* [Features](#-features)
* [User Roles](#-user-roles)
* [Technologies Used](#-technologies-used)
* [Project Structure](#-project-structure)
* [Getting Started](#-getting-started)
* [How to Run](#-how-to-run)
* [Data Storage](#-data-storage)
* [Future Improvements](#-future-improvements)
* [Disclaimer](#-disclaimer)
* [Author](#-author)

## 📖 Project Overview

The Banking Management System is a Python application designed to simulate basic banking activities through a command-line interface.

It organizes banking operations around different user roles, allowing authorized users to perform relevant administrative and account-related tasks.

The project uses a modular structure to separate application logic into different Python files. JSON-based storage is used to maintain application data between sessions.

## ✨ Features

### 👨‍💼 Manager Features

* Staff management.
* Customer account oversight.
* Account restriction management.
* Customer balance management.
* Administrative operations.

### 🧑‍💻 Staff Features

* Create customer accounts.
* View customer account balances.
* Deposit money into customer accounts.
* Withdraw money from customer accounts.
* Restrict customer accounts.
* Unblock restricted customer accounts.
* Delete customer accounts.

### 👤 Customer Features

* Check account balance.
* Transfer money.
* Block their own account.

*The availability of individual features depends on the current implementation of the application.*

## 👥 User Roles

The application is designed around three primary roles:

| Role     | Description                                                  |
| -------- | ------------------------------------------------------------ |
| Manager  | Handles administrative and management operations.            |
| Staff    | Performs customer account management and banking operations. |
| Customer | Accesses personal account functions.                         |

Each role is intended to have access to the operations relevant to its responsibilities.

## 🛠️ Technologies Used

* **Python** — Core programming language.
* **JSON** — Data storage and persistence.
* **Git** — Version control.
* **GitHub** — Source code hosting and project collaboration.

## 📂 Project Structure

```text
banking_system/
│
├── banking_system.py
├── customer_module.py
├── staff_module.py
├── data_manager.py
├── explain.py
├── .gitignore
└── README.md
```

### File Descriptions

| File                 | Purpose                                                      |
| -------------------- | ------------------------------------------------------------ |
| `banking_system.py`  | Main application entry point and navigation.                 |
| `customer_module.py` | Contains customer-related functionality.                     |
| `staff_module.py`    | Contains staff-related functionality.                        |
| `data_manager.py`    | Handles loading and saving application data.                 |
| `explain.py`         | Contains supplementary project explanations or related code. |
| `.gitignore`         | Specifies files Git should exclude from version control.     |
| `README.md`          | Provides project documentation and usage instructions.       |

## 🚀 Getting Started

Follow these instructions to run the project on your local computer.

### Prerequisites

You need:

* Python 3 installed.
* Git installed.
* A code editor such as Visual Studio Code.

### 1. Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/amsanda/banking_system.git
```

### 2. Navigate to the Project Directory

```bash
cd banking_system
```

### 3. Run the Application

Execute the main Python file:

```bash
python banking_system.py
```

If your system uses the Python launcher on Windows, you can also try:

```powershell
py banking_system.py
```

Follow the instructions displayed in the terminal to interact with the application.

## 💾 Data Storage

The application uses JSON for persistent data storage.

The data file is named:

```text
bank_data.json
```

This file is excluded from Git tracking because it may contain customer information, account balances, or other sensitive application data.

For local development, ensure that the application can create or access the required data file.

**Important:** Do not upload real customer records, passwords, or financial information to a public repository.

## 🔮 Future Improvements

Potential improvements include:

* Developing a graphical user interface.
* Building a web-based banking dashboard.
* Improving authentication and access control.
* Implementing secure password hashing.
* Adding transaction history and downloadable statements.
* Strengthening transaction validation and error handling.
* Adding automated unit and integration tests.
* Introducing database integration using SQLite or PostgreSQL.
* Improving financial transaction consistency and audit logging.
* Adding comprehensive input validation and account security controls.

## ⚠️ Disclaimer

This project is intended for educational purposes and software development practice.

It is **not a production-ready banking application** and should not be used to manage real customer funds or sensitive financial information.

A real banking system requires comprehensive security controls, reliable transaction processing, audit trails, regulatory compliance, and extensive testing.

## 👨‍💻 Author

**Ahmad Sanda**

Software Engineering Student | Python Developer

GitHub: [@amsanda](https://github.com/amsanda)

### Repository

Explore the source code:

[Banking Management System on GitHub](https://github.com/amsanda/banking_system)

---

⭐ If you find this project interesting, feel free to explore the source code and follow my software development journey.
