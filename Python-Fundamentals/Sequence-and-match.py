'''Write a python program to
a.Find the sequence of uppercase letters followed by lowercase letters.
b.Match a word containing 'z'.
c.match a string that contains only upper and lowercase letters,numbers and underscores.
d.To remove leading zero's from an IP address.'''
#a.Find the sequence of uppercase letters followed by lowercase letters.
text1=input("Enter a text:")
words=text1.split()
result=[]
for word in words:
        if word[0].isupper() and word[1:].islower():
            result.append(word)
print("Sequences are:",result)

#b.Match a word containing 'z'.
text2=input("\nEnter a text to check word containing'z':");
words=text2.split()
result2=[]
for word in words:
    if'z' in word or 'Z' in word:
        result2.append(word)
print("Words Containing'z':",result2)

#c.match a string that contains only upper and lowercase letters,numbers and underscores.
text3=input("\nEnter text:")

has_upper=False
has_lower=False
has_digit=False
has_underscore=False
valid=True
for ch in text3:
    if ch.isupper():
        has_upper=True
    elif ch.islower():
        has_lower=True
    elif ch.isdigit():
        has_digit=True
    elif ch=="_":
        has_underscore=True
    else:
        valid=False

if valid and has_upper and has_lower and has_digit and has_underscore:
    print("Valid string.")
else:
    print("Invalid string.")


#d.To remove leading zero's from an IP address.
ip="192.168.001.010"
parts=ip.split('.')
new_parts=[]

for part in parts:
    new_parts.append(str(int(part)))
new_ip='.'.join(new_parts)
print("\nGiven IP:",ip)
print("Updated IP after removing trailing zeros:",new_ip)

