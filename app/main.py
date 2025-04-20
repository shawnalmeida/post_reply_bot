from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import ReplyRequest, ReplyResponse
from app.generator import generate_reply
from app.database import save_to_db

app = FastAPI(title="Social Media Reply Generator")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/reply", response_model=ReplyResponse)
def generate_human_like_reply(request: ReplyRequest):
    try:
        reply = generate_reply(request.platform, request.post_text)
        save_to_db(request.platform, request.post_text, reply)
        return {"generated_reply": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    return {"message": "Welcome to the Social Media Reply Generator API. Use the /reply endpoint with POST."}
    
