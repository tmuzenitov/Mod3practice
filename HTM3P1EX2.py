x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = 0
keep_running = True
while (keep_running):
    y += 1
    for i in range(len(x)):
        if not x[i] < 3:
            keep_running = False
            break
        print(y)