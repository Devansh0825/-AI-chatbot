let isWaitingForResponse = false;

// Initialize chat functionality when page loads
document.addEventListener('DOMContentLoaded', function() {
    const messageInput = document.getElementById('messageInput');
    const sendButton = document.getElementById('sendButton');
    
    // Send message on Enter key press
    messageInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });
    
    // Focus on input field
    messageInput.focus();
});

function sendMessage() {
    const messageInput = document.getElementById('messageInput');
    const message = messageInput.value.trim();
    
    if (!message || isWaitingForResponse) {
        return;
    }
    
    // Clear input
    messageInput.value = '';
    
    // Add user message to chat
    addMessageToChat(message, 'user');
    
    // Show typing indicator
    showTypingIndicator();
    
    // Set waiting state
    isWaitingForResponse = true;
    updateSendButton(false);
    
    // Send message to server
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        hideTypingIndicator();
        
        if (data.response) {
            addMessageToChat(data.response, 'bot', data.intent, data.confidence);
        } else {
            addMessageToChat('Sorry, I encountered an error. Please try again.', 'bot', 'error');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        hideTypingIndicator();
        addMessageToChat('Sorry, I encountered a connection error. Please check your internet connection and try again.', 'bot', 'error');
    })
    .finally(() => {
        isWaitingForResponse = false;
        updateSendButton(true);
        messageInput.focus();
    });
}

function askQuestion(question) {
    const messageInput = document.getElementById('messageInput');
    messageInput.value = question;
    sendMessage();
}

function addMessageToChat(message, sender, intent = null, confidence = null) {
    const chatMessages = document.getElementById('chatMessages');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}-message`;
    
    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    
    // Add confidence styling for bot messages
    if (sender === 'bot' && confidence !== null) {
        if (confidence > 0.8) {
            contentDiv.className += ' confidence-high';
        } else if (confidence > 0.5) {
            contentDiv.className += ' confidence-medium';
        } else {
            contentDiv.className += ' confidence-low';
        }
    }
    
    if (sender === 'user') {
        contentDiv.innerHTML = `<p class="mb-0">${escapeHtml(message)}</p>`;
    } else {
        let botContent = `
            <div class="d-flex align-items-center mb-2">
                <i class="fas fa-robot text-primary me-2"></i>
                <strong>Internship Assistant</strong>
            </div>
        `;
        
        // Add intent badge if available
        if (intent && intent !== 'error' && intent !== 'fallback') {
            botContent += `<span class="intent-badge intent-${intent}">${formatIntent(intent)}</span><br>`;
        }
        
        botContent += `<div>${formatMessage(message)}</div>`;
        
        // Add confidence indicator for debugging (only show for low confidence)
        if (confidence !== null && confidence < 0.5) {
            botContent += `<div class="message-meta">Confidence: ${Math.round(confidence * 100)}%</div>`;
        }
        
        contentDiv.innerHTML = botContent;
    }
    
    messageDiv.appendChild(contentDiv);
    chatMessages.appendChild(messageDiv);
    
    // Scroll to bottom
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function showTypingIndicator() {
    const chatMessages = document.getElementById('chatMessages');
    const typingDiv = document.createElement('div');
    typingDiv.id = 'typingIndicator';
    typingDiv.className = 'message bot-message';
    typingDiv.innerHTML = `
        <div class="message-content">
            <div class="d-flex align-items-center mb-2">
                <i class="fas fa-robot text-primary me-2"></i>
                <strong>Internship Assistant</strong>
            </div>
            <div class="typing-indicator">
                <span></span>
                <span></span>
                <span></span>
                <em class="ms-2">typing...</em>
            </div>
        </div>
    `;
    
    chatMessages.appendChild(typingDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function hideTypingIndicator() {
    const typingIndicator = document.getElementById('typingIndicator');
    if (typingIndicator) {
        typingIndicator.remove();
    }
}

function updateSendButton(enabled) {
    const sendButton = document.getElementById('sendButton');
    const messageInput = document.getElementById('messageInput');
    
    sendButton.disabled = !enabled;
    messageInput.disabled = !enabled;
    
    if (enabled) {
        sendButton.innerHTML = '<i class="fas fa-paper-plane"></i> Send';
    } else {
        sendButton.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
    }
}

function resetConversation() {
    if (isWaitingForResponse) {
        return;
    }
    
    fetch('/reset', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        }
    })
    .then(response => response.json())
    .then(data => {
        // Clear chat messages except welcome message
        const chatMessages = document.getElementById('chatMessages');
        const messages = chatMessages.querySelectorAll('.message');
        
        // Keep only the first message (welcome message)
        for (let i = 1; i < messages.length; i++) {
            messages[i].remove();
        }
        
        // Show reset confirmation
        addMessageToChat('Conversation has been reset. How can I help you with your internship questions?', 'bot', 'greeting');
    })
    .catch(error => {
        console.error('Error resetting conversation:', error);
        addMessageToChat('Sorry, I couldn\'t reset the conversation. You can continue asking questions.', 'bot', 'error');
    });
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function formatMessage(message) {
    // Simple formatting for better readability
    return message
        .replace(/\n/g, '<br>')
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        .replace(/\*(.*?)\*/g, '<em>$1</em>')
        .replace(/\d+\)\s/g, '<br>$&') // Add line breaks before numbered lists
        .replace(/^(\d+\.\s)/gm, '<br>$1'); // Add line breaks before numbered lists
}

function formatIntent(intent) {
    return intent
        .replace(/_/g, ' ')
        .replace(/\b\w/g, l => l.toUpperCase());
}

// Add some keyboard shortcuts
document.addEventListener('keydown', function(e) {
    // Ctrl/Cmd + R to reset conversation
    if ((e.ctrlKey || e.metaKey) && e.key === 'r') {
        e.preventDefault();
        resetConversation();
    }
    
    // Escape to focus input
    if (e.key === 'Escape') {
        document.getElementById('messageInput').focus();
    }
});

// Add auto-resize for input field
function autoResize(element) {
    element.style.height = 'auto';
    element.style.height = element.scrollHeight + 'px';
}

// Optional: Add some example questions that users can click
function addExampleQuestions() {
    const examples = [
        "How do I write a good internship application?",
        "What should I expect in a technical interview?",
        "Are there internships available for freshmen?",
        "How can I find remote internship opportunities?",
        "What's the typical internship timeline for summer programs?"
    ];
    
    // This could be added to the sidebar or as quick suggestions
    console.log('Example questions available:', examples);
}
