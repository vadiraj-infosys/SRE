def triangle(lines):
    line_start = 3
    for i in range(1,lines+1):
        print("_"*i,line_start)
        line_start += 3


n = int(input("Enter the number of lines: "))
triangle(n)
