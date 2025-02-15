// leaderboard.js
document.addEventListener("DOMContentLoaded", () => {
    const leaderboardData = [
        { name: "Alice", streak: 15, saved: 500 },
        { name: "Bob", streak: 12, saved: 420 },
        { name: "Charlie", streak: 10, saved: 350 },
        { name: "You", streak: 8, saved: 300 },
    ];
    
    const leaderboardBody = document.getElementById("leaderboardBody");
    leaderboardBody.innerHTML = "";
    leaderboardData.forEach((user, index) => {
        const row = `<tr>
            <td>#${index + 1}</td>
            <td>${user.name}</td>
            <td>${user.streak}🔥</td>
            <td>₹${user.saved}</td>
        </tr>`;
        leaderboardBody.innerHTML += row;
    });
    
    document.getElementById("userRank").textContent = "#4";
    document.getElementById("userStreak").textContent = "8";
    
    const challenges = [
        "Save ₹100 this week!",
        "Avoid impulse purchases for 3 days!",
        "Track all expenses for a full week!",
        "Cook at home instead of ordering food!"
    ];
    
    document.getElementById("newChallenge").addEventListener("click", () => {
        const randomChallenge = challenges[Math.floor(Math.random() * challenges.length)];
        document.getElementById("challengeText").textContent = randomChallenge;
    });
});
