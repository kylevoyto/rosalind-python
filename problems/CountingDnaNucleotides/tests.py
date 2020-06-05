from problems.CountingDnaNucleotides.code import counting_dna_nucleotides


def test_counting_dna_nucleotides_single_A():
    assert counting_dna_nucleotides('A') == '1 0 0 0'


def test_counting_dna_nucleotides_single_C():
    assert counting_dna_nucleotides('C') == '0 1 0 0'


def test_counting_dna_nucleotides_single_G():
    assert counting_dna_nucleotides('G') == '0 0 1 0'


def test_counting_dna_nucleotides_single_T():
    assert counting_dna_nucleotides('T') == '0 0 0 T'


def test_counting_dna_nucleotides_21():
    assert counting_dna_nucleotides('ATGCTTCAGAAAGGTCTTACG') == '6 4 5 6'


def test_counting_dna_nucleotides_70():
    assert counting_dna_nucleotides(
        'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAG'
        'C'
    ) == '20 12 17 21'