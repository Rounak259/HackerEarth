seat_type = {1:'WS', 2:'MS', 3:'AS', 4:'AS', 5:'MS', 6:'WS', 7:'WS', 8:'MS', 9:'AS', 10:'AS', 11:'MS', 0:'WS'}
seat_num = {0:-11, 1:11, 2:9, 3:7, 4:5, 5:3, 6:1, 7:-1, 8:-3, 9:-5, 10:-7, 11:-9}

t_case = int(input())
for i in range(0,t_case):
    seat = int(input())
    req_seat = seat + seat_num[seat%12]
    print(req_seat, seat_type[req_seat%12])