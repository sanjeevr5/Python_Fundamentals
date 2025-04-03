def reverse_words(sentence):
    sentence = list(sentence)[::-1]
    left: int = 0
    right: int = 0
    leng: int = len(sentence)
    while right <= leng - 1:
        while right <= leng - 1 and sentence[right] == " ":
            sentence.pop(right)
            leng -= 1
        while right <= leng - 1 and sentence[right] != " ":
            right += 1
        sentence[left:right] = sentence[left:right][::-1]
        right += 1
        left = right
    return "".join(sentence[:-1] if sentence[-1] == " " else sentence)


assert reverse_words("  hello world!  ") == "world! hello"
