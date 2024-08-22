
divisors = []
for i in range(1, 101):
    my_list = range(1,i+1)
    for item in my_list:

     if i % item  == 0:
        divisors.append(item)

    if sum(divisors) == i * 2:
        print(i)
    else: divisors =[]
