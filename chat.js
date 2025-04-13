/* async function getAIResponse(userInput) {
    const response = await fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ input: userInput })
    });

    const data = await response.json();
    return data.response;
} */
    const messageInput = document.getElementById("message-input");
    const modelSelector = document.getElementById("model-selector"); // if you're using one
    
    messageInput.addEventListener("keydown", function(event) {
        if (event.key === "Enter" && !event.shiftKey) {
            event.preventDefault(); // Prevent newline (if textarea) or form submit
    
            const message = messageInput.value.trim();
            const selectedModel = modelSelector ? modelSelector.value : "default-model";
    
            if (message === "") return;
    
            sendMessage(message, selectedModel);
            messageInput.value = ""; // Clear the input after sending
        }
    });
    
    function sendMessage(message, model) {
        fetch("/send_message", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ message: message, model: model }),
        })
        .then(response => response.json())
        .then(data => {
            console.log("Server response:", data);
            // Optional: Update your chat display here
        })
        .catch(error => {
            console.error("Error:", error);
        });
    }
    