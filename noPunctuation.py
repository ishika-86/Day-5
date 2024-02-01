punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''\

text = "Hello!!!, he said ---and went str@ight hi$ way*."
no_pct = ""
for char in text:
    if char not in punctuations:
        no_pct += char

print(no_pct)
