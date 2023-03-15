<template>
  <div class="chat">
    <div class="messages">
      <div v-for="(msg, index) in conversation" :key="index" :class="msg.sender">
        <div class="message">{{ msg.message }}</div>
      </div>
    </div>
    <div class="input-area">
      <input
        v-model="currentMessage"
        @keydown.enter="sendMessage"
        type="text"
        placeholder="Type your message here..."
      />
      <button @click="sendMessage">Send</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ChatBox",
  data() {
    return {
      currentMessage: "",
      conversation: [],
    };
  },
  methods: {
    async sendMessage() {
      const message = this.currentMessage.trim();
      if (message) {
        this.conversation.push({ sender: "user", message: message });
        this.currentMessage = "";

        try {
          const response = await axios.post("http://127.0.0.1:5000/chatbot", {
            message: message,
          });
          const chatgptMessage = response.data.message;
          this.conversation.push({ sender: "chatgpt", message: chatgptMessage });
        } catch (error) {
          console.error("Error communicating with the Flask backend:", error);
        }
      }
    },
  },
};
</script>

<style scoped>
.chat {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100vh;
  width: 600px;
  margin: 0 auto;
  font-family: Arial, sans-serif;
  box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.1);
  background-color: #f7f9fa;
  border-radius: 8px;
}

.messages {
  overflow-y: auto;
  flex-grow: 1;
  padding: 20px;
}

.message {
  display: inline-block;
  max-width: 70%;
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 20px;
}

.user {
  text-align: right;
}

.user .message {
  background-color: #2979ff;
  color: #ffffff;
}

.chatgpt {
  text-align: left;
}

.chatgpt .message {
  background-color: #e0e0e0;
  color: #222222;
}

.input-area {
  display: flex;
  align-items: center;
  padding: 10px 20px;
  background-color: #ffffff;
  border-top: 1px solid #e0e0e0;
}

.input-area input {
  flex-grow: 1;
  padding: 8px 16px;
  margin-right: 10px;
  border: none;
  border-radius: 20px;
  outline: none;
}

.input-area button {
  padding: 8px 16px;
  background-color: #2979ff;
  color: #ffffff;
  border: none;
  border-radius: 20px;
  cursor: pointer;
  outline: none;
  transition: background-color 0.3s;
}

.input-area button:hover {
  background-color: #1864ab;
}

</style>
