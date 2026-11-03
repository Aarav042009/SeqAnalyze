


dna_sequence = input("Enter the DNA sequence: ")



#dna_sequence = "ATTACGACTATCACAGCATACGCAGACTACTAGACGATCACAG"

print("DNA analysis Report")
print(f"DNA Sequence> {dna_sequence}")

total_length = len(dna_sequence)
print(f"Total Length> {total_length}")

a_count = dna_sequence.count("A")
t_count = dna_sequence.count("T")
g_count = dna_sequence.count("G")
c_count = dna_sequence.count("C")

print(f"A Count: {a_count} | T Count: {t_count} | G Count: {g_count} | C Count: {c_count}")

gc_concentration = c_count+g_count
print(f"GC Concentration: {gc_concentration}")


target_motif = "TATAAT"

if target_motif in dna_sequence:
    print(f"Target Motif '{target_motif}' found in the DNA sequence.")
else:
    print(f"Target Motif '{target_motif}' not found in the DNA sequence.")