import csv
import copy

myVehicle = {
    "vin": "ABC123456DEF",
    "make": "Tesla",
    "model": "Model S",
    "year": 2022,
    "range": 412,
    "topSpeed": 155,
    "zeroSixty": 3.1,
    "mileage": 25000
}

for key, value in myVehicle.items():
    print("{} : {}".format(key, value))

myInventoryList = []

with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    lineCount = 0
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')
        else:
            print(f'vin: {row[0]}, make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')
            currentVehicle = copy.deepcopy(myVehicle)
            currentVehicle["vin"] = row[0]
            currentVehicle["make"] = row[1]
            currentVehicle["model"] = row[2]
            currentVehicle["year"] = int(row[3])  # Convert to integer
            currentVehicle["range"] = int(row[4])  # Convert to integer
            currentVehicle["topSpeed"] = int(row[5])  # Convert to integer
            currentVehicle["zeroSixty"] = float(row[6])  # Convert to float
            currentVehicle["mileage"] = int(row[7])  # Convert to integer
            myInventoryList.append(currentVehicle)
        lineCount += 1
    print(f'Processed {lineCount} lines.')

for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key, value))
    print("-----")


