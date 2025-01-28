import openai

# Function to generate images from text using OpenAI's DALL·E
def generate_image_from_text(text):
    openai.api_key = "your_openai_api_key"
    response = openai.Image.create(
        prompt=text,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url

# Example usage
text =input()
image_url = generate_image_from_text(text)
print(f"Generated Image URL: {image_url}")
