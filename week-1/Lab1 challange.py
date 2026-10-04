import keyword

def is_valid_identifier(name):
    if not name or keyword.iskeyword(name):
        return False

    if not (name[0].isalpha() or name[0] == "_"):
        return False

    for ch in name:
        if not (ch.isalnum() or ch == "_"):
            return False

    return True

print(is_valid_identifier("student_name"))
print(is_valid_identifier("2value"))
print(is_valid_identifier("class"))
