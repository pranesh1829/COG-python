from collections import Counter
import string

def count_word_occurrences(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read().lower()
            text = text.translate(str.maketrans("", "", string.punctuation))
            word_list = text.split()
            word_count = Counter(word_list)

            return word_count

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

def display_word_counts(word_count):
    if word_count:
        print("Word Occurrences:")
        for word, count in sorted(word_count.items()):
            print(f"{word}: {count}")
    else:
        print("No word occurrences to display.")

def main():
    try:
        file_path = input("Enter the path to the text file: ")
        word_count = count_word_occurrences(file_path)
        display_word_counts(word_count)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
