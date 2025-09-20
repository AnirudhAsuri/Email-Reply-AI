# Overview

Smart Office Assistant is a complete Flask web application that helps users draft professional email replies using AI. The application takes an original email, key points for the response, and desired tone as input, then constructs a detailed prompt and uses the Groq API with the llama3-8b-8192 model to generate a polished, professional email reply. The system features a clean, modern interface with a responsive two-column layout for input and output display, complete with copy-to-clipboard functionality and robust error handling.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture
- **Single-page application** using Flask's template rendering with Jinja2
- **Two-column grid layout** separating input forms from output display
- **Responsive design** with modern CSS styling using Roboto font family
- **Form-based interaction** with server-side processing and page refresh for results

## Backend Architecture
- **Flask web framework** serving as the main application server
- **Route-based request handling** with a single endpoint (`/`) handling both GET and POST requests
- **Server-side form processing** with input validation and error handling
- **Template rendering** for dynamic content display with user input persistence

## AI Integration
- **Groq API integration** using the official groq Python library
- **llama3-8b-8192 model** for email reply generation
- **Prompt engineering** system that constructs detailed prompts from user inputs
- **Structured prompt template** combining original email, key points, and tone specifications

## Configuration Management
- **Environment variable configuration** using python-dotenv for local development
- **Replit Secrets integration** for secure API key storage in production
- **Error handling** for missing API keys with informative error messages

## Input Processing
- **Multi-input form system** accepting original email text, reply key points, and tone selection
- **Input validation** ensuring required fields are provided before processing
- **Tone selection** from predefined options (Formal, Friendly & Casual, Direct & Concise, Apologetic)
- **Input persistence** maintaining user data across form submissions and errors

# External Dependencies

## AI Services
- **Groq API** - Primary AI service for email reply generation using llama3-8b-8192 model
- **API Key Authentication** - Requires GROQ_API_KEY environment variable

## Python Libraries
- **Flask 3.0.0** - Web framework for application server and routing
- **groq 0.4.1** - Official client library for Groq API integration
- **python-dotenv 1.0.0** - Environment variable management for development

## Frontend Assets
- **Google Fonts** - Roboto font family for typography
- **Custom CSS** - Self-contained styling without external CSS frameworks

## Deployment Platform
- **Replit** - Target deployment platform with integrated secrets management
- **Environment Variables** - GROQ_API_KEY stored in Replit Secrets for production security