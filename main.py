ans = []
while True:
    line = input()
    if line == '</body>':
        break
    if line[:3] == '<p>' and line[-4:] == '</p>':
        ans.append(line[3:-4])
    elif line[:3] == '<p>':
        s = line[3:]
        line = input()
        while line[-4:] != '</p>':
            s += ' ' + line
            line = input()
        s += ' ' + line[:-4]
        ans.append(s)
for i in range(len(ans) - 1, -1, -1):
    print(ans[i])
