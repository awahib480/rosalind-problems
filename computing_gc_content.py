with open('dataset/rosalind_gc.txt', 'r') as file:
    content = file.read().strip()

seq = content.strip().split(">")
seq.pop(0)  # removing blank first entry

strings = {}    # dict for storing ids with gc-content
for string in seq:
    len_seq, gc_count = 0, 0
    for i in string[14:]:
        if i == 'A' or i == 'T' or i == 'C' or i == 'G':
            len_seq += 1
            if i == "C" or i == "G":
                gc_count += 1
    percentage = round((gc_count/len_seq)*100, 6)
    strings[string[0:13]] = percentage

max_gc, max_id = 0, 'Rosalind_xxxx'
for i in strings:
    if strings[i] > max_gc:
        max_gc = strings[i]
        max_id = i

print(f"{max_id}\n{max_gc}")
