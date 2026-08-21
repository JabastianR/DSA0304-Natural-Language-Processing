

lambda1 = 0.5   
lambda2 = 0.3   
lambda3 = 0.2   
C_data_science_is = 2
C_data_science = 3

C_science_is = 2
C_science = 3

C_is = 2
total_words = 12

P_trigram = C_data_science_is / C_data_science
P_bigram = C_science_is / C_science
P_unigram = C_is / total_words

P_final = (
    lambda1 * P_trigram
    + lambda2 * P_bigram
    + lambda3 * P_unigram
)

print("Trigram probability =", P_trigram)
print("Bigram probability  =", P_bigram)
print("Unigram probability =", P_unigram)

print("Interpolated probability =", P_final)
