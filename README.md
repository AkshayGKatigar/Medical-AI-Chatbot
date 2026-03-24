# Medical-AI-Chatbot

## Project Overview

The Medical AI Chatbot is designed to assist users in getting quick medical information when a doctor may not be immediately available.

The main intention behind building this project is simple:

“A doctor may not always be available, but basic guidance should be.”

This chatbot allows users to ask medical-related questions and receive helpful responses based on available knowledge.

This chatbot is trained using a medical book and retrieves relevant information to answer user queries.

While it does not replace professional medical advice, it helps users:

- Understand possible health conditions.
- Get quick medical insights.
- Make better decisions for themselves or their family.

## Features
- Interactive chat interface.
- AI responses based on medical knowledge.
- Retrieval-Augmented Generation(Rag).
- Answers fetched from a trained medical dataset(book).
- Fast and responsive UI.

## How It Works (RAG Architecture)
- User asks a question
- The system searches relevant content from the medical book
- Retrieved context is passed to the AI model
- AI generates a response based on that context

# Tech Stack
## Frontend
- React
## Backend
- FastAPI
## AI & Data
- Ollama (Local LLM)
- LangChain (RAG pipeline)
- Pinecone (Vector Database for storing embeddings)






