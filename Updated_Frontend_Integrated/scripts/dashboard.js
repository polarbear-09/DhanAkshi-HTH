document.addEventListener("DOMContentLoaded", function () {
    console.log("📊 Dashboard Loaded!");

    // Simulated user data
    const userMood = "happy"; // Options: happy, sad, stressed
    const spendingStreak = 7; // Days
    const leaderboard = [
        { name: "Alice", score: 1200 },
        { name: "Bob", score: 950 },
        { name: "You", score: 870 },
        { name: "Charlie", score: 800 }
    ];

    // Update mood-based UI
    updateMoodUI(userMood);

    // Update spending streak
    document.getElementById("streak-count").textContent = spendingStreak;

    // Populate leaderboard
    updateLeaderboard(leaderboard);

    // Spending advice button
    document.getElementById("get-advice").addEventListener("click", async () => {
        const advice = await fetchFinancialAdvice();
        document.getElementById("advice-text").textContent = advice;
    });
});

// Function to update UI based on mood
function updateMoodUI(mood) {
    const moodIndicator = document.getElementById("mood-indicator");
    moodIndicator.classList.add(mood);

    let moodText = "Feeling Neutral";
    if (mood === "happy") moodText = "😊 Feeling Happy!";
    else if (mood === "sad") moodText = "😢 Feeling Sad...";
    else if (mood === "stressed") moodText = "😟 Feeling Stressed!";

    moodIndicator.textContent = moodText;
}

// Function to fetch AI-powered financial advice
async function fetchFinancialAdvice() {
    try {
        const response = await fetch("/api/get-financial-advice");
        const data = await response.json();
        return data.advice || "Unable to fetch advice at the moment.";
    } catch (error) {
        console.error("Error fetching advice:", error);
        return "Error fetching advice. Please try again later.";
    }
}

// Function to update leaderboard
function updateLeaderboard(players) {
    const leaderboardList = document.getElementById("leaderboard-list");
    leaderboardList.innerHTML = "";

    players.forEach((player, index) => {
        const listItem = document.createElement("li");
        listItem.textContent = `#${index + 1} ${player.name} - ${player.score} pts`;
        leaderboardList.appendChild(listItem);
    });
}
