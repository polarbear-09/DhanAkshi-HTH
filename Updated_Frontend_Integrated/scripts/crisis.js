// crisis.js
function startBreathingExercise() {
    const breathingText = document.getElementById('breathing-animation');
    breathingText.classList.remove('hidden');
    breathingText.innerText = "🌬️ Breathe in... Hold... Breathe out...";
    setTimeout(() => {
        breathingText.classList.add('hidden');
    }, 10000);
}

function lockShoppingApps() {
    alert("🔒 Shopping apps have been temporarily locked to prevent impulse purchases!");
}

function callSupport() {
    alert("📞 Connecting you to financial support... Stay calm, help is on the way!");
}
