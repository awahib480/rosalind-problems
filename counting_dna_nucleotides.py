with open ('dataset/rosalind_dna.txt', "r") as file:
    seq = file.read().strip()

count_A, count_C, count_G, count_T = 0, 0, 0, 0

for i in seq:
    if i == "A":
        count_A += 1
    elif i == "C":
        count_C += 1
    elif i == "G":
        count_G += 1
    elif i == "T":
        count_T += 1

print(f"{count_A} {count_C} {count_G} {count_T}")