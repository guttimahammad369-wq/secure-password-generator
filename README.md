# 🔐 Advanced Secure Password Generator (Python) 
A professional, security-focused password generator built using Python. This project generates strong, secure passwords with entropy calculation, brute-force time estimation, guaranteed character inclusion, and customizable exclusions. 
--- 
## 🚀 Features ##
✅ Cryptographically Secure Password Generation (using Python secrets module) 
✅ Guaranteed inclusion of selected character types 
✅ Password Entropy Calculation (in bits) 
✅ Brute-Force Crack Time Estimation 
✅ Password Strength Classification 
✅ Character Exclusion Option (e.g., remove confusing characters like O, 0, l) 
✅ Total Possible Combinations Display 
✅ Clean, Modular Code Structure 
---
##📂 Project Structure ##
secure-password-generator/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
---
## 🔍 What This Project Does ##
This tool allows users to: 
- Choose password length
- Select character types:
- Uppercase letters
- Lowercase letters
- Numbers
- Symbols
- Exclude specific characters (like e, O, 0)
- Generate a secure password
- View:
- Entropy (bits of security)
- Total combinations
- Estimated cracking time(approx..)
- Strength level
---
## 🧠 Security Concepts Used ### 
1️⃣ Entropy Calculation 
Entropy measures how unpredictable a password is. 
Formula: Entropy = Length × log₂(CharacterSetSize) 
Higher entropy = harder to crack. 
--- 
### 2️⃣ Brute-Force Attack Simulation ##
The program estimates how long it would take an attacker to guess the password if they try 1 billion guesses per second. 
It converts time into: 
- Years
- Months
- Weeks
- Days
- Hours
- Minutes
- Seconds
---
### 3️⃣ Guaranteed Complexity If user selects: ##
- Uppercase
- Lowercase
- Digits
The system guarantees at least one character from each selected category. This prevents weak random distribution.
---
## 📊 Strength Levels | Entropy (bits) | Strength | ##
|---------------|----------| 
| < 28 | Very Weak | 
| 28–35 | Weak | 
| 36–59 | Moderate | 
| 60–127 | Strong | 
| 128+ | Very Strong | 
---
## 🛠 Technologies Used ##
🛠️ Tech Stack
🔹 Backend

Python 3

Flask

🔹 Frontend

HTML5

CSS3

JavaScript

👨‍💻 Author

Mahammad Gutti
GitHub: https://github.com/guttimahammad369-wq
