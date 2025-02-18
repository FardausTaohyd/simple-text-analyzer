from collections import Counter

def word_frequency(text):
    """Counts occurrences of each word in a given text."""
    words = text.lower().split()  # Convert to lowercase and split words
    return dict(Counter(words))   # Use Counter for word count

def first_unique_word(text):
    """Finds the first unique word in a given text."""
    words = text.lower().split()
    count = Counter(words)  # Count occurrences
    for word in words:
        if count[word] == 1:
            return word
    return None  # If no unique word is found

def are_anagrams(word1, word2):
    """Checks if two words are anagrams."""
    return sorted(word1.lower()) == sorted(word2.lower())

def longest_unique_word(words):
    """Finds the longest word with all unique characters."""
    return max([word for word in words if len(set(word)) == len(word)], key=len, default="")

def main_menu():
    """Main function to interact with the user."""
    while True:
        print("\n🔹 Simple Text Analyzer 🔹")
        print("1️⃣ Word Frequency Counter")
        print("2️⃣ First Unique Word Finder")
        print("3️⃣ Anagram Checker")
        print("4️⃣ Longest Unique Character Word")
        print("5️⃣ Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            text = input("\nEnter a sentence: ")
            print("\n📊 Word Frequency:", word_frequency(text))

        elif choice == '2':
            text = input("\nEnter a sentence: ")
            result = first_unique_word(text)
            print("\n🟢 First Unique Word:", result if result else "No unique words found.")

        elif choice == '3':
            word1 = input("\nEnter first word: ")
            word2 = input("Enter second word: ")
            print("\n🔄 Are Anagrams?", are_anagrams(word1, word2))

        elif choice == '4':
            words = input("\nEnter words separated by space: ").split()
            print("\n📝 Longest Unique Character Word:", longest_unique_word(words))

        elif choice == '5':
            print("\n🚀 Exiting... Thank you for using Simple Text Analyzer!")
            break

        else:
            print("\n❌ Invalid choice. Please enter a number between 1-5.")

# Run the program
if __name__ == "__main__":
    main_menu()