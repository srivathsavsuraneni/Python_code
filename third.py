sum = []
def main(a,b):
    print (a, " ", b, end = ' ')

    for i in range(10):
        sum.append(a+b)
        a, b = b, sum[i]
        print (sum[i], end = ' ')

main(0, 1)