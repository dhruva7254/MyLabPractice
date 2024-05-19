import textwrap
sample_text = '''
            Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language.Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    '''
#text_without_Indentation = textwrap.dedent(sample_text)
#print()
#print(text_without_Indentation )
#print()
l=sample_text.split("\n")
for e in l:
    print(e.lstrip())
#s1="   aaca"
#print(s1.lstrip("  a"))     
