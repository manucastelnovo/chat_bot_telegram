# Paraguayan Labor Code PDF Consumer and Telegram Bot

This repository contains a project that serves as a consumer for Paraguayan labor code PDFs, storing worker's labor code information in a vectorized database. Additionally, it connects to Telegram, allowing users to make requests via a Telegram bot. The bot performs semantic searches using Pineco and sends a prompt to OpenAI containing the context acquired from the semantic search, along with the user's question.

## Project Overview

The main objective of this project is to provide an automated solution for extracting and storing Paraguayan labor code information from PDF documents. The project consists of the following components:

- **PDF Consumer**: Extracts relevant data from Paraguayan labor code PDFs and stores the information in a vectorized database. This component ensures easy access to worker-related legal information.

- **Telegram Bot**: Interacts with users through a Telegram bot interface. Users can request specific labor code information by sending queries to the bot.

- **Semantic Search with Pineco**: When users make requests through the Telegram bot, the system uses Pineco for semantic search. This ensures that the context of the user's query is considered for accurate and relevant results.

- **OpenAI Integration**: After the semantic search, the bot sends a prompt to the OpenAI API. The prompt includes both the context acquired from Pineco's semantic search and the user's question. OpenAI generates responses based on the provided prompt.

