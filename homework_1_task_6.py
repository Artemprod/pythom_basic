print("I'll help you rich your sport goals, but you should trust me and do whatever i ask you to do  ")
first_result = int(input('how many kilometers you have run today?: '))
wished_result = int(input('How many kilometers you want to achieve?: '))

progress = first_result
day = 0
while progress <= wished_result:
    progress = progress + (progress * 0.1)
    day = day + 1
    print('DAY', day, ':',  round(progress, 2), 'km.')
