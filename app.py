from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

import final_nlp_model

app = FastAPI()

# CORS middleware to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print("Starting")

class TextInput(BaseModel):
    text: str

@app.post("/ai")
def intake_process_text(text_input: TextInput):
    # Retrieve text input from frontend and feed it to NLP model
    input_text = text_input.text
    print(input_text, "text")
    keywords = final_nlp_model.keywords(input_text)
    print(keywords, "text")

    # Takes extracted keywords and returns them
    return {"status": "Saved query and keywords", "keywords": keywords}

# Use the PORT environment variable or default to 8080
port = int(os.getenv("PORT", 8080))

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=port)
