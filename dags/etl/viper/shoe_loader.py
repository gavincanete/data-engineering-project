import csv
import psycopg2
from configparser import ConfigParser

# Get the database name, user, host and password
def get_credentials():
    filename = 'shoe_database.ini'
    section = 'postgresql'

    parser = ConfigParser()
    parser.read(filename)

    credential = {}

    if parser.has_section(section):
        for param in parser.items(section):
            credential[param[0]] = param[1]

    return credential

def store_in_postgres(
        shoes_info,
        stocks,
        table_name
    ):

    # Get Credential for Database access
    params = get_credentials()

    print(params)

    # Connect to Database
    try:
        conn = psycopg2.connect(**params)
    except psycopg2.Error as e:
        print(e)

    try:
        cur = conn.cursor()
    except psycopg2.Error as e:
        print(e)

    # Upon executing SQL, the table gets updated automatically
    conn.set_session(autocommit=True)

    cur.execute('drop table if exists ' + table_name)
    cur.execute('create table ' + table_name + \
        '(stock_number int, color varchar, sizes varchar, description varchar)')
    
    
    for stock in stocks:
        cur.execute('insert into '+ table_name +' values (%s, %s, %s, %s)', \
            (stock['stock_number'], stock['color'], stock['sizes'], stock['description']))

    # print('Successfully stored in Database!')

    cur.close()
    conn.close()


    return None


# Convert into CSV file
def convert_into_csv(path, category, shoes_info, stocks):    
    with open(path+category+'_shoes.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=shoes_info)
        writer.writeheader()
        writer.writerows(stocks)
        
        csvfile.close()

    return None