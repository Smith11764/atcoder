s = input()
term_list = ['dream', 'dreamer', 'erase', 'eraser']
term_list = sorted(term_list, reverse=True)

for i in range(len(term_list)):
    s = s.replace(term_list[i], '')

if s == '':
    print('YES')
else:
    print('NO')
