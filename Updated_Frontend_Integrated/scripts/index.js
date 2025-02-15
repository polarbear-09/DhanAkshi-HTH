// index.js
document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("start-session").addEventListener("click", () => {
        document.getElementById("session-output").textContent = "🧠 Your financial session has started! Take control now!";
    });
    document.getElementById("crisis-mode").addEventListener("click", () => {
        alert("🚨 Crisis Mode Activated! Redirecting to emergency support...");
        window.location.href = 'crisis.html';
    });
});
