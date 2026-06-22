from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from llm_client import generate_response
from prompts import summarize_prompt,translate_prompt,rewrite_prompt

app = FastAPI(
    title="Text Summarization and Translation API"
)

@app.get("/")
async def root():
    return {"message": "TEXT SUMMARIZATION AND TRANSLATION"}


class Summary(BaseModel):
    text:str

class Translation(BaseModel):
    text:str
    lang:str

class Rewriting(BaseModel):
    text:str
    tone:str

@app.post("/summarize")
async def summarize(inp:Summary):
    summarized_text=generate_response(summarize_prompt(inp.text))
    return {"summary":summarized_text}



@app.post("/translate")
async def translate(inp:Translation):
    translated_text=generate_response(translate_prompt(inp.text,inp.lang))
    return {"translated_text":translated_text}



@app.post("/rewrite")
async def rewrite(inp:Rewriting):
    rewritten_text=generate_response(rewrite_prompt(inp.text,inp.tone))
    return {"rewritten_text":rewritten_text}

if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

   
