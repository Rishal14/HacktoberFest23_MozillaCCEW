def max_words(sentences):
    max_word_count = 0
    for sentence in sentences:
        words = sentence.split()
        max_word_count = max(max_word_count, len(words))
    return max_word_count

# Example usage:
sentences = ["This is an example", "Another sentence", "Yet another example sentence"]
result = max_words(sentences)
print(result)  # Output will be 4
