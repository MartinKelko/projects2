def kbd(times):
    from time import time
    for p in range(0, times):
        t1 = time()
        try:
            n = 0
            while True: n += 1
        except KeyboardInterrupt:
            t2 = time()
            print(p, '. pokus, ', n, 'behov, ', s:=round(t2-t1, 3), ' sekund, ', round(n/s/1e6,3),'behov za mikrosekundu', sep='')
    print('koniec testu')

kbd(3)
