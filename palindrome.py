
test_sentence = 'A man, a plan, a canal: Panama'

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

print(is_palindrome(test_sentence))
