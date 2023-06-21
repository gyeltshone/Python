def alplaNumeric(s):
    # removealphanumericschar = ''.join(char for char in s if not(char.isalpha() or char.numrical()) )
    removealphanumericschar= ''.join(char for char in s if not char.isalpha() or char.isnumeric())
    return removealphanumericschar 
print(alplaNumeric('dfjl2349lsj@'))