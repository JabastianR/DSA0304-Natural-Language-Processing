word = "improves"

trigram_probability = 0
bigram_probability = 0
unigram_probability = 0

print("Sequence: data science improves")

if trigram_probability == 0:
    print("Trigram is unseen.")
    
    if bigram_probability == 0:
        print("Bigram is also unseen.")
        
        if unigram_probability == 0:
            print("Unigram is also unseen.")
            print("Backoff probability =", unigram_probability)
