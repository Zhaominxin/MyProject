#Python精英挑战赛第二季第1期：本期题目：字符串格式化输出“两端对齐”

#给定一组字符串，字符串均由标准英语单词、空格及常用英语标点符号组成，
#要求编写函数，根据给定宽度，按照“两端对齐”的格式化输出。

#“两端对齐”格式要求：
#1. 每行必须以字母或标点符号开头，但表示结束的标点符号，如逗号、句号、问好、感叹号等不允许出现在每行开头。每行必须以字母或标点符号结尾，空格不允许出现在每行的开头和结尾。
#2. 若某一行只容得下一个单词，则该行按照左对齐格式输出，行尾同样不需要用空格填充。
#3. 参数width肯定会大于字符串中最长单词的长度，不需要考虑单词长度超过width的情况。
#4. 用空格填充时，应当遵循“空格尽可能均匀分布到单词与单词之间”的原则。

    
txt = "Hot work is one of the typical high risk work in work shop, if out of control, it will cause tragedy. We manage our hot work basing on the FM hot work permit system. Then, to make sure the fire risk are eliminated before we start hot work, what should we do? Please refer to this week's topic, hot work permit."

a = txt.split()
b=[]
for i in a:
	b.append(i)
	b.append(' ')

c = []
count = 0
print(b)
for i in range(122):
    if (count + len(b[i])) <= 30:
        c.append(b[i])
        count += len(b[i])
        print(count)
        print(b[i])
        print(c)
    else:
        c.append('\n')
        count = 0
        c.append(b[i])
        count+=len(b[i])

try:
    for i in range(len(c)):
        if c[i] == '\n':
            if c[i-1] == ' ':
                c.pop(i-1)
            else:
                c[i+1] == ' '
                c.pop(i+1)
except IndexError:
    None

d=''
for i in c:
    d+=i

print(d)
e = d.split('\n')

print(e)

for i in range(len(e)):
    if len(e[i]) < 30:
        #while  len(e[i])<30:
        diff = 30 - len(e[i])
        start = 0
        end = len(e[i])
        for j in range(1,diff):
            index = e[i].find(' ', start, end)
            e[i] = e[i][:index] + ' ' + e[i][index:]
            start + index


f = ''
for i in e:
    f += (i+'\n')

print(f)
