for i in range(int(input())):
    sh, sm, eh, em = map(int, input().split(' '))
    wh, wm = 0, 0
    wm = (60-sm)+em
    wh = eh-sh-1
    if wm>=60:
        corr_hr = wm//60
        wm=wm%60
        wh = wh+corr_hr
    print(wh, wm)