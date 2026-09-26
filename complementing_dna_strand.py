with open("dataset/rosalind_revc.txt", "r") as file:
    seq = file.read().strip()

reversed_seq = seq[::-1]
c_seq = ""

for i in reversed_seq:
    if i == "A":
        c_seq += "T"
    elif i == "T":
        c_seq += "A"
    elif i == "C":
        c_seq += "G"
    elif i == "G":
        c_seq += "C"

print(c_seq)