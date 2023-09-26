# Video alternative: https://youtu.be/qDWyR0XpJtQ&t=1295s

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging
# than the example.

# Write a function that takes a list of words and returns a
# report of all the words that are longer than 10 characters
# but don't contain a hyphen. If those words are longer than
# 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.

print("")
print("Function: report_long_words")

def report_long_words(words):
  long_words = remove_short_words(words)
  no_hyphens = remove_hyphens(long_words)
  shortened_words = shorten_long_words(no_hyphens)
  sentence = combine_words(shortened_words)

  print(sentence)
  return sentence

def remove_short_words(words):
  long_words = []

  for word in words:
    if len(word) > 10:
      long_words.append(word)
  
  print(long_words)
  return long_words

def remove_hyphens(words):
  no_hyphens =[]

  for word in words:
    if "-" not in word:
      no_hyphens.append(word)

  print(no_hyphens)
  return no_hyphens

def shorten_long_words(words):
  shortened_words = []

  for word in words:
    if len(word) > 15:
      ell = word[0:15] + "..."
      shortened_words.append(ell)
    else:
      shortened_words.append(word)

  print(shortened_words)
  return shortened_words


def combine_words(words):
  sentence = "These words are quite long: "

  for word in words:
    if word != words[-1]:
      sentence += f"{word}, "
    else:
      sentence += word
  
  print(sentence)
  return sentence



check_that_these_are_equal(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]),
  "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
  report_long_words([
    'cat',
    'dog',
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog'
  ]),
  "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
  report_long_words([
    'cat'
  ]),
  "These words are quite long: "
)

# Once you're done, move on to 041_challenge_2_example.py
