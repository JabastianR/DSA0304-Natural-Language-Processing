C_data = 3
C_data_science = 3

probability = C_data_science / C_data

print("MLE of P(science | data)")
print("P(science | data) =", probability)

if probability == 1:
    print("Interpretation: Science always follows data in this corpus.")
