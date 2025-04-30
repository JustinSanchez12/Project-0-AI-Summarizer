from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_community.chat_models import ChatOllama

app = FastAPI()

# Allow local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the LLM
llm = ChatOllama(
    model="gemma3:4b",
    temperature=0.7,
)

class TextInput(BaseModel):
    text: str

@app.post("/summarize")
async def summarize(data: TextInput):
    try:
        # Create a prompt for summarization
        prompt = f"Summarize the following text in 1-2 paragraphs:\n\n{data.text}"
        
        # Get the summary from the LLM
        response = llm.invoke(prompt)
        
        # Extract the content from the response
        summary = response.content if hasattr(response, 'content') else str(response)
        
        return {"summary": summary}
    except Exception as e:
        return {"summary": f"Error: {str(e)}"}
