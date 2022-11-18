# given the attached fasta file, return the DNA sequence name that has the highest GC-content
# The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'.
#
# Expected output:
# sequence_0808
# 60.919540

def read_fasta(file_name):
    fasta_file = open(file_name)
    name = ''
    sequences = {}

    for line in fasta_file:
        if line.startswith('>'):
            name = line[1:].rstrip('\n')
            sequences[name] = ''
        else:
            sequences[name] += line.rstrip('\n').rstrip('*')
    return sequences


def count_symbols(sequences):
    gc_content = {}
    counter = 0
    for i in sequences:
        gc_content[i] = ''
        for symbol in sequences[i]:
            if symbol == "C" or symbol == "G":
                counter += 1
        gc_content[i] = (counter/len(sequences[i]))*100
        counter = 0
    max_percentage = max(gc_content, key=lambda x: gc_content[x])
    return max_percentage + "\n" + str(gc_content[max_percentage])


sequence_list = read_fasta("question_2.fasta")
print(count_symbols(sequence_list))
