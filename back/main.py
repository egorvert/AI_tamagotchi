from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
from typing import Optional
import uvicorn


# Response model
class GenerationResponse(BaseModel):
    prompt: str
    generated_text: str

# Request model
class GenerationRequest(BaseModel):
    prompt: str
    max_length: Optional[int] = 100

app = FastAPI(
    title="LLM Generation API",
    description="API for text generation using TinyLlama"
)

# Initialize LLM
generator = None

def setup_llm():
    global generator
    generator = pipeline('text-generation', model='TinyLlama/TinyLlama-1.1B-Chat-v1.0')

def generate_response(prompt, max_length=100):
    if generator is None:
        setup_llm()
    result = generator(prompt, max_length=max_length, num_return_sequences=1)
    return result[0]['generated_text']

@app.on_event("startup")
async def startup_event():
    setup_llm()

@app.post("/generate", response_model=GenerationResponse)
async def generate(request: GenerationRequest):
    try:
        generated_text = generate_response(request.prompt, request.max_length)
        return GenerationResponse(
            prompt=request.prompt,
            generated_text=generated_text
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
import requests
def download_image(prompt, width=768, height=768, model='flux'):
    url = f"https://image.pollinations.ai/prompt/{prompt}?width={width}&height={height}&model={model}"
    response = requests.get(url)
    if response.status_code == 200:
        with open('tamagotchi.jpg', 'wb') as file:
            file.write(response.content)
        print('Image downloaded as tamagotchi.jpg!')
    else:
        print('Error:', response.status_code)

# Example usage
# download_image("a singular, 16 bit, pixelated, simple, black tamagotchi cat in a very sad expression with a white background")
# download_image("a singular, 16 bit, pixelated, black and white, simple, tamagotchi penguin in an idle expression with eyes open with a white background, no shadows or colours")
download_image("a singular, 16 bit, pixelated, simple, tamagotchi lion in a smily expression with a white background")