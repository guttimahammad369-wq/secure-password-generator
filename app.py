from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import secrets
import string
import math

app = Flask(__name__)
CORS(app)

ATTACK_SPEED = 1_000_000_000  # 1 billion guesses per second


def generate_password(length, use_upper, use_lower, use_digits, use_symbols, exclude_chars=""):
    characters = ""
    password = []

    if use_upper:
        upper = ''.join(c for c in string.ascii_uppercase if c not in exclude_chars)
        characters += upper
        if upper:
            password.append(secrets.choice(upper))

    if use_lower:
        lower = ''.join(c for c in string.ascii_lowercase if c not in exclude_chars)
        characters += lower
        if lower:
            password.append(secrets.choice(lower))

    if use_digits:
        digits = ''.join(c for c in string.digits if c not in exclude_chars)
        characters += digits
        if digits:
            password.append(secrets.choice(digits))

    if use_symbols:
        symbols = ''.join(c for c in string.punctuation if c not in exclude_chars)
        characters += symbols
        if symbols:
            password.append(secrets.choice(symbols))

    if not characters:
        return None, 0

    while len(password) < length:
        password.append(secrets.choice(characters))

    secrets.SystemRandom().shuffle(password)

    return ''.join(password), len(characters)


def calculate_entropy(length, charset_size):
    return length * math.log2(charset_size)


def entropy_strength(entropy):
    if entropy < 28:
        return "Very Weak"
    elif entropy < 36:
        return "Weak"
    elif entropy < 60:
        return "Moderate"
    elif entropy < 128:
        return "Strong"
    else:
        return "Very Strong"


def convert_time(seconds):
    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    years = days / 365

    if years >= 1:
        return f"{years:.2f} years"
    elif days >= 1:
        return f"{days:.2f} days"
    elif hours >= 1:
        return f"{hours:.2f} hours"
    elif minutes >= 1:
        return f"{minutes:.2f} minutes"
    else:
        return f"{seconds:.2f} seconds"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    length = int(data["length"])

    password, charset_size = generate_password(
        length,
        data["upper"],
        data["lower"],
        data["digits"],
        data["symbols"],
        data["exclude"]
    )

    if not password:
        return jsonify({"error": "Select at least one character type."})

    entropy = calculate_entropy(length, charset_size)
    strength = entropy_strength(entropy)

    combinations = charset_size ** length
    seconds = combinations / ATTACK_SPEED
    crack_time = convert_time(seconds)

    return jsonify({
        "password": password,
        "charset_size": charset_size,
        "entropy": round(entropy, 2),
        "strength": strength,
        "combinations": f"{combinations:,}",
        "crack_time": crack_time
    })


if __name__ == "__main__":
    app.run(debug=True)