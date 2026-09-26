with open("dataset/rosalind_rna.txt", "r") as file:
    seq = file.read().strip()

new_seq = ""

for i in seq:
    if i == "T":
        new_seq += "U"
    else:
        new_seq += i

print(new_seq)
