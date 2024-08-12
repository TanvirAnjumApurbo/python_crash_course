str = 'This is a string.\n'
str2 = "This is also a string."
print(str+str2)

name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada "
last_name = "lovelace"
full_name = f"{first_name}{last_name}"
full_name1 = first_name+last_name
print(full_name)
print(full_name1)
print(f"Hello, {full_name.title()}!")

favorite_language = ' python '
print(favorite_language.strip())

nostarch_url = "https://www.nostarch.com"
print(nostarch_url.removeprefix('https://'))
