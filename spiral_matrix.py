def f(n):
    res = [[0]*n for i in range(n)]
    dirs = [(-1,0), (0,-1), (1,0), (0,1)]
    times = n
    cdir = 0
    sx, sy = n, n-1

    num = 1
    

    ####
    print(cdir)
    for i in range(times):
        sx = sx + dirs[cdir][0] 
        sy = sy + dirs[cdir][1] 
        print(sx+1, sy+1)
        res [sx][sy] = num
        num +=1
    
    cdir = (cdir+1)%4

    for times in range(n-1, 0, -1):
        print(cdir)
        for i in range(times):
            sx = sx + dirs[cdir][0] 
            sy = sy + dirs[cdir][1] 
            print(sx+1, sy+1)
            res [sx][sy] = num
            num += 1
        cdir = (cdir+1)%4
        
        print(cdir)
        for i in range(times):
            sx = sx + dirs[cdir][0] 
            sy = sy + dirs[cdir][1] 
            print(sx+1, sy+1)
            res [sx][sy] = num
            num += 1
        
        cdir = (cdir+1)%4

    return res


n=5
res = f(n)

for i in res:
    print(i)
