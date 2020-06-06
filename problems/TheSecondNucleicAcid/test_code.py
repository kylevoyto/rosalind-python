from problems.TheSecondNucleicAcid.code import the_second_nucleic_acid


def test_the_second_nucleic_acid_single_A():
    assert the_second_nucleic_acid('A') == 'A'


def test_the_second_nucleic_acid_single_C():
    assert the_second_nucleic_acid('C') == 'C'


def test_the_second_nucleic_acid_single_G():
    assert the_second_nucleic_acid('G') == 'G'


def test_the_second_nucleic_acid_single_T():
    assert the_second_nucleic_acid('T') == 'U'


def test_the_second_nucleic_acid_all_T():
    assert the_second_nucleic_acid('TTTTTTTTTT') == 'UUUUUUUUUU'


def test_the_second_nucleic_acid_sample():
    assert the_second_nucleic_acid('GATGGAACTTGACTACGTAAATT') == \
        'GAUGGAACUUGACUACGUAAAUU'
