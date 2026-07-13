const usernameInput = document.getElementById("username");
const messageInput = document.getElementById("message");
const sendButton = document.getElementById("send-btn");
const messagesEl = document.getElementById("messages");
const statusEl = document.getElementById("status");
const form = document.getElementById("chat-form");

const wsProtocol = window.location.protocol === "https:" ? "wss:" : "ws:";
const socket = new WebSocket(`${wsProtocol}//${window.location.host}/ws`);

function timestamp() {
    return new Date().toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit",
    });
}

function scrollToBottom() {
    messagesEl.scrollTop = messagesEl.scrollHeight;
}

function addMessage(text, type, sender) {
    const item = document.createElement("li");
    item.className = `message message--${type}`;

    const meta = document.createElement("div");
    meta.className = "message__meta";
    meta.textContent = `${sender} · ${timestamp()}`;

    const body = document.createElement("div");
    body.className = "message__body";
    body.textContent = text;

    item.appendChild(meta);
    item.appendChild(body);
    messagesEl.appendChild(item);
    scrollToBottom();
}

function addSystemMessage(text) {
    const item = document.createElement("li");
    item.className = "message message--system";
    item.textContent = text;
    messagesEl.appendChild(item);
    scrollToBottom();
}

function setStatus(text, state) {
    statusEl.textContent = text;
    statusEl.className = `status status--${state}`;
}

socket.onopen = () => {
    setStatus("Connected", "connected");
    addSystemMessage("Connection established.");
};

socket.onmessage = (event) => {
    addMessage(event.data, "received", "Server");
};

socket.onclose = () => {
    setStatus("Disconnected", "disconnected");
    addSystemMessage("Connection lost.");
    sendButton.disabled = true;
};

socket.onerror = () => {
    setStatus("Error", "disconnected");
};

form.addEventListener("submit", (event) => {
    event.preventDefault();

    const text = messageInput.value.trim();
    if (!text || socket.readyState !== WebSocket.OPEN) {
        return;
    }

    const username = usernameInput.value.trim() || "You";
    addMessage(text, "sent", username);
    socket.send(text);

    messageInput.value = "";
    messageInput.focus();
});
