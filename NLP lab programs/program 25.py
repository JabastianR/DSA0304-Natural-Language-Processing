from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

response = client.responses.create(
    model="gpt-3.5-turbo",
    input="Write a short poem about AI."
)

print(response.output_text)