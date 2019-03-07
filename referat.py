with open('referat.txt', 'r', encoding='utf-8') as referat:
	content = referat.read()
number_symbol = len(content)
print(number_symbol)
len_words = 0
for i in content.split():
	len_words += 1
print(len_words)
correct_text = content.replace('.', '!')

with open('referat2.txt', 'w', encoding='utf-8') as referat2:
	referat2.write(correct_text)