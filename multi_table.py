def print_multi_table(a,b):
    for i in range(a, b+1):
        print(f"สูตรคูณแม่ {i} ")
        for j in range(1, 13):
            if (i*j%2 == 0):
                print(f"{i} x {j} = {i * j}")
        print("\n")