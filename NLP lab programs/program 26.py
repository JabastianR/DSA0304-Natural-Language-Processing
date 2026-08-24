from transformers import pipeline

translator = pipeline("translation_en_to_fr")

text = "Machine Learning is very useful."

result = translator(text)

print(result[0]["translation_text"])