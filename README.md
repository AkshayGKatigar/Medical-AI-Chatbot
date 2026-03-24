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

# Setup Instructions
## 1. Clone Repository
git clone https: https://github.com/AkshayGKatigar/Medical-AI-Chatbot
cd Medical-AI-Chatbot
## 2. Install Dependencies
pip install -r requirements.txt
## 3. Run Backend
uvicorn app.main:app --reload
## 4. Run Frontend
npm install
npm run dev

# Disclaimer

This project is built for educational purposes only.
- It does not provide medical diagnosis
- It is not a substitute for professional healthcare
- Always consult a doctor for serious medical conditions

# Goal of the Project

- To build a real-world AI application
- To implement RAG (Retrieval-Augmented Generation)
- To explore AI in healthcare domain
