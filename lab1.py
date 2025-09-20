def print_multi_table(a,b):
    for i in range(a, b+1):
        print(f"สูตรคูณแม่ {i} ")
        for j in range(1, 13):
            if (i*j%2 == 0):
                print(f"{i} x {j} = {i * j}")
        print("\n")

print_multi_table(2,5)

students = [{'name': 'Mark', 'grade':'A'},
            {'name': 'John', 'grade':'B'},
            {'name': 'Jeff', 'grade':'A'},
            {'name': 'Peach', 'grade':'A'},
            {'name': 'Boat', 'grade':'A'}]

count = 0
for person in students:
    if person['grade'] == 'A':
        print(person)
        count +=1
print(count)