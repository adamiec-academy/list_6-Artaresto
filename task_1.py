from random import shuffle
from copy import copy


def is_self_review(new_assignments):
    for key, value in new_assignments.items():
        if key == value:
            return True
    return False


def is_symetric_review(new_assignments):
    for key in new_assignments.items():
        if key == new_assignments[new_assignments[key]]:
            return True
    return False


def is_subsequent_review(previous_assignments, new_assignments):
    for key in new_assignments.items():
        if key in previous_assignments and new_assignments[key] == previous_assignments[key]:
            return True
    return False


def are_assignments_correct(previous_assignments, new_assignments):
    return all([
        not is_self_review(new_assignments),
        not is_symetric_review(new_assignments),
        not is_subsequent_review(previous_assignments, new_assignments)
    ])


def generate_assignments(previous_assignments, coders):
    shuffled_coders = copy(coders)

    while True:
        shuffle(shuffled_coders)
        new_assignments = {}

        for i in range(len(coders)):
            new_assignments[coders[i]] = shuffled_coders[i]

        if are_assignments_correct(previous_assignments, new_assignments):
            print(new_assignments)

