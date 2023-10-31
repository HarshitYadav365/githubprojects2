for i in range(1, 11):
    print()

    for j in range(1, 11):
        product = i * j
        if product in range(1, 10):
            print(product, end="  ")
        else:
            print(product, end=" ")
