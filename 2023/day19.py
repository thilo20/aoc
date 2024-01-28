import json
import re

total=0

#idea: use eval() function
x=eval("a<2006", {"x":787,"m":2655,"a":1222,"s":2876})
# x= exec("if a<2006:qkq", {'a':2005})

# (\w+){(([xmas][<>]\d+):(\w+),?)
# [^{},]+ gives: ['px', 'a<2006:qkq', 'm>2090:A', 'rfg']
workflows={} # name:[rules]

parts=[] # xmas dicts

# Opening file
file = open('day19.txt', 'r')
for line in file:
    # try:
    #     # line='{x:787,m:2655,a:1222,s:2876}'
    #     line='{"x"=787,"m"=2655,"a"=1222,"s"=2876}'
    #     # line='{x=787,m=2655,a=1222,s=2876}'
    #     line=line.replace('=', ':')
    #     ratings.append( json.loads(line) )
    # except json.JSONDecodeError:
    #     pass
    command=re.findall("[^{},\n]+", line)
    if len(command)==4 and command[0].startswith('x='):
        d={}
        for com in command:
            s=com.split('=')
            d[s[0]]=int(s[1])
        parts.append(d)
    elif len(command)>1:
        workflows[command[0]]=command[1:]
file.close()

# apply workflows
def evaluate(part, workflows) -> int:
    wf='in'

    while True:
        for rule in workflows[wf]:
            if rule=='A':
                return sum(part.values())
            if rule=='R':
                return 0
            if ':' in rule:
                s=rule.split(':')
                # https://stackoverflow.com/questions/13491571/how-does-the-eval-function-change-the-dict
                # if eval(s[0], part):
                if eval(s[0], {}, part):
                    wf=s[1]
                    if wf=='A':
                        return sum(part.values())
                    if wf=='R':
                        return 0
                    break
            else: 
                wf=rule
    return 0


for part in parts:
    rating = evaluate(part, workflows)
    total += rating 

print(total)

# find start pos
# for i in range(dimx):
#      if image[0][i]>0: print(i)
# 127,1
print(total)
