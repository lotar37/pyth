result  = []
files = ["x.txt","+.txt","-.txt","=.txt"]
x_arr = []
y_arr = []
for k in range(len(files)):
    print(files[k])
    f = open(files[k])
    lines = f.readlines()
    for line in lines:
        # if line == "\n":
        #     continue
        x_arr.append([int(i) for i in line.split(",")])
        y_arr.append(10+k)
print(len(x_arr),len(y_arr))