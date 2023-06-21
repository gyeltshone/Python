def reverse(text):
    if len(text) == 0:
        return text
    else:
        return (reverse(text[1:])+ text[0] )
print(reverse('pythons'))
# def reverse(text):
#     string = ""
#     for i in text:
#         string = i + string
#     return string
# print(reverse('hello'))


# def reverse_string(string):

#     i = -1
#     reverseString = []
#     while i < len(string) and len(string):
        
#         text = string[i]
#         reverseString.append(text)
#         i-=1
#     print(reverseString)
# reverse_string('python')

