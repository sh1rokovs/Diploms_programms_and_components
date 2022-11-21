import csv

list1 = []
for el in range(0, 2):
    for elem in range(0, 100):
        list1.append(el + (elem / 100))

print(list1)

list2 = []
for elem in range(0, 200):
    list2.append(3.0)

print(list2)
print(len(list2))

with open('data1.csv', 'w', newline='') as csvfile:
    fieldnames = ['time', 'amp']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for el in range(0, 200):
        writer.writerow({'time': list1[el], 'amp': list2[el]})
