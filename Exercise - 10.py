# Exercise - 10: Find and Replace

def findAndReplace(text,oldText,newText):
    return text.replace(oldText,newText)

original_text = input("Enter text: ")
old = input("Text to replace: ")
new = input("Replacement text: ")

result = findAndReplace(original_text, old, new)
print("Result:", result)
