s="kamana"
freq={}
for ch in s:
    freq[ch]=freq.get(ch, 0) + 1
print(freq)
for ch in s:
    if freq[ch]==1:
        print(ch)
        break