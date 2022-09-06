class Mission:
    def __init__(self, code, point, time):
        self.code = code
        self.point = point
        self.time = time

input_val = list(input().split())

mission = Mission(input_val[0],input_val[1],input_val[2])

code, point, time =  mission

print(f"secret code : {mission.code}\nmeeting point : {mission.point}\ntime : {mission.time}")
