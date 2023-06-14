import random
from mnemonic import Mnemonic

output_file = r"C:\Users\oluwa\OneDrive\Documents\my files\new compiliations.txt"  # Replace with the desired output file path
num_phrases = 1000000  # Number of sets of phrases to generate

def generate_seed_phrase():
    mnemo = Mnemonic("english")
    seed_phrase = mnemo.generate(strength=128)
    return seed_phrase

# Generate and store seed phrases in the output file
with open(output_file, "w") as file:
    for _ in range(num_phrases):
        seed_phrase = generate_seed_phrase()
        file.write(seed_phrase + "\n")
