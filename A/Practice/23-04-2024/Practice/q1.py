
# def max_occurrence_one_liner(test_str):
#     return max(test_str, key=test_str.count)

# original_str = "exemplary"
# most_frequent = max_occurrence_one_liner(original_str)
# print(f"The maximum occurring character in '{original_str}' is: {most_frequent}")



# def mool(tstr):
#     print(tstr.count)
#     return max(tstr, key=tstr.count)

# ostr = "exemplary is gd di"
# mfre = mool(ostr)
# print(mfre)




input_text = "All Is Well"

p1_text = {i: input_text.count(i) for i in set(input_text)}

print("Count of all characters is: "+ str(p1_text))

max_text = max(p1_text.values())
print(max_text)


# # ages = {'Matt': 30, 'Katie': 29, 'Nik': 31, 'Jack': 43, 'Alison': 32, 'Kevin': 38}
# max_value = max(ages.values())
# print(max_value)  # Returns: 43

