from collections import Counter
filename = 'input8.txt'

f = open(filename)

total = 0
while True:
  line = f.readline()
  if line == '':
    break
  lookup = {}
  c = [x.strip() for x in line.split('|')]
  d = [''.join(sorted(x)) for x in c[0].split(' ')]
  one = [x for x in d if len(x) == 2][0]
  lookup[one] = 1
  four = [x for x in d if len(x) == 4][0]
  lookup[four] = 4
  seven = [x for x in d if len(x) == 3][0]
  lookup[seven] = 7
  eight = [x for x in d if len(x) == 7][0]
  lookup[eight] = 8

  # 2 is the digit without the only segment that appears nine times
  freq = Counter(''.join(d))
  segment_appears_nine_times = [x for x in freq if freq[x] == 9][0]
  two = [x for x in d if not segment_appears_nine_times in x][0]
  lookup[two] = 2
  # 2, 3 and 5 have five digits, we already found 2
  # of 3 and 5, only 3 contain all digits contained in 1
  one_segments = list(one)
  three = [x for x in d if len(x) == 5 and all(item in x for item in one)][0]
  lookup[three] = 3
  five = [x for x in d if len(x) == 5 and x != two and x!= three][0]
  lookup[five] = 5
  
  # e appears 4 times, of 0, 6 and 9, only 9 doesn't have e
  segment_appears_four_times = [x for x in freq if freq[x] == 4][0]
  nine = [x for x in d if len(x) == 6 and segment_appears_four_times not in x][0]
  lookup[nine] = 9

  # 0 and 6 remain, 0 includes c and f, the parts of 1
  zero = [x for x in d if len(x) == 6 and x != nine and all(item in x for item in one)][0]
  lookup[zero] = 0
  six = [x for x in d if x not in lookup.keys()][0]
  lookup[six] = 6


  e = [''.join(sorted(x)) for x in c[1].split(' ')]
  output = int(''.join([str(lookup[x]) for x in e]))
  total += output

print(f"total = {total}")

