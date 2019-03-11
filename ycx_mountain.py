
def cal_km(roadline, roadmap):
    km = 0
    for pos in range(len(roadline)-1):
        km += roadmap[roadline[pos]]
        km += roadmap[roadline[pos]+roadline[pos+1]]
    if roadline[0] != 'H':
        km += roadmap['H'+roadline[0]]
    return km

def creat_roadline(roadline,  mont, time ,all_line):
    if time > 1:
        for pos in mont:
            if pos != roadline[-1]:
                roadline.append(pos)
                time -= 1
                creat_roadline(roadline,  mont, time ,all_line)
                time += 1
                roadline.pop()
    if time == 1:
        roadline.append('H')
        time -= 1 
        creat_roadline(roadline,  mont, time ,all_line)
        roadline.pop()
        time += 1            
                
    if time == 0:
        all_line.append(tuple(roadline))
        # print(roadline,end='*\n')


roadmap = {'H': 6, 'J': 4, 'Y': 5, 'HJ': 3, 'JH': 3,
           'JY': 2, 'YJ': 2, 'HY': 5, 'YH': 5, 'HH': 0}
mont = ['H', 'J', 'Y']
roadline = []
km_dic = {}
all_line = []
for pos in mont:
    roadline.append(pos)
    creat_roadline(roadline,mont,5,all_line)
    roadline.pop()

# print(all_line)

for line in all_line:
    # print(line)
    km_dic[str(line)] = cal_km(line,roadmap)

tmp = sorted(km_dic.items(),key = lambda x:x[1],reverse = True)
for i in range(len(tmp)):
    print(tmp[i])
