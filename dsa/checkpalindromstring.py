def checkpalindromstring(s):
    chars = s.lower()
    cleantext = ''.join(char for char in chars if char.isalnum())
    reverse = cleantext[::-1]
    if cleantext == reverse:
        return reverse
    else:
        return False
   

print(checkpalindromstring( "hh"))