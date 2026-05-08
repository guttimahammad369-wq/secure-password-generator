async function generatePassword() {

    const length = document.getElementById("length").value;

    if (!length || length < 4) {
        alert("Enter valid password length (min 4)");
        return;
    }

    const data = {
        length: length,
        upper: document.getElementById("upper").checked,
        lower: document.getElementById("lower").checked,
        digits: document.getElementById("digits").checked,
        symbols: document.getElementById("symbols").checked,
        exclude: document.getElementById("exclude").value
    };

    const response = await fetch("/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });

    const result = await response.json();

    if (result.error) {
        alert(result.error);
        return;
    }

    document.getElementById("password").innerText = "Password: " + result.password;
    document.getElementById("entropy").innerText = "Entropy: " + result.entropy + " bits";
    document.getElementById("strength").innerText = "Strength: " + result.strength;
    document.getElementById("combinations").innerText = "Total Combinations: " + result.combinations;
    document.getElementById("crack_time").innerText = "Basic Crack Time: " + result.crack_time;
}

function copyPassword() {
    const text = document.getElementById("password").innerText.replace("Password: ", "");
    if (!text) {
        alert("Generate password first!");
        return;
    }
    navigator.clipboard.writeText(text);
    alert("Copied!");
}

async function checkPassword() {

    const password = document.getElementById("checkPassword").value;

    if (!password) {
        alert("Enter password");
        return;
    }

    const response = await fetch("/check", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ password: password })
    });

    const result = await response.json();

    document.getElementById("checkResult").innerText =
        "Entropy: " + result.entropy +
        " | Strength: " + result.strength +
        " | Crack Time: " + result.crack_time;
}