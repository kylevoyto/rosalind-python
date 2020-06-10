from problems.RabbitsAndRecurrenceRelations.code import (
    rabbits_and_recurrence_relations
)


def test_rabbits_and_recurrence_relations_n_1_k_1():
    assert rabbits_and_recurrence_relations(1, 1) == 1


def test_rabbits_and_recurrence_relations_n_1_k_2():
    assert rabbits_and_recurrence_relations(1, 2) == 1


def test_rabbits_and_recurrence_relations_n_1_k_3():
    assert rabbits_and_recurrence_relations(1, 3) == 1


def test_rabbits_and_recurrence_relations_n_1_k_4():
    assert rabbits_and_recurrence_relations(1, 4) == 1


def test_rabbits_and_recurrence_relations_n_1_k_5():
    assert rabbits_and_recurrence_relations(1, 5) == 1


def test_rabbits_and_recurrence_relations_n_2_k_1():
    assert rabbits_and_recurrence_relations(2, 1) == 1


def test_rabbits_and_recurrence_relations_n_2_k_2():
    assert rabbits_and_recurrence_relations(2, 2) == 1


def test_rabbits_and_recurrence_relations_n_2_k_3():
    assert rabbits_and_recurrence_relations(2, 3) == 1


def test_rabbits_and_recurrence_relations_n_2_k_4():
    assert rabbits_and_recurrence_relations(2, 4) == 1


def test_rabbits_and_recurrence_relations_n_2_k_5():
    assert rabbits_and_recurrence_relations(2, 5) == 1


def test_rabbits_and_recurrence_relations_n_3_k_5():
    assert rabbits_and_recurrence_relations(3, 5) == 6


def test_rabbits_and_recurrence_relations_n_4_k_5():
    assert rabbits_and_recurrence_relations(4, 5) == 11


def test_rabbits_and_recurrence_relations_n_7_k_5():
    assert rabbits_and_recurrence_relations(7, 5) == 301


def test_rabbits_and_recurrence_relations_n_12_k_2():
    assert rabbits_and_recurrence_relations(12, 2) == 1365


def test_rabbits_and_recurrence_relations_n_5_k_3():
    assert rabbits_and_recurrence_relations(5, 3) == 19


def test_rabbits_and_recurrence_relations_n_35_k_2():
    assert rabbits_and_recurrence_relations(35, 2) == 11453246123
