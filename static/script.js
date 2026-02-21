async function generatePassword() {

    const length = document.getElementById("length").value;

    if (!length || length < 4) {
        alert("Please enter valid password length (min 4)");
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

    document.getElementById("password").innerText =
        "Password: " + result.password;

    document.getElementById("entropy").innerText =
        "Entropy: " + result.entropy + " bits";

    document.getElementById("strength").innerText =
        "Strength: " + result.strength;

    document.getElementById("combinations").innerText =
        "Total Combinations: " + result.combinations;

    document.getElementById("crack_time").innerText =
        "Estimated Crack Time: " + result.crack_time;
}