



````markdown
# 🔌 Smart Billing Expression Evaluator

An intelligent, web-based utility billing engine built for smart city simulations and competitive software development. Supports mixed-type expression evaluation, conditional logic, forecasting, and variable assignment — all through a simple, fast interface.

---

## 🎯 Project Overview

This system allows users to evaluate real-world utility billing expressions with:

- ✅ Variable assignment and reuse
- ✅ Arithmetic and boolean logic
- ✅ Short-circuit evaluation (&&, ||)
- ✅ Ternary expressions (e.g., `isPeak ? surcharge : 0`)
- ✅ Forecasting (`forecast(units)`)
- ✅ Memory inspection and reset functions

Built with:

- [x] **Python 3**
- [x] **Flask** (web framework)
- [x] **PLY** (expression parsing)
- [x] **HTML** (simple UI)

---

## 📦 Features

| Feature         | Description                                      |
|----------------|--------------------------------------------------|
| 📥 Input        | Billing logic (e.g. `base + units * rate`)       |
| 🧠 Memory       | Stores variables like a real scripting language |
| 🔁 Reset        | Clear all assigned variables                    |
| 👀 Inspect      | View current memory state                       |
| 🔮 Forecasting  | Predict usage with `forecast(units)`            |
| 🚫 Error Check  | Prevents divide-by-zero, syntax errors          |

---

## 🛠 How to Run Locally

### ✅ Step 1: Clone the Repo

```bash
git clone https://github.com/YOUR-USERNAME/smart-billing-evaluator.git
cd smart-billing-evaluator
````

### ✅ Step 2: Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On macOS/Linux
```

### ✅ Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### ✅ Step 4: Run the App

```bash
python run.py
```

Then open your browser at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧪 Testing

Run unit tests from the `/tests` folder:

```bash
pytest tests/
```

---

## 💬 Sample Input Expressions

```c
base = 100
rate = 2.5
units = 30
total = base + (rate * units)
isPeak = true
surcharge = 50
total = total + (isPeak ? surcharge : 0)
penalty = units > 1000 && !isLowIncome ? 500 : 0
nextMonth = forecast(units)
```

---

## 🧰 Project Structure

```
smart-billing-evaluator/
│
├── app/
│   ├── __init__.py
│   ├── views.py             # Flask routes
│   ├── evaluator.py         # Expression parser/evaluator
│   ├── templates/
│   │   └── index.html       # Web UI
│
├── tests/
│   └── test_evaluator.py    # Unit tests
│
├── run.py                   # App entry point
├── requirements.txt
├── README.md
├── .gitignore
```

---

## 👥 Team Members

* Mark Denis Mugai – C026-01-0733/2023
* Wilkister Kawira – C026-01-0727/2023
* Keziah Syokau Kioko – C026-01-0735/2023
* Zachary Odhiambo – C026-01-0764/2023
* Keith Kinuthia Ndarwa – C026-01-2228/2023

---

## ✍️ Author & Coordinator

**Mark Denis Mugai**
DeKUT – Computer Science Student


---

## 🏁 License

This project is open-source and free to use for educational and demonstration purposes.

````


