import { useState, useEffect, useRef } from "react";
import { sendMessage } from "../services/api.js";
import avatar from "../assets/doctor.png";

export default function Home() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const chatRef = useRef(null);

  useEffect(() => {
    chatRef.current?.scrollTo({
      top: chatRef.current.scrollHeight,
      behavior: "smooth",
    });
  }, [messages]);

  const handleSend = async () => {
    if (!input) return;

    const userMsg = { role: "user", text: input };
    setMessages((prev) => [...prev, userMsg]);

    setInput("");

    setMessages((prev) => [...prev, { role: "bot", text: "Typing..." }]);

    const res = await sendMessage(input);

    setMessages((prev) => [
      ...prev.slice(0, -1),
      { role: "bot", text: res.response },
    ]);
  };

  return (
    <div style={styles.page}>
      <div style={styles.chatContainer}>
        {/* Header */}
        <div style={styles.header}>
          <img src={avatar} alt="avatar" style={styles.avatar} />

          <div style={styles.headerText}>
            <div style={styles.title}>AI Assistant</div>

            <div style={styles.statusRow}>
              <span style={styles.statusDot}></span>
              <span style={styles.statusText}>Online</span>
            </div>
          </div>
        </div>

        {/* Messages */}
        <div style={styles.messages} ref={chatRef}>
          {messages.map((msg, i) => (
            <div
              key={i}
              style={{
                ...styles.messageWrapper,
                justifyContent: msg.role === "user" ? "flex-end" : "flex-start",
              }}
            >
              <div
                style={{
                  ...styles.message,
                  background:
                    msg.role === "user"
                      ? "linear-gradient(135deg, #3b82f6, #2563eb)"
                      : "rgba(255,255,255,0.05)",
                  color: msg.role === "user" ? "white" : "#e2e8f0",
                }}
              >
                {msg.text}
              </div>
            </div>
          ))}
        </div>

        {/* Input */}
        <div style={styles.inputWrapper}>
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleSend()}
            placeholder="Type your message..."
            style={styles.input}
          />
          <button onClick={handleSend} style={styles.sendBtn}>
            ➤
          </button>
        </div>
      </div>
    </div>
  );
}

const styles = {
  page: {
    height: "100vh",
    background: "linear-gradient(135deg, #0f172a, #1e293b)",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
  },

  chatContainer: {
    width: "420px",
    height: "600px",
    background: "rgba(255,255,255,0.05)",
    borderRadius: "20px",
    backdropFilter: "blur(10px)",
    display: "flex",
    flexDirection: "column",
    justifyContent: "space-between",
    boxShadow: "0 10px 30px rgba(0,0,0,0.5)",
    padding: "15px",
  },

  header: {
    display: "flex",
    alignItems: "center",
    gap: "12px",
    marginBottom: "10px",
  },

  headerText: {
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
  },

  avatar: {
    width: "45px",
    height: "45px",
    borderRadius: "50%",
    objectFit: "cover",
    border: "2px solid #3b82f6",
  },

  title: {
    fontWeight: "600",
    fontSize: "17px",
    marginBottom: "4px",
  },

  subtitle: {
    fontSize: "13px",
    color: "#94a3b8",
  },

  statusRow: {
    display: "flex",
    alignItems: "center",
    gap: "6px",
  },

  statusDot: {
    width: "8px",
    height: "8px",
    background: "#22c55e",
    borderRadius: "50%",
  },

  statusText: {
    fontSize: "12px",
    color: "#22c55e",
  },

  messages: {
    flex: 1,
    display: "flex",
    flexDirection: "column",
    gap: "12px",
    overflowY: "auto",
    padding: "10px",
  },

  messageWrapper: {
    display: "flex",
    width: "100%",
    padding: "4px 0",
  },

  message: {
    padding: "14px 18px",
    borderRadius: "16px",
    maxWidth: "60%",
    fontSize: "14px",
    lineHeight: "1.6",
    wordBreak: "break-word",
    textAlign: "left",
  },

  inputWrapper: {
    display: "flex",
    alignItems: "center",
    background: "#020617",
    borderRadius: "12px",
    padding: "8px",
  },

  input: {
    flex: 1,
    background: "transparent",
    border: "none",
    outline: "none",
    color: "white",
    padding: "8px",
  },

  sendBtn: {
    background: "#3b82f6",
    border: "none",
    borderRadius: "50%",
    width: "35px",
    height: "35px",
    color: "white",
    cursor: "pointer",
  },
};
