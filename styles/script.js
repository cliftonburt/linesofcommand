const terminal = document.getElementById("chat-history");
const input = document.getElementById("command-input");

input.addEventListener("keypress", (event) => {
    if (event.key === "Enter") {
        const userMessage = input.value.trim();

        if (userMessage) {
            // Add user message to the chat
            const userMessageElement = document.createElement("div");
            userMessageElement.className = "chat-message user-message";
            userMessageElement.textContent = userMessage;
            terminal.appendChild(userMessageElement);

            // Simulate bot response
            const botResponse = simulateBotResponse(userMessage);
            const botMessageElement = document.createElement("div");
            botMessageElement.className = "chat-message bot-message";
            botMessageElement.textContent = botResponse;
            terminal.appendChild(botMessageElement);

            // Scroll to the bottom
            terminal.scrollTop = terminal.scrollHeight;

            // Clear input field
            input.value = "";
        }
    }
});

function simulateBotResponse(message) {
    // Basic bot logic for demonstration
    if (message.toLowerCase().includes("hello")) {
        return "Hello there! How can I assist you today?";
    } else if (message.toLowerCase().includes("help")) {
        return "Available commands: hello, help, exit.";
    } else {
        return "I'm sorry, I didn't understand that. Try typing 'help' for available commands.";
    }
}
