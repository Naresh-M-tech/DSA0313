from transformers import pipeline

translator = pipeline("translation_en_to_fr")

text = "Natural language processing is amazing"
translation = translator(text)

print("Original:", text)
print("French Translation:", translation[0]['translation_text'])
