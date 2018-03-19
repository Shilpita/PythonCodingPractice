import csv
def getRatio(filepath):
    sum_total_in = sum_total_out = ratio = 0.0
    with open(filepath, 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        for row in csv_reader:
            sum_total_in = sum_total_in + int(row[12])
            sum_total_out = sum_total_out + int(row[14])

    print(sum_total_in/(1024) , sum_total_out/(1024))
    ratio = float(sum_total_in /sum_total_out)
    return ratio


ratio = getRatio("data.txt")
print(ratio)