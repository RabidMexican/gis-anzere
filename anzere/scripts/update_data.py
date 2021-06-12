import csv

TABLE = input('Enter table name : ')
REQUEST_START = 'UPDATE ' + TABLE + ' SET '

with open('data.csv', newline='') as csvfile:
    i = 1
    reader = csv.reader(csvfile, delimiter=',')

    for row in reader:
        t = 0
        request = REQUEST_START

        for data in row:
            data = data.replace('%', '')
            request = '{0} t_{1} = {2}'.format(request, t, data)

            if t < 9:
                request = request + ','

            t += 1

        request = '{0} WHERE id = {1}'.format(request, i)
        i += 1
        print(request)
