# Central Park & LGA Transport Assistant Agent

This project demonstrates a conversational AI agent built using the Google Agent Development Kit (ADK). The agent is designed primarily to answer questions about Central Park in New York City, using information grounded in a Vertex AI Search data store. It also features a sub-agent specialized in answering questions about public transportation to LaGuardia Airport (LGA), leveraging another Vertex AI Search data store. The main agent delegates non-Central Park questions to the appropriate sub-agent.

## Features

* Answers user questions about Central Park using Retrieval-Augmented Generation (RAG) via Vertex AI Search.
* Answers user questions about public transport options to LGA airport using RAG via Vertex AI Search.
* Demonstrates agent delegation: the main "root" agent routes specific queries to a specialized "search" agent.
* Utilizes Google's Gemini model so that you can interact with Gemini using Voice (`gemini-2.0-flash-live-preview-04-09`).
* Built with the  capabilities of the Google ADK.
