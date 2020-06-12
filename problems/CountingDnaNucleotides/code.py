def counting_dna_nucleotides(DnaString):
    DnaString = DnaString.upper()

    CountA = 0
    CountC = 0
    CountG = 0
    CountT = 0

    for letter in DnaString:
        if letter == "A":
            CountA = CountA + 1
        elif letter == "C":
            CountC = CountC + 1
        elif letter == "G":
            CountG = CountG + 1
        elif letter == "T":
            CountT = CountT + 1

    return f"{CountA} {CountC} {CountG} {CountT}"
