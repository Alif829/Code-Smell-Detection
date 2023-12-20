def complex_method(data):
    if data:
        for item in data:
            if item > 0:
                if item % 2 == 0:
                    for i in range(1, item):
                        if i % 2 != 0:
                            print(f"Odd: {i}")
                        else:
                            if i > 5:
                                for j in range(i):
                                    if j < item:
                                        print(j)
                            else:
                                print("Less than 5")
                elif item < 10:
                    for k in range(item, 0, -1):
                        if k in data:
                            print(f"Item {k} in data")
                        else:
                            for x in range(5):
                                if x in data:
                                    print(f"{x} found in data")
                else:
                    print("Item is negative or zero")
            else:
                print("No data")
    else:
        print("Empty data")
