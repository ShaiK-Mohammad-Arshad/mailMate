import streamlit as st
from transformers import pipeline

# Initialize the text generation pipeline with a Hugging Face email generation model
generator = pipeline(
    "text-generation",
    model="pszemraj/opt-125m-email-generation",
    use_fast=False,
    do_sample=False
)

def generate_email_response(email_text, tone):
    prompt = f"Reply to the following email in a {tone.lower()} tone:\n\n{email_text}\n\nReply:"
    outputs = generator(prompt, max_length=150, num_return_sequences=1)
    return outputs[0]['generated_text']