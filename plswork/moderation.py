from transformers import pipeline

pipe = pipeline("text2text-generation", model="abhiai/ModerationGPT")

print(pipe("Hello world!")[0]['generated_text'])
print(pipe("fuck you")[0]['generated_text'])