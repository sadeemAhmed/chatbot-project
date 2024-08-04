import os
import openai

# Mock OpenAI class for testing without API calls
class MockOpenAI:
    class ChatCompletion:
        @staticmethod
        def create(model, messages):
            return MockResponse()

class MockResponse:
    class Choice:
        def __init__(self, message):
            self.message = message
    def __init__(self):
        self.choices = [self.Choice({"role": "assistant", "content": "This is a mocked response."})]

# Use the real OpenAI client or the mock depending on environment
use_mock = os.getenv("USE_MOCK", "true").lower() == "true"
openai = MockOpenAI() if use_mock else openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_openai(prompt):
    try:
        # Create a chat completion request
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "What is the capital city of Saudi Arabia?"},
                {"role": "user", "content": "How many people are on the Earth?"},
            ]
        )
        # Access and return the response content directly
        return completion.choices[0].message["content"].strip()
    except Exception as e:
        # Print any error that occurs
        print(f"An error occurred: {e}")
        return None

# Main loop for the chatbot
def main():
    print("Chatbot is ready. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = chat_with_openai(user_input)
        if response:
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
