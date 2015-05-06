def CountingMinutesI(str):

    e = str.replace(':',' ').replace('-',' ').replace('pm',' p').replace('am',' a').split()
    g = [int(s) for s in e if s.isdigit()]

    if (e[2] == 'p' and e[5] == 'p') or (e[2] == 'a' and e[5] == 'a'):

        if g[0] == g[2]:
            if g[1] == g[3]:
                return 1440
            
            elif g[1] < g[3]:
                return abs((g[1])-g[3])
            
            elif g[1] > g[3]:
                return 1380+(60-abs((g[1])-g[3]))
        
        elif g[0] < g[2]:
            if g[2] == 12:
                if g[3] < g[1]:
                    return 720+((g[2]-g[0])*60)-(abs(g[1]-g[3]))
                return 720+((g[2]-g[0])*60)+(abs(g[1]-g[3]))
            return abs((g[1])-g[3])+60*abs((g[2])-g[0])

        elif g[0] > g[2]:
            if g[0] == 12:
                if g[1] == g[3] or g[1] < g[3]:
                    return abs((g[1])-g[3])+60*g[2]            
            return (g[2]*60)+abs((g[1])-g[3])

    elif e[2] == 'a' and e[5] == 'p' or e[2] == 'p' and e[5] == 'a':
        if g[0] == 12 or g[2] == 12:
            if g[2] == 12:
                return 720-(g[0]*60)+abs(g[1]-g[3])
            return 720+(g[2]*60)+abs(g[1]-g[3])
        elif g[0] == g[2]:
            if g[3] == g[1]:
                return 720
            elif g[3] > g[1]:
                return 720+abs((g[1])-g[3])
            elif g[3] < g[1]:
                return 720-abs((g[1])-g[3])
        elif g[0] < g[2]:
            return 720+abs((g[2] - g[0])*60)+abs(g[1]-g[3])
        
        return ((g[1])-g[3])+720
print CountingMinutesI(raw_input())           
# needs redoing
