users_time = int(input('input amount of seconds: '))  # user type his time
cnt_sec = users_time % 60
cnt_min = (users_time // 60) % 60
cnt_hr = int((users_time // 3600) % 24)

print(f" {cnt_hr:02d}:{cnt_min:02d}:{cnt_sec:02d}")



