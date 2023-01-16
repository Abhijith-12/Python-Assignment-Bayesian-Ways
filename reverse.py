orst = input('Enter the string you want to reverse?\n') 
orst= orst.lower()
revstring = "".join(reversed(orst))
if orst==revstring:
    print("The string is a pallinderome")
else:
    print("The string is not a pallinderome")