# task4: Chatbot Project 💬

This project is a simple command-line chatbot application using OpenAI's GPT-3.5-turbo model. It allows users to interact with a chatbot through a terminal, providing responses based on user input. The application can be run in testing mode using a mock response or with the real OpenAI API.
![Chatbotterm](https://github.com/user-attachments/assets/c85fc533-0953-425b-ba4d-1803fe98d5e5)

## Table of Contents ⚙️
- [Project Description](#project-description)
- [Technologies Used](#technologies-used)
- [Code Explanation](#code-explanation)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Features](#features)

## Project Description 📝
The Chatbot Project provides an interactive command-line interface where users can engage in a conversation with a chatbot powered by OpenAI's GPT-3.5-turbo model. Users can type their queries, and the chatbot responds with relevant answers.


The application can operate in two modes:
1. **Real Mode**: Uses the actual OpenAI API to generate responses.
2. **Mock Mode**: Uses a mock response for testing purposes without making real API calls.

## Technologies Used 🔧

- **Python**: The programming language used for implementing the chatbot.
- **OpenAI API**: Provides the chatbot functionality via GPT-3.5-turbo.
- **Mock Class**: A simulated version of the OpenAI API for testing.

## Code Explanation 👩🏻‍🏫

### `main.py`

- **Imports**: Imports required modules (`os` and `openai`).
- **MockOpenAI Class**: A mock class used for testing without actual API calls.
- **get_api_key Function**: Reads the API key from a file named `API_KEY`.
- **chat_with_openai Function**: Sends user input to the OpenAI API and retrieves the response.
- **main Function**: Provides a command-line interface for users to interact with the chatbot.

## Installation 🗺️

1. **Clone the repository**:
    ```sh
    git clone https://github.com/sadeemAhmed/chatbot-project.git
    cd chatbot-project
    ```

2. **Set up a virtual environment** (optional but recommended):
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install openai
    ```

4. **Create the API key file**:
    - Create a file named `API_KEY` in the project directory.
    - Paste your OpenAI API key into this file and save it.

## Usage 🤖

1. **Run the chatbot**:
    ```sh
    python main.py
    ```

2. **Interact with the chatbot**:
    - Type your queries at the prompt.
    - Type `exit` to end the conversation.

3. **Testing Mode**:
    - Set the environment variable `USE_MOCK` to `"true"` to use the mock response:
      ```sh
      export USE_MOCK=true  # On Windows use `set USE_MOCK=true`
      ```

## File Structure 🏗️
chatbot-project


- `main.py`: The main script containing the chatbot logic.
- `API_KEY`: A file containing your OpenAI API key.
- `README.md`: This file, containing information about the project.

## ⭐️ Features ⭐️

- **Interactive Chat**: Engage in a conversation with the chatbot.
- **Real and Mock Modes**: Test with actual API calls or a mock response.
- **Easy Setup**: Simple installation and configuration.

Made with love by "She Codes Team" 🤍😄
Raghad Alshammari - Sadeem Alresaini - Razan Alothaim.

