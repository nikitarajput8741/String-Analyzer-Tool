class StringAnalyzer:
    def __init__(self, input_string):
        self.input_string = input_string.strip()
        if not self.input_string:
            raise ValueError("Input string cannot be empty.")

    def character_count(self):
        return len(self.input_string)

    def word_count(self):
        words = self.input_string.split()
        return len(words)

    def vowel_consonant_count(self):
        vowels = "aeiouAEIOU"
        vowel_count = sum(1 for char in self.input_string if char in vowels)
        consonant_count = sum(1 for char in self.input_string if char.isalpha() and char not in vowels)
        return vowel_count, consonant_count

    def is_palindrome(self):
        cleaned = ''.join(char.lower() for char in self.input_string if char.isalnum())
        return cleaned == cleaned[::-1]

    def character_frequency(self):
        freq = {}
        for char in self.input_string:
            if char.isalpha():
                char = char.lower()
                freq[char] = freq.get(char, 0) + 1
        return freq

    def average_word_length(self):
        words = self.input_string.split()
        if not words:
            return 0
        return sum(len(word) for word in words) / len(words)

    def analyze(self):
        return {
            "Character Count": self.character_count(),
            "Word Count": self.word_count(),
            "Vowels": self.vowel_consonant_count()[0],
            "Consonants": self.vowel_consonant_count()[1],
            "Is Palindrome": self.is_palindrome(),
            "Character Frequency": self.character_frequency(),
            "Average Word Length": round(self.average_word_length(), 2)
        }

# Example usage
if __name__ == "__main__":
    sample_string = "Hello, World! This is a test string."
    analyzer = StringAnalyzer(sample_string)
    results = analyzer.analyze()
    for key, value in results.items():
        print(f"{key}: {value}")