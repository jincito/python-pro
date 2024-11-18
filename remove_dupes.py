def remove_duplicates(s):
    dupes = []

    for char in s:
        # If dupes is empty or last char is not the same as current
        if not dupes or dupes[-1] != char:
            dupes.append(char)
        else:
            dupes.pop()  # If duplicate, remove last char (duplicate)

    return "".join(dupes)
