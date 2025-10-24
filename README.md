# Simple Q&A Chatbot 🤖

This is a straightforward little web app that lets you ask questions and get fast answers from an AI. It's built with **Streamlit** for the interface and uses the speedy **Groq API** (powered by **LangChain**) to do the heavy lifting.

## What it does

* Lets you ask any question in a simple text box.
* Connects to the Groq API for super-fast AI responses.
* Uses LangChain to structure the prompt and parse the output.
* Provides a sidebar to:
    * Enter your Groq API key securely.
    * Choose your preferred LLM (like `llama-3.3-70b-versatile`).
    * Adjust the AI's "creativity" (Temperature).
    * Set the maximum answer length (Max Tokens).

## How to Run It

1.  **Clone the Repository**
    ```bash
    git clone [https://your-repository-url.git](https://your-repository-url.git)
    cd your-repository-directory
    ```

2.  **Install Requirements**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set Up API Keys**
    Create a `.env` file in the folder and add your Groq API key:
    ```
    GROQ_API_KEY="gsk_YOUR_REAL_GROQ_KEY"
    ```
    *(You can also add `LANGCHAIN_API_KEY` for tracing.)*

4.  **Run the App**
    ```bash
    streamlit run app.py
    ```
    *(Replace `app.py` with the name of your Python file if it's different.)*

## How to Use the App

Once it's running, your web browser will open.

1.  Look at the sidebar on the left.
2.  Paste your **Groq API Key** into the top box. (The app won't work without this!)
3.  Type your question in the main chat box.
4.  Press Enter and wait a moment for your answer!
