// home.js
document.addEventListener("DOMContentLoaded", () => {
    const featureCards = document.querySelectorAll(".feature-card");

    featureCards.forEach(card => {
        card.addEventListener("mouseenter", () => {
            card.style.boxShadow = "0px 10px 20px rgba(0, 0, 0, 0.3)";
        });
        card.addEventListener("mouseleave", () => {
            card.style.boxShadow = "none";
        });
    });

    const quotes = [
        "Small savings today, big rewards tomorrow! 💰",
        "Spend smart, live better! 🌟",
        "Your financial future starts with a single wise decision! 🚀",
        "Financial freedom is one habit away! 🔥"
    ];

    let quoteIndex = 0;
    setInterval(() => {
        document.querySelector(".changing-quote").textContent = quotes[quoteIndex];
        quoteIndex = (quoteIndex + 1) % quotes.length;
    }, 4000);
});
