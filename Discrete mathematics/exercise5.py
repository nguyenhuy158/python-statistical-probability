s = input("enter= ")

if s.find("-") != -1:
	first = s[: s.find("-")]
	second = s[s.find("-") + 1:]

	print(int(first) - int(second))

if s.find("+") != -1:
	first = s[: s.find("+")]
	second = s[s.find("+") + 1:]

	print(int(first) + int(second))

if s.find("*") != -1:
	first = s[: s.find("*")]
	second = s[s.find("*") + 1:]

	print(int(first) * int(second))

if s.find("/") != -1:
	first = s[: s.find("/")]
	second = s[s.find("/") + 1:]

	print(int(first) / int(second))
