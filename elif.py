x = range(30)
for y in x:
    if y%3==0:
        print(f"{y}\t This is divisible by three")
    elif y%5==0:
        print(f"{y}\t This is divisibleby five.")
    elif y%7==0:
        print(f"{y}\t This is divisible by seven.")
    else:
        print(f"{y}\t is not divisible.")            