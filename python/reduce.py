from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None
dic = {}
i = 0

for line in sys.stdin:
	line = line.strip()

	word, count = line.split('\t', 1)

	count = int(count)

	if current_word == word:
		current_count += count
	else:
		if current_word:
			#print '%s\t%s' % (current_word, current_count)
			dic[current_word] = int(current_count)
		current_count = count
		current_word = word

if current_word == word:
	#print '%s\t%s' % (current_word, current_count)
	dic[current_word] = int(current_count)

for key, value in sorted(dic.iteritems(), key=lambda (k,v): (v,k), reverse=True):
	i += 1
	print "%d: %s\t%d" % (i, key, value)

	if i == 1500:
		break
