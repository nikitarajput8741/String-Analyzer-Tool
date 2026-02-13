import re

def analyze_string(text):
    if not text.strip():
        return "The input is empty. Please provide some text!"

    # Basic Metrics
    char_count_with_spaces = len(text)
    char_count_no_spaces = len(text.replace(" ", ""))
    words = text.split()
    word_count = len(words)
    sentences = re.split(r'[.!?]+', text)
    sentence_count = len([s for s in sentences if s.strip()])
    
    # Calculations
    avg_word_length = sum(len(word) for word in words) / word_count if word_count > 0 else 0
    
    # Advanced Features
    unique_words = len(set(word.lower().strip(".,!?") for word in words))
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in text if char in vowels)
    consonant_count = sum(1 for char in text if char.isalpha() and char not in vowels)

    # Report Generation
    print("\n" + "="*30)
    print("      STRING ANALYSIS      ")
    print("="*30)
    print(f"Total Characters  : {char_count_with_spaces}")
    print(f"Chars (no spaces) : {char_count_no_spaces}")
    print(f"Word Count        : {word_count}")
    print(f"Unique Words      : {unique_words}")
    print(f"Sentence Count    : {sentence_count}")
    print(f"Avg Word Length   : {avg_word_length:.2f}")
    print(f"Vowels/Consonants : {vowel_count}/{consonant_count}")
    print("-" * 30)
    print(f"Reversed Text (Preview): {text[::-1][:50]}...")
    print("="*30)

# User Input
if __name__ == "__main__":
    user_input = input("Enter the text you want to analyze: ")
    analyze_string(user_input) 