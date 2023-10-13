def reverse_sort_dictionary(d: dict) -> dict:
    solution = []
    for key in sorted(d.keys(), reverse = True):
        solution.append((key, d[key][0]))
    return solution