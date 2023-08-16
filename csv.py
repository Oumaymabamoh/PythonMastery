import csv

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction-id", "product_id", "price"])
    writer.writerow([1000, 1, 5])
    writer.writerow([1001, 2, 15])
    # read data
    reader = csv.reader(file)
    print(list(reader))
