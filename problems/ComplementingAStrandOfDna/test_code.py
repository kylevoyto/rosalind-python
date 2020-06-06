from problems.ComplementingAStrandOfDna.code import (
    complementing_a_strand_of_dna
)


def test_complementing_a_strand_of_dna_single_A():
    assert complementing_a_strand_of_dna('A') == 'T'


def test_complementing_a_strand_of_dna_single_C():
    assert complementing_a_strand_of_dna('C') == 'G'


def test_complementing_a_strand_of_dna_single_G():
    assert complementing_a_strand_of_dna('G') == 'C'


def test_complementing_a_strand_of_dna_single_T():
    assert complementing_a_strand_of_dna('T') == 'A'


def test_complementing_a_strand_of_dna_all_G():
    assert complementing_a_strand_of_dna('GGGGGGGGGGGG') == 'CCCCCCCCCCCC'


def test_complementing_a_strand_of_dna_sample():
    assert complementing_a_strand_of_dna('AAAACCCGGT') == 'ACCGGGTTTT'
