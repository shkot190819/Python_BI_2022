
import requests
import re
import seaborn as sns

# 1
url = 'https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/references'
r = requests.get(url, allow_redirects=True)
pattern = re.compile(r'(ftp.sra.ebi.ac.uk.+?)(\t|;)')
rrr = re.findall(pattern, r.content.decode("utf-8"))

with open('ftps', 'w') as f:
  for i in range(len(rrr)):
    print(rrr[i][0], file=f)

# 6
def brick_language(translate_string):
  return re.sub(r"([аиоуэыеёюАИОУЭЫЕЁЮ])", r"\1р\1", translate_string)

url2 = 'https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/2430AD'

# 2
story = requests.get(url2, allow_redirects=True).text
numbers = re.findall(r'(\b\d+?\.?\d*?)\D', story)

# 3
word_with_a = re.findall(r'[a-zA-Z]*[aA][a-zA-Z]*\b', story)

# 4
exclamatory_sentences = re.findall(r'[A-Z][^\.]*?!', story)

# 5
not_yet_unique_words = re.findall(r"\w*\w'?\w*", story)
not_yet_unique_words_lower = [x.lower() for x in not_yet_unique_words]
unique_words = list(set(not_yet_unique_words_lower))

lengths_of_words = []
for i in unique_words:
  lengths_of_words.append(len(i))

lengths_of_unique_words = list(set(lengths_of_words))
numbers_of_words = []
for z in range(1,16):
  numbers_of_words.append(lengths_of_words.count(z)/len(unique_words))

sns.barplot(x=lengths_of_unique_words, y=numbers_of_words)



