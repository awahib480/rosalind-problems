with open("dataset/rosalind_hamm.txt", "r") as file:
    content = file.read().strip()

seq = content.split('\n')
seq_1, seq_2 = seq[0], seq[1]

diff = 0
for i, j in zip(seq_1, seq_2):
    if i != j:
        diff += 1

print(diff)
