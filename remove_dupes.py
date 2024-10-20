def remove_duplicates(s):
    dupes = []
    
    for char in s:
        if not dupes or dupes[-1] != char:  # If dupes is empty or last char is not the same as current
            dupes.append(char)
        else:
            dupes.pop()  # If duplicate, remove last char (duplicate)
    
    return "".join(dupes)
