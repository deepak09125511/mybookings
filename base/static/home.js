document.addEventListener("DOMContentLoaded", function() {
    let chatMessages = document.getElementById("chat-messages");
    chatMessages.scrollTop = chatMessages.scrollHeight; // Auto-scroll to latest message

    document.getElementById("message-form").addEventListener("submit", function(event) {
        let messageInput = document.getElementById("message-input");
        if (messageInput.value.trim() === "") {
            event.preventDefault(); // Prevent form submission if input is empty
        } else {
            setTimeout(() => {
                chatMessages.scrollTop = chatMessages.scrollHeight; // Scroll down after sending
            }, 100);
        }
    });
});

