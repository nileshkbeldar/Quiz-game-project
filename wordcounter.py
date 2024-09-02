def count_words(text):
    """
    This function takes a string of text as input and returns the number of words.
    """
    # Splitting the text by spaces to count the words
    words = text.split()
    return len(words)

def main():
    print("Welcome to the Word Counter Program!")
    
    # Taking user input
    user_input = input("Please enter a sentence or paragraph: ").strip()
    
    # Error handling for empty input
    if not user_input:
        print("Error: The input cannot be empty. Please try again.")
    else:
        # Counting the words in the user input
        word_count = count_words(user_input)
        
        # Displaying the result
        print(f"The number of words in the input text is: {word_count}")

if __name__ == "__main__":
    main()
