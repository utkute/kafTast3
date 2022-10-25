def rug_layout(height):
    width = height*3
    for i in range(1, height, 2):
        print(("/o\\"*i).center(width, "*"))

    print("Kovrick".center(width, "*"))

    for i in range(height-2, 0, -2):
        print(("\\o/"*i).center(width, "*"))