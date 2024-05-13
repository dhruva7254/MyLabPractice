
input_text = " Analysis involves examining data to extract 34 67 43 34 34c 34 34 insights and draw conclusions. It is like dissecting a complex puzzle into smaller pieces and using statistical methods to identify patterns and trends "

p1_text = input_text.replace(" ", "")

p2_text = {i: p1_text.count(i) for i in set(p1_text)}

print(str(p2_text))

max_text = max(p2_text.values())

print(max_text)

