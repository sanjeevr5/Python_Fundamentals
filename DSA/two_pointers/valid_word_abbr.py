def valid_word_abbreviation(word, abbr):
  word_index: int = 0
  abbr_index: int = 0
  word_leng: int = len(word)
  abbr_leng: int = len(abbr)
  while abbr_index < abbr_leng:
    if abbr[abbr_index].isnumeric():
      if abbr[abbr_index] == '0':
        return False
      num = ''
      while abbr_index < abbr_leng and abbr[abbr_index].isnumeric():
        num += abbr[abbr_index]
        abbr_index += 1
      num = int(num)
      word_index += num
    else:
      if word_index >= word_leng or word[word_index] != abbr[abbr_index]:
        return False
      else:
        word_index += 1
        abbr_index += 1
  return True if word_index == word_leng and abbr_index == abbr_leng else False

assert valid_word_abbreviation("internationalization", "i12iz4n") is True
assert valid_word_abbreviation("apple", "a2e") is False