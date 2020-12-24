frame = [0,1,2,3,4,5,6,7,8]

counter = 0
frame_L = []
frame_R = []

for i  in range(len(frame)):
    if i % 2 == 0:
        frame_L.append(frame[i])
    elif i % 2 != 0:
        frame_R.append(frame[i])
    else:
        print("Error")

print(frame_L)
print(frame_R)