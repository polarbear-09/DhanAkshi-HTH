document.addEventListener("DOMContentLoaded", () => {
    const heartRateDisplay = document.getElementById("heartRate");
    const stressLevel = document.getElementById("stress-level");
    const spendingStatus = document.getElementById("spending-status");
    const calmModeBtn = document.getElementById("calmMode");
    const stopSpendingBtn = document.getElementById("stopSpending");
    const timeDisplay = document.getElementById("time");

    // Fake Heart Rate Simulation
    function generateHeartRate() {
        return Math.floor(Math.random() * (120 - 60) + 60); // 60-120 BPM
    }

    function updateHeartRate() {
        let heartRate = generateHeartRate();
        heartRateDisplay.textContent = heartRate;

        // Stress Detection Logic
        if (heartRate > 100) {
            stressLevel.textContent = "🚨 High Stress! Take a deep breath.";
            stressLevel.style.color = "red";
        } else if (heartRate > 80) {
            stressLevel.textContent = "⚠️ Mild Stress. Consider a break.";
            stressLevel.style.color = "orange";
        } else {
            stressLevel.textContent = "✅ Relaxed. Keep going!";
            stressLevel.style.color = "green";
        }
    }

    // Fake Spending Alert System
    function updateSpendingStatus() {
        const spendingWarnings = [
            "🚨 High spending detected! Set a limit.",
            "✅ On track! Keep saving.",
            "⚠️ Warning: Unusual spending pattern.",
            "💰 You have some budget left for the week."
        ];
        const randomWarning = spendingWarnings[Math.floor(Math.random() * spendingWarnings.length)];
        spendingStatus.textContent = randomWarning;
    }

    // Update time on the wearable UI
    function updateTime() {
        const now = new Date();
        const hours = now.getHours().toString().padStart(2, '0');
        const minutes = now.getMinutes().toString().padStart(2, '0');
        timeDisplay.textContent = `${hours}:${minutes}`;
    }

    // Activate Calm Mode
    calmModeBtn.addEventListener("click", () => {
        alert("🧘‍♂️ Activating guided breathing for stress relief...");
        stressLevel.textContent = "🧘‍♀️ Deep breathing activated...";
        stressLevel.style.color = "blue";
    });

    // Block Spending
    stopSpendingBtn.addEventListener("click", () => {
        alert("🚫 Crisis Mode Activated: Spending is temporarily blocked!");
        spendingStatus.textContent = "🔒 Spending Blocked!";
        spendingStatus.style.color = "red";
    });

    // Auto-update every 5 seconds
    setInterval(updateHeartRate, 5000);
    setInterval(updateSpendingStatus, 7000);
    setInterval(updateTime, 1000);

    // Initial Load
    updateHeartRate();
    updateSpendingStatus();
    updateTime();
});
