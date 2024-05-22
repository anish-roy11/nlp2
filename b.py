


import nltk
from nltk.corpus import brown

# Download the Brown corpus if not already downloaded
nltk.download('brown')

# Step 1: Ask the user to enter a sentence S
sentenceEntered = input("Enter a sentence: ")
print("sentenceEntered=", sentenceEntered)

# Step 2: Apply lowercasing to the sentence
sentence = sentenceEntered.lower()

# Step 3: Calculate P(S) assuming a 2-gram language model
# Load the Brown corpus and tokenize it
brown_words = brown.words()
brown_words_lower = [word.lower() for word in brown_words]  # Lowercase all words



bigrams = nltk.bigrams(brown_words_lower)

# Calculate the frequency of each bigram
bigram_freq = nltk.FreqDist(bigrams)

# Calculate the probability of each bigram
total_bigrams = sum(bigram_freq.values())
probability_start_end = 0.25  # Probability of starting or ending a sentence
probability_sentence = 1

# Tokenize the input sentence
sentence_tokens = nltk.word_tokenize(sentence)

# Add start and end tokens to the sentence
sentence_tokens = ['<s>'] + sentence_tokens + ['</s>']

for i in range(1, len(sentence_tokens)):
    # Calculate the probability of the bigram in the sentence
    bigram = (sentence_tokens[i-1], sentence_tokens[i])
    if(sentence_tokens[i-1].startswith('<s>') | sentence_tokens[i].endswith('</s>')):
        probability_bigram=0.25
    else:
        probability_bigram = bigram_freq[bigram] / total_bigrams if bigram in bigram_freq else 0
    
    probability_sentence *= probability_bigram
    print("bigram=",bigram)
    print("probability_bigram=",probability_bigram)
    print("probability_sentence=",probability_sentence)


# Multiply by the probability of starting or ending a sentence
# probability_sentence *= probability_start_end

# Display the calculated probability
print("Probability of the sentence using a 2-gram language model:", probability_sentence)






# Enter a sentence: The grand jury took a swipe at the State Welfare Department
# sentenceEntered= The grand jury took a swipe at the State Welfare Department
# bigram= ('<s>', 'the')
# probability_bigram= 0.25
# probability_sentence= 0.25
# bigram= ('the', 'grand')
# probability_bigram= 1.722369532660863e-05
# probability_sentence= 4.305923831652157e-06
# bigram= ('grand', 'jury')
# probability_bigram= 8.611847663304314e-06
# probability_sentence= 3.708196008797999e-11
# bigram= ('jury', 'took')
# probability_bigram= 8.611847663304314e-07
# probability_sentence= 3.193441913344143e-17
# bigram= ('took', 'a')
# probability_bigram= 3.703094495220855e-05
# probability_sentence= 1.1825617170112252e-21
# bigram= ('a', 'swipe')
# probability_bigram= 1.7223695326608628e-06
# probability_sentence= 2.0368082718712513e-27
# bigram= ('swipe', 'at')
# probability_bigram= 1.7223695326608628e-06
# probability_sentence= 3.508136511342667e-33
# bigram= ('at', 'the')
# probability_bigram= 0.001425260788276864
# probability_sentence= 5.0000094095390964e-36
# bigram= ('the', 'state')
# probability_bigram= 0.0002333810716755469
# probability_sentence= 1.1669075543860529e-39
# bigram= ('state', 'welfare')
# probability_bigram= 1.7223695326608628e-06
# probability_sentence= 2.009846019106336e-45
# bigram= ('welfare', 'department')
# probability_bigram= 8.611847663304314e-07
# probability_sentence= 1.7308487743242378e-51
# bigram= ('department', '</s>')
# probability_bigram= 0.25
# probability_sentence= 4.3271219358105944e-52
# Probability of the sentence using a 2-gram language model: 4.3271219358105944e-52






#####(4)Display the sentence S, list all the individual bigrams and their probabilities, and the final probability P(S) on screen. It is fine if it is zero.

print("============================================")
print("sentenceEntered=", sentenceEntered)

# Step 4: Display the sentence, individual bigrams and their probabilities, and the final probability P(S)
sentence = sentenceEntered.lower()


brown_words = brown.words()
brown_words_lower = [word.lower() for word in brown_words]  # Lowercase all words
bigrams = nltk.bigrams(brown_words_lower)

# Calculate the frequency of each bigram
bigram_freq = nltk.FreqDist(bigrams)

# Calculate the probability of each bigram
total_bigrams = sum(bigram_freq.values())
bigram_probabilities = {bigram: (count / total_bigrams) for bigram, count in bigram_freq.items()}


print("\nSentence:", sentence)
print("\nIndividual Bigrams and their Probabilities:")
sentence_bigrams = list(nltk.bigrams(sentence.split()))
probability_sentence = 1
for bigram in sentence_bigrams:
    bigram_lower = (bigram[0].lower(), bigram[1].lower())  # Lowercase the bigram
    probability = bigram_probabilities.get(bigram_lower, 0)
    print(f"{bigram}: {probability}")
    probability_sentence *= probability

# Calculate P(S)
#probability_sentence *= 0.25  # Probability of starting or ending a sentence
print("\nProbability P(S):", probability_sentence)








# Individual Bigrams and their Probabilities:
# ('the', 'grand'): 1.722369532660863e-05
# ('grand', 'jury'): 8.611847663304314e-06
# ('jury', 'took'): 8.611847663304314e-07
# ('took', 'a'): 3.703094495220855e-05
# ('a', 'swipe'): 1.7223695326608628e-06
# ('swipe', 'at'): 1.7223695326608628e-06
# ('at', 'the'): 0.001425260788276864
# ('the', 'state'): 0.0002333810716755469
# ('state', 'welfare'): 1.7223695326608628e-06
# ('welfare', 'department'): 8.611847663304314e-07

# Probability P(S): 1.7308487743242378e-51





