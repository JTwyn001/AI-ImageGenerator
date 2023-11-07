import openai
import os
import customtkinter as ctk
import tkinter


def generate():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    user_prompt = "cat wearing a hat"

    response = openai.Image.create(
        prompt=user_prompt,
        n=1,
        size="512x512"
    )

    image_url = response['data'][0]['url']
    print(image_url)
