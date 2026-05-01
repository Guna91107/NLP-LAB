from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

prompt = input("Enter prompt: ")

response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

print(response.output[0].content[0].text)