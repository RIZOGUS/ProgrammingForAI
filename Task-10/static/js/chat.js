const chatMessages = document.getElementById('chat-messages');
const chatForm = document.getElementById('chat-form');
const chatInput = document.getElementById('chat-input');
const sendBtn = document.getElementById('send-btn');
const typingIndicator = document.getElementById('typing-indicator');

// Add welcome message on load
window.addEventListener('DOMContentLoaded', () => {
    addBotMessage("Hello! Welcome to the University Admission Chatbot. 👋\n\nI can help you with:\n• Available programs\n• Admission requirements\n• Application deadlines\n• Tuition fees\n\nHow can I assist you today?");
});

chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const message = chatInput.value.trim();
    if (!message) return;

    // Add user message
    addUserMessage(message);
    chatInput.value = '';

    // Show typing indicator
    showTyping();

    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message })
        });

        const data = await response.json();

        // Simulate delay for more natural feel
        setTimeout(() => {
            hideTyping();
            addBotMessage(data.response);
        }, 500);

    } catch (error) {
        hideTyping();
        addBotMessage("Sorry, I'm having trouble connecting. Please try again.");
    }
});

function addUserMessage(text) {
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message user';
    messageDiv.innerHTML = `
        <div class="message-avatar">👤</div>
        <div class="message-content">${escapeHtml(text)}</div>
    `;
    chatMessages.appendChild(messageDiv);
    scrollToBottom();
}

function addBotMessage(text) {
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message bot';

    // Convert markdown-style bold to HTML
    const formattedText = text
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        .replace(/\n/g, '<br>');

    messageDiv.innerHTML = `
        <div class="message-avatar">🤖</div>
        <div class="message-content">${formattedText}</div>
    `;
    chatMessages.appendChild(messageDiv);
    scrollToBottom();
}

function showTyping() {
    typingIndicator.classList.add('active');
    scrollToBottom();
}

function hideTyping() {
    typingIndicator.classList.remove('active');
}

function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Auto-focus input
chatInput.focus();
