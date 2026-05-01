from transformers import pipeline

translator = pipeline(
    task="image-text-to-text",   
    model="Helsinki-NLP/opus-mt-en-fr"
)

text = input("Enter English text: ")

result = translator(text)

print("French:", result[0]['generated_text'])