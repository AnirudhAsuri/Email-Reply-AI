# 📧 Email-Reply-AI

An intelligent assistant to help you craft professional email replies in seconds.

***

### Table of Contents
* [About The Project](#about-the-project)
* [Screenshot](#screenshot)
* [Key Features](#key-features)
* [Tech Stack](#tech-stack)
* [Getting Started](#getting-started)
* [Usage](#usage)

***

## About The Project

Drafting professional, well-structured email replies can be time-consuming. **Email-Reply-AI** is a tool designed to solve this problem. By pasting the content of an email you've received and providing a simple instruction (e.g., "politely decline" or "accept the invitation"), the system leverages a powerful Large Language Model (LLM) to generate a context-aware, polished, and ready-to-send reply. This project saves users valuable time and mental energy.

***

## Screenshot

<img width="2163" height="1691" alt="image" src="https://github.com/user-attachments/assets/3826837f-3e2d-4744-a7c6-04eada88df6b" />

***

## Key Features

* **Context-Aware Generation:** The AI understands the original email to craft relevant replies.
* **Instruction-Based Control:** Guide the AI with simple prompts to get the exact response you need.
* **Simple Web Interface:** A clean and intuitive UI built for ease of use.
* **One-Click Copy:** Instantly copy the generated reply to your clipboard.

***

## Tech Stack

* **Backend:** Python
* **Frontend:** Streamlit
* **LLM Provider:** Groq API / OpenAI API
* **Environment Management:** python-dotenv

***

## Getting Started

Follow these instructions to get a local copy of the project set up and running.

### Prerequisites

* Python 3.9+
* Git

### Installation

1.  **Clone the repository** to your local machine.
    ```sh
    git clone [https://github.com/AnirudhAsuri/Email-Reply-AI.git](https://github.com/AnirudhAsuri/Email-Reply-AI.git)
    cd Email-Reply-AI
    ```

2.  **Create and activate a virtual environment.**
    * For macOS/Linux:
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```
    * For Windows:
        ```sh
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install the required packages.**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Set up your environment variables.**
    * Create a file named `.env` by copying the example file.
    * Add your API key to the `.env` file:
        ```env
        API_KEY="YourSecretApiKeyHere"
        ```

***

## Usage

To start the application, run the following command in your terminal:
```sh
streamlit run app.py
