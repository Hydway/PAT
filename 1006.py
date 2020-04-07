#Hydway
#2020-4-
# π”√¡Àtimeø‚

import time
num = int(input())
mat = [[] for i in range(num)]
log_in = []
log_out = []
temp = []
for i in range(num):
    temp = list(input().split())
    temp[1] = time.strptime(temp[1], "%H:%M:%S")
    temp[2] = time.strptime(temp[2], "%H:%M:%S")
    mat[i] = temp
    temp = []
for i in range(num):
    log_in.append(mat[i][1])
    log_out.append(mat[i][2])
first_in = [log_in.index(min(log_in)), min(log_in)]
last_out = [log_out.index(max(log_out)), max(log_out)]
print(mat[first_in[0]][0],mat[last_out[0]][0])