document.addEventListener("DOMContentLoaded", () => {
    const spendingChartCtx = document.getElementById("spendingChart").getContext("2d");
    const savingTipsText = document.getElementById("savingTips");
    const refreshTipsButton = document.getElementById("refreshTips");
    const budgetFill = document.getElementById("budgetFill");
    const budgetPercentage = document.getElementById("budgetPercentage");

    // Sample spending data
    const spendingData = {
        labels: ["Food", "Rent", "Shopping", "Entertainment", "Savings", "Transport"],
        datasets: [{
            data: [2000, 8000, 2500, 1500, 3000, 1000], // Sample values in INR
            backgroundColor: ["#ff6384", "#36a2eb", "#ffce56", "#8e44ad", "#2ecc71", "#f39c12"]
        }]
    };

    // Render Pie Chart
    new Chart(spendingChartCtx, {
        type: "pie",
        data: spendingData
    });

    // AI-Generated Saving Tips
    const savingTips = [
        "Try a 'No-Spend Challenge' for a week and save extra! 💰",
        "Avoid impulse buys – wait 24 hours before making a purchase! 🕒",
        "Set up automatic savings transfers to make saving effortless! 🏦",
        "Cut down on subscriptions you no longer use! 📉",
        "Meal prep at home to save on food expenses! 🍽️"
    ];

    function generateSavingTip() {
        const randomTip = savingTips[Math.floor(Math.random() * savingTips.length)];
        savingTipsText.textContent = randomTip;
    }

    refreshTipsButton.addEventListener("click", generateSavingTip);
    
    // Budget Progress Calculation
    const totalBudget = 15000; // Example total budget
    const totalSpent = spendingData.datasets[0].data.reduce((a, b) => a + b, 0);
    const spentPercentage = Math.round((totalSpent / totalBudget) * 100);

    budgetFill.style.width = `${spentPercentage}%`;
    budgetPercentage.textContent = `${spentPercentage}%`;

    // Initialize Data
    generateSavingTip();
});
