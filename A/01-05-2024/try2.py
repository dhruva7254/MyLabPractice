# a = input("enter something: ")
# print(a)
# print(id(a))
# import keyword as k
# print(k.kwlist)
# k.iskeyword(ord)
# print("*"*5)
# n=0
# while n<5:
#     print("*",end=' ')
#     n += 1

# c=0
# while()

def remove_common_indentation(s):
    # Split the string into lines
    lines = s.splitlines()

    # Determine the minimum indentation (excluding the first line)
    min_indent = float('inf')
    for line in lines[1:]:
        stripped_line = line.lstrip()
        if stripped_line:
            min_indent = min(min_indent, len(line) - len(stripped_line))

    # Remove the common indentation from all lines
    trimmed_lines = [line[min_indent:] for line in lines]
    return '\n'.join(trimmed_lines)

# Example usage:
original_string = """
        foo bar
    baz
    foobar
"""
result = remove_common_indentation(original_string)
print(result)