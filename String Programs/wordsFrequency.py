# Words Frequency in String Shorthands

test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'

print("======= dict comp, count() and split() =======")
string_list = test_str.split()
words_freq = { ele:string_list.count(ele) for ele in string_list}
print(words_freq)


print("========= Counter() and split() =========")
from collections import Counter

wordsfreq = Counter(test_str.split())
print(wordsfreq)