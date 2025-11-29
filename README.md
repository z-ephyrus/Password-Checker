🔐 Python Password Checker (bcrypt)

A simple, secure Python script demonstrating modern password hashing and verification using the industry-standard bcrypt algorithm.

This example uses:

bcrypt for hashing and verifying passwords

getpass for masked password input

Secure, salted hashing designed for real-world authentication systems

✨ Features

Secure Hashing
Uses bcrypt.hashpw() to generate strong, salted, slow-hashes suitable for authentication.

Automatic Salt Handling
Each hash contains its unique salt — no need to store or manage salts separately.

Hidden Input
Uses getpass to safely read passwords without echoing them on screen.

Secure Verification
Check entered passwords using bcrypt.checkpw().

🛠️ Prerequisites

You’ll need:

Python 3.x

The bcrypt package (not included in the Python standard library)

📦 Installation

Clone the repository:

git clone https://github.com/your-username/password-checker.git
cd password-checker


Install dependencies:

pip install bcrypt

🚀 Usage

Run the script:

python password_checker.py


The script will ask for:

A password to hash

A password to verify against the stored hash
