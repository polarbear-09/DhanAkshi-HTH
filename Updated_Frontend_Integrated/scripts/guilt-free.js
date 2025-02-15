// guilt-free.js
function calculateBudget() {
    const income = document.getElementById("income").value;
    const percentage = document.getElementById("percentage").value;
    
    if (!income || !percentage || income <= 0 || percentage <= 0 || percentage > 100) {
        alert("Please enter valid income and percentage values.");
        return;
    }
    
    const budget = (income * percentage) / 100;
    document.getElementById("budgetAmount").textContent = `💵 You can spend: $${budget.toFixed(2)}`;
    showMotivation();
}

function showMotivation() {
    const messages = [
        "Smart spending = Happy Wallet! 💰",
        "Budgeting today means freedom tomorrow!",
        "Enjoy your guilt-free purchases! 🎉",
        "Every smart choice builds wealth!"
    ];
    const randomMessage = messages[Math.floor(Math.random() * messages.length)];
    document.getElementById("motivationText").textContent = randomMessage;
}
