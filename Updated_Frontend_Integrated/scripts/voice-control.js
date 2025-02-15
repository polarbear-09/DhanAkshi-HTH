document.addEventListener("DOMContentLoaded", () => {
    const aiResponse = document.getElementById("ai-response");
    const startVoice = document.getElementById("startVoice");
    const stopVoice = document.getElementById("stopVoice");

    // Speech Recognition Setup
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const recognition = new SpeechRecognition();
    recognition.lang = "en-US";
    recognition.continuous = false;
    recognition.interimResults = false;

    // AI Response Logic (Mock)
    function generateAIResponse(command) {
        const responses = {
            "how can i save more money": "Try setting up a 50-30-20 budget. Need help calculating?",
            "help me control impulse spending": "I recommend adding items to a wishlist before purchasing. Want me to track it?",
            "show my weekly spending report": "Here's your latest spending breakdown: Food 30%, Shopping 20%, Rent 40%.",
            "i'm feeling stressed about money": "Take a deep breath. Money is a tool, not a master. Do you need a savings plan?",
            "set a savings goal for this month": "How much do you want to save? I can help break it into daily targets."
        };

        const lowerCommand = command.toLowerCase();
        return responses[lowerCommand] || "I'm not sure about that, but I can give financial advice! Try asking me about savings.";
    }

    // Start Voice Recognition
    startVoice.addEventListener("click", () => {
        aiResponse.innerHTML = "<p>Listening... 🎙️</p>";
        recognition.start();
    });

    // Stop Voice Recognition
    stopVoice.addEventListener("click", () => {
        recognition.stop();
        aiResponse.innerHTML = "<p>Voice input stopped.</p>";
    });

    // Speech Recognition Result Handling
    recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        aiResponse.innerHTML = `<p>🗣️ You: ${transcript}</p>`;

        // Generate AI Response
        setTimeout(() => {
            const aiReply = generateAIResponse(transcript);
            aiResponse.innerHTML += `<p>🤖 AI: ${aiReply}</p>`;
        }, 1000);
    };

    // Handle Speech Recognition Errors
    recognition.onerror = (event) => {
        aiResponse.innerHTML = `<p>Error: ${event.error}</p>`;
    };
});
