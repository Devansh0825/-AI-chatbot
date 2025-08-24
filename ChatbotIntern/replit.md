# Overview

This is an Internship FAQ Chatbot application built with Flask that helps students and job seekers get answers to common questions about internships. The chatbot uses OpenAI's GPT-5 model to provide intelligent, contextual responses and maintains a structured knowledge base of frequently asked questions about internship applications, requirements, timelines, compensation, and more.

The application features a web-based chat interface with a sidebar containing quick-access FAQ topics, real-time messaging, and conversation context management. Users can ask questions naturally or click on predefined topics to get instant answers about the internship process.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture
- **Framework**: Vanilla JavaScript with Bootstrap 5 for responsive UI components
- **Design Pattern**: Single-page application with real-time chat interface
- **User Interface**: Two-column layout with FAQ topic sidebar and main chat area
- **Styling**: Custom CSS with gradient backgrounds and modern chat bubble design
- **Interactivity**: Event-driven JavaScript for message handling and API communication

## Backend Architecture
- **Framework**: Flask (Python) serving as a lightweight web server
- **Application Structure**: Modular design with separate components for chatbot logic and knowledge base
- **API Design**: RESTful endpoints for chat interactions and conversation management
- **Error Handling**: Comprehensive exception handling with fallback responses
- **Context Management**: Conversation history tracking with message limit (10 messages) to manage memory

## Chatbot Intelligence
- **AI Integration**: OpenAI GPT-5 model for natural language processing and response generation
- **Intent Classification**: Confidence-based intent detection to determine response strategy
- **Knowledge Base**: Structured FAQ system with categorized topics and predefined responses
- **Fallback Strategy**: Graceful degradation when intent confidence is low or errors occur

## Data Architecture
- **Knowledge Storage**: In-memory dictionary structure organizing FAQ data by categories
- **Session Management**: Temporary conversation context storage without persistent database
- **Response Format**: Structured JSON responses including intent classification and confidence scores

# External Dependencies

## AI Services
- **OpenAI API**: GPT-5 model integration for natural language understanding and response generation
- **Authentication**: API key-based authentication for OpenAI services

## Frontend Libraries
- **Bootstrap 5.1.3**: CSS framework for responsive design and UI components
- **Font Awesome 6.0.0**: Icon library for visual elements and navigation

## Python Packages
- **Flask**: Web framework for handling HTTP requests and serving the application
- **OpenAI Python Client**: Official library for interacting with OpenAI's API

## Development Environment
- **Hosting**: Configured for Replit deployment with host='0.0.0.0' and port=5000
- **Debug Mode**: Enabled for development with automatic reload on code changes