"""A deliberately simple, local-only password phrase discussion exercise."""

sample_phrase = input("Type a sample phrase (not a real password): ")
has_letters = any(character.isalpha() for character in sample_phrase)
has_digits = any(character.isdigit() for character in sample_phrase)
is_long_enough = len(sample_phrase) >= 12

print("Sample length:", len(sample_phrase))
print("Contains letters:", has_letters)
print("Contains digits:", has_digits)
print("At least 12 characters:", is_long_enough)
print("This toy check is not a password security guarantee.")
