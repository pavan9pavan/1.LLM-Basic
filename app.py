import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Set your Google API Key (replace with your actual key or use environment variable)
google_api_key = "aSyAQYcnI0Gj8T8IlgbzJtMgFru8hK6Q06qU"  # REMOVE FOR ACTUAL CODE

# Initialize the Gemini Pro LLM
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=google_api_key)

# Define a prompt template
prompt_template = PromptTemplate.from_template(
    "Answer the following question:\n\n{question}\n\n"
)

# Create an LLM Chain
llm_chain = LLMChain(llm=llm, prompt=prompt_template)

# Simple chatbot interaction loop
if __name__ == "__main__":
    while True:
        user_question = input("You: ")
        if user_question.lower() in ["exit", "quit", "bye"]:
            print("Goodbye!")
            break
        try:
          response = llm_chain.run(question=user_question)
          print(f"Bot: {response}")
        except Exception as e:
          print(f"Error: {e}")   
)