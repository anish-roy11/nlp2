import nltk
from nltk.corpus import brown, stopwords

# Download the Brown corpus and stopwords if not already downloaded
nltk.download('brown')
nltk.download('stopwords')

# Load the Brown corpus and stopwords
brown_words = [word.lower() for word in brown.words() if word.isalpha()]
stop_words = set(stopwords.words('english'))

# Function to calculate the probability of a word following W1 in a 2-gram language model
def calculate_next_word_probability(W1, word):
    #print("inside calculate_next_word_probability")
    bigrams = nltk.bigrams(brown_words)
    filtered_bigrams = [(w1, w2) for w1, w2 in bigrams if w1 == W1]
    total_bigrams = len(filtered_bigrams)
    word_count = sum(1 for w1, w2 in filtered_bigrams if w2 == word)
    probability = word_count / total_bigrams if total_bigrams > 0 else 0
    return probability

# Function to display the menu of top 3 most likely words to follow W1
def display_menu(W1):
    print("inside display_menu")
    word_probabilities = [(word, calculate_next_word_probability(W1, word)) for word in set(brown_words)]
    sorted_words = sorted(word_probabilities, key=lambda x: x[1], reverse=True)[:3]
    print(f"\nWhich word should follow '{W1}':")
    for i, (word, probability) in enumerate(sorted_words, 1):
        print(f"{i})\t{word}\tP({W1} {word}) = {probability:.2f}")
    print("4) QUIT")

flag=True
# Step 1: Ask the user for initial word/token W1
while (flag==True):
    W1 = input("Enter the initial word/token (W1): ").lower()
    if W1 != 'quit' and W1 in brown_words:
        print("W1 is in brown_words")
        flag=True
        break
    elif W1 == 'quit':
        print("W1 is not in brown_words")
        flag=False
        exit()
    else:
        print("Word not found in the corpus. Please try again or type 'quit' to exit.")
        flag=True

# Step 2: Display the menu and continue asking for next words until the user quits
sentence = [W1]
while (flag==True):
    display_menu(W1)
    choice = input("Enter your choice (1-3) or 'quit' to exit: ").lower()
    if choice == 'quit':
        break
    elif choice.isdigit() and 1 <= int(choice) <= 3:
        #next_word = sorted_words[int(choice) - 1][0]
        next_word = choice
        sentence.append(next_word)
        W1 = next_word
    else:
        #next_word = sorted_words[0][0]  # Assume user choice is 1 if invalid choice is entered
        next_word = choice
        sentence.append(next_word)
        W1 = next_word

# Display the final sentence
print("Generated sentence:", ' '.join(sentence))
