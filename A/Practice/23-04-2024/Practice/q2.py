
input_text = " Analysis involves examining data to extract insights and draw conclusions. It’s like dissecting a complex puzzle into smaller pieces and using statistical methods to identify patterns and trends "

p1_text = {i: input_text.count(i) for i in set(input_text)}

print(str(p1_text))

max_text = max(p1_text.values())

print(max_text)

p1_text = input_text.replace(" ", "")