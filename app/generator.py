import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from transformers import pipeline as hf_pipeline

quantization_config = BitsAndBytesConfig(load_in_4bit=True)

# Model selection
model_id = "google/gemma-2b"
device = 0 if torch.cuda.is_available() else -1

# Load model + tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto", quantization_config=quantization_config)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer, torch_dtype=torch.bfloat16)

# Sentiment analysis pipeline
sentiment_analyzer = hf_pipeline("sentiment-analysis", device=device)

# Tone templates by platform
tone_prompts = {
    "Twitter": "Witty and concise",
    "LinkedIn": "Professional and insightful",
    "Instagram": "Friendly, casual, and upbeat",
}

def generate_reply(platform: str, post_text: str) -> str:
    tone = tone_prompts.get(platform, "Friendly and helpful")

    # Detect sentiment of the post
    try:
        sentiment = sentiment_analyzer(post_text)[0]['label']
    except Exception:
        sentiment = "Neutral"  # Fallback sentiment

    # Sophisticated structured prompt
    prompt = (
        f"You are an assistant that writes natural, human-like replies to social media posts.\n"
        f"Platform: {platform}\n"
        f"Tone: {tone}\n"
        f"Sentiment of the post: {sentiment}\n"
        f"Original Post: \"{post_text}\"\n"
        f"Write a relevant, friendly reply:"
    )

    # Generate reply
    response = generator(
        prompt,
        max_new_tokens=80,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        pad_token_id=tokenizer.eos_token_id  
    )

    # Extract and clean the reply
    generated_text = response[0]['generated_text']
    reply = generated_text.replace(prompt, "").strip().split("\n")[0]
    reply = reply.encode('utf-8').decode('unicode_escape')

    return reply