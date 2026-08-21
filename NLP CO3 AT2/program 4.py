import math

P_is = 0.66
P_drives = 0.33

total = P_is + P_drives

P_is = P_is / total
P_drives = P_drives / total

entropy = -(
    P_is * math.log2(P_is)
    + P_drives * math.log2(P_drives)
)

print("P(is) =", P_is)
print("P(drives) =", P_drives)
print("Entropy =", entropy, "bits")

print("Higher entropy means greater prediction uncertainty.")
