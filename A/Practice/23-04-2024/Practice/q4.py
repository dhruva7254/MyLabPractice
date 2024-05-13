
input_text = " Analysis involves examining data to extract 34 67 43 34 34c 34 34 insights and draw conclusions. It is like dissecting a complex puzzle into smaller pieces and using statistical methods to identify patterns and trends "

p1_text = input_text.replace(" ", "")

p2_text = {}

for i in p1_text:
	if i in p2_text:
		p2_text[i] += 1
	else:
		p2_text[i] = 1

print(str(p2_text))

max_text = max(p2_text.values())

print(max_text)


# The for loop iterates through each character in p1_text. If the character is already a key in p2_text, 
# its count is incremented by 1. Otherwise, a new key is added with an initial count of 1.