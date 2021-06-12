import csv

TABLES = ['commerce', 'gare', 'parking', 'piste', 'telecabine', 'teleski', 'telesiege']
LAST_COLUMN = 9


def print_request_for_table(current_table):
    request_start = 'UPDATE ' + current_table + ' SET '
    with open('./data/{0}.csv'.format(current_table), newline='') as csvfile:
        i = 1
        reader = csv.reader(csvfile, delimiter=',')

        for row in reader:
            t = 0
            request = request_start

            for data in row:
                data = data.replace('%', '')
                request = '{0} t_{1} = {2}'.format(request, t, data)

                if t < LAST_COLUMN:
                    request = request + ','

                t += 1

            request = '{0} WHERE id = {1}{2}'.format(request, i, ';')
            i += 1
            print(request)


for table in TABLES:
    print_request_for_table(table)
