// chatbot.js
document.getElementById('sendMessage').addEventListener('click', function() {
    const userInput = document.getElementById('userInput');
    const message = userInput.value.trim();
    if (message) {
        appendMessage('user', message);
        setTimeout(() => appendMessage('bot', "That's an interesting financial concern! Let's talk about it."), 1000);
        userInput.value = '';
    }
});

function appendMessage(sender, text) {
    const chatWindow = document.getElementById('chatWindow');
    const messageDiv = document.createElement('div');
    messageDiv.classList.add(sender === 'user' ? 'user-message' : 'bot-message');
    messageDiv.innerHTML = `<p>${text}</p>`;
    chatWindow.appendChild(messageDiv);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}
