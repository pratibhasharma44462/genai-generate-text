from transformers import pipeline, set_seed

# Create text generation pipeline
generator = pipeline('text-generation', model='gpt2')
set_seed(42)

# Generate text
output = generator(
    "Once upon a time",
    max_length=80,
    num_return_sequences=1,
    temperature=0.8,
    top_k=50,
    top_p=0.9
)

print("Generated Text:\n")
print(output[0]['generated_text'])