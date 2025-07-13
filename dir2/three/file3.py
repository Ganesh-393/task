def flatten(lst):
    return [i for sub in lst for i in sub]

print(flatten([[1,2],[3,4]]))  # [1, 2, 3, 4]

