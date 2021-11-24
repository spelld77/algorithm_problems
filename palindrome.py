
test_sentence = 'A man, a plan, a canal: Panama'

# first solution
def is_palindrome(sentence) -> bool:

    #rm capital
    temp = sentence.lower()
    sent = ''
    reverse = ''

    #assign alphabet & number
    for i in temp:
        if i.encode().isalnum():
            sent = sent + i

    #saving reversed alpha & number
    for i in reversed(sent):
        reverse = reverse + i

    if sent == reverse:
        return True

    return False

#palindrome by list
def palindrome_by_list(self, s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    #펠린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True
