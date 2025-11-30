
# coding: UTF-8

# db_connect.py

import mysql.connector
import os
from tabulate import tabulate

connect = mysql.connector.connect (

    host = '127.0.0.1',
    user = 'root',
    password = '',

)

if connect.is_connected ():

    pass
    
else:

    print ('not connected!')
    exit ()

cursor = connect.cursor ()

my_database = 'my_database' 

verify_database = f"SHOW DATABASES LIKE '{my_database}';"

cursor.execute (verify_database)

verify_database = cursor.fetchone ()

if verify_database:

    pass

else:

    pwd = os.getcwd ()

    file_my_database = f'{pwd}\\my_database.sql'

    with open (file_my_database, 'r', encoding = 'UTF-8') as file:

        import_query_sql = file.read ()

    for jump in import_query_sql.split (';'):

        if jump.strip ():
   
            cursor.execute (jump)

while True:

    selected_database = f"USE {my_database};"
    
    cursor.execute (selected_database)

    os.system ('cls')
    
    print ("""
    =============================
   *                             * 
   *       CRUD in the Python    *
   *                             *   
   *     1) CREATE | CRIAR       *
   *     2) READ | LER           *
   *     3) UPDATE | ATUALIZAR   *
   *     4) DELETE | DELETAR     *
   *                             *
    =============================
    """)
    
    crud = int (input ('Type the option: '))
    os.system ('cls')

    if crud >= 5:
    
        print ('incorrect!')
        exit ()
        
    else:
    
        break

tables = ['users', 'address']

def show_tables_command ():

    command_show_tables = f"SHOW TABLES;"
    
    cursor.execute (command_show_tables)
    
    results = cursor.fetchall ()
    
    """for result in results:
    
        print (result [0])"""
        
    columns = [line[0] for line in results]

    datas = [[column] for column in columns]

    print (tabulate (datas, headers = [], tablefmt='grid'))

show_tables_command ()

print ('\n')

table_name = input ('table_name or e/E to exit: ')
os.system ('cls')

def show_columns_command ():

    if table_name in tables and table_name == 'users':

        command_show_columns = f"DESCRIBE users;"
        
        cursor.execute (command_show_columns)
        
        results = cursor.fetchall ()
        
        """for result in results:
        
            print (result [0])"""
            
        columns = [line[0] for line in results]

        datas = [[column] for column in columns]

        print (tabulate (datas, headers = [], tablefmt = 'grid'))
        
    elif table_name in tables and table_name == 'address':

        command_show_columns = f"DESCRIBE address;"
        
        cursor.execute (command_show_columns)
        
        results = cursor.fetchall ()
        
        """for result in results:
        
            print (result [0])"""
            
        columns = [line[0] for line in results]

        datas = [[column] for column in columns]

        print (tabulate (datas, headers = [], tablefmt = 'grid'))

if crud == 1:

    while True:
        
        if table_name in tables:
        
            show_columns_command ()
        
            if table_name == 'users':
            
                should_break = False
                
                print ('\n')
                quantity_columns = int (input ('quantity_columns: '))
            
                while True:
                
                    columns_users = []
                    data_users = []

                    print ('\n')
                    
                    for quantity_column in range (quantity_columns):
                    
                        column_user = input ('column_name{}: '.format (quantity_column+1))
                        columns_users.append (column_user)
                        
                    print ('\n')

                    for zero, column_user in enumerate (columns_users):
                    
                        data_for_column = input ('data_for_column_{}: '.format (column_user))
                        data_users.append (data_for_column)
                        
                    columns_join = ", ".join (columns_users)
                    values = []    
                        
                    for column, data_column in zip (columns_users, data_users):
                    
                        values.append (f"'{data_column}'" if isinstance (data_column, str) else str (data_column))
                    
                    data_join = ", ".join (values)
                    
                    command_insert = f"INSERT INTO {table_name} ({columns_join}) VALUES ({data_join})"
                    
                    cursor.execute (command_insert)
                    connect.commit ()
                    should_break = True
                    break
                
                if should_break == True:
                
                    break
                    
                else:
                
                    continue
                    
            elif table_name == 'address':
            
                should_break = False
                
                print ('\n')
                quantity_columns = int (input ('quantity_columns: '))
                
                while True:
                
                    columns_address = []
                    data_address = []
                    
                    print ('\n')
                    
                    for quantity_column in range (quantity_columns):
                    
                        column_address = input ('column_name{}: '.format (quantity_column+1))
                        columns_address.append (column_address)
                        
                    print ('\n')
                        
                    for zero, column_address in enumerate (columns_address):
                    
                        address_data = input ('data_for_column_{}: '.format (column_address))
                        data_address.append (address_data)
                        
                    columns_join = ", ".join (columns_address)
                    values = []
                    
                    for column, data_column in zip (columns_address, data_address):

                        values.append (f"'{data_column}'" if isinstance (data_column, str) else str (data_column))
                    
                    data_join = ", ".join (values)

                    command_insert = f"INSERT INTO {table_name} ({columns_join}) VALUES ({data_join})"

                    cursor.execute (command_insert)                    
                    connect.commit ()
                    should_break = True
                    break

                if should_break == True:

                    break

                else:

                    continue                
                
            elif table_name == 'e' or table_name == 'E':
        
                break
                
            else:
            
                print ('table not found!')
            
        else:
        
            print ('table not found!')
            break

elif crud == 2:

    while True:

        should_break = False

        def select_command ():

            if table_name in tables and table_name == 'users':
            
                show_columns_command ()
                
                print ('\n')
                quantity_columns = input ('quantity_columns or a/A to all: ')
                
                if quantity_columns.isdigit ():
                
                    quantity_columns = int (quantity_columns)
                
                    if quantity_columns >= 1 and quantity_columns < 6:
                    
                        columns_users = []

                        print ('\n')
                            
                        for quantity_column in range (quantity_columns):
                        
                            column_user = input ('column_name{}: '.format (quantity_column+1))
                            columns_users.append (column_user)
                            
                        print ('\n')
                        
                        columns_join = ", ".join (columns_users)
                    
                        command_select = f"SELECT {columns_join} FROM users;"

                        cursor.execute (command_select)
                        
                        results = cursor.fetchall ()

                        columns = [desc[0] for desc in cursor.description]

                        os.system ('cls')
                        print (tabulate (results, headers = columns, tablefmt = 'grid'))
                        
                    else:
                    
                        exit ()
                        
                elif quantity_columns == 'a' or quantity_columns == 'A':
                    
                    command_select = f"SELECT * FROM users;"
                
                    cursor.execute (command_select)
                    
                    results = cursor.fetchall ()

                    columns = [desc[0] for desc in cursor.description]

                    os.system ('cls')
                    print (tabulate (results, headers = columns, tablefmt = 'grid'))
                    
                else:
                
                    exit ()
                
            elif table_name in tables and table_name == 'address':
            
                show_columns_command ()
                
                print ('\n')
                quantity_columns = input ('quantity_columns or a/A to all: ')
                
                if quantity_columns.isdigit ():
                
                    quantity_columns = int (quantity_columns)
                
                    if quantity_columns >= 1 and quantity_columns < 6:
                    
                        columns_address = []

                        print ('\n')
                            
                        for quantity_column in range (quantity_columns):
                        
                            column_address = input ('column_name{}: '.format (quantity_column+1))
                            columns_address.append (column_address)
                            
                        print ('\n')
                        
                        columns_join = ", ".join (columns_address)
                    
                        command_select = f"SELECT {columns_join} FROM address;"

                        cursor.execute (command_select)
                        
                        results = cursor.fetchall ()

                        columns = [desc[0] for desc in cursor.description]

                        os.system ('cls')
                        print (tabulate (results, headers = columns, tablefmt = 'grid'))
                        
                    else:
                    
                        exit ()  
                
                elif quantity_columns == 'a' or quantity_columns == 'A':
            
                    command_select = f"SELECT * FROM address;"
                    
                    cursor.execute (command_select)
                    
                    results = cursor.fetchall ()

                    columns = [desc[0] for desc in cursor.description]

                    os.system ('cls')
                    print (tabulate (results, headers = columns, tablefmt = 'grid'))
                    
                else:
                
                    exit ()
                
            else:
            
                print ('table not found!')

        select_command ()
        
        if should_break == False:
        
            break

elif crud == 3:

    while True:

        should_break = False

        if table_name in tables and table_name == 'users':
        
            def select_command ():
        
                command_select = f"SELECT * FROM users;"
                
                cursor.execute (command_select)
                
                results = cursor.fetchall ()

                columns = [desc[0] for desc in cursor.description]

                print (tabulate (results, headers = columns, tablefmt = 'grid'))
                print ('\n')
                
            select_command ()
        
            data_id = int (input ('data_id: '))
            os.system ('cls')
            
            while True:
            
                columns_users = []
                data_users = []

                show_columns_command ()
                print ('\n')
                
                column_user = input ('column_name: ')
                columns_users.append (column_user)
                    
                print ('\n')
                
                data_for_column = input ('data_for_column_{}: '.format (column_user))
                data_users.append (data_for_column)
                    
                columns_join = ", ".join (columns_users)
                values = []    
                    
                for column, data_column in zip (columns_users, data_users):
                
                    values.append (f"'{data_column}'" if isinstance (data_column, str) else str (data_column))
                
                data_join = ", ".join (values)
                
                command_update = f"UPDATE {table_name} SET {columns_join} = {data_join} WHERE id = {data_id}"
                
                cursor.execute (command_update)
                connect.commit ()
                should_break = True
                break
            
            if should_break == True:
            
                break
                
            else:
            
                continue
            
        if table_name in tables and table_name == 'address':
        
            def select_command ():
        
                command_select = f"SELECT * FROM address;"
                
                cursor.execute (command_select)
                
                results = cursor.fetchall ()

                columns = [desc[0] for desc in cursor.description]

                print (tabulate (results, headers = columns, tablefmt = 'grid'))
                print ('\n')
                
            select_command ()
        
            data_id = int (input ('data_id: '))
            os.system ('cls')
            
            while True:
            
                columns_address = []
                data_address = []
                
                show_columns_command ()
                print ('\n')
                
                column_address = input ('column_name: ')
                columns_address.append (column_address)
                    
                print ('\n')
                
                data_for_column = input ('data_for_column_{}: '.format (column_address))
                data_address.append (data_for_column)
                    
                columns_join = ", ".join (columns_address)
                values = []
                    
                for column, data_column in zip (columns_address, data_address):
                
                    values.append (f"'{data_column}'" if isinstance (data_column, str) else str (data_column))
                
                data_join = ", ".join (values)
                
                command_update = f"UPDATE {table_name} SET {columns_join} = {data_join} WHERE id = {data_id}"
                
                cursor.execute (command_update)
                connect.commit ()
                should_break = True
                break
            
            if should_break == True:
            
                break
                
            else:
            
                continue

        elif table_name == 'e' or table_name == 'E':
        
            break
            
        else:
        
            print ('table not found!')
            break

elif crud == 4:

    while True:

        should_break = False

        if table_name in tables and table_name == 'users':
        
            def select_command ():
        
                command_select = f"SELECT * FROM users;"
                
                cursor.execute (command_select)
                
                results = cursor.fetchall ()

                columns = [desc[0] for desc in cursor.description]

                os.system ('cls')
                print (tabulate (results, headers = columns, tablefmt = 'grid'))
                print ('\n')
                
            select_command ()
            
            while True:
                
                data_id = int (input ('data_id: '))
                
                command_update = f"DELETE FROM {table_name} WHERE id = {data_id}"
                
                cursor.execute (command_update)
                connect.commit ()
                should_break = True
                break
            
            if should_break == True:
            
                break
                
            else:
            
                continue
            
        if table_name in tables and table_name == 'address':

            def select_command ():
        
                command_select = f"SELECT * FROM address;"
                
                cursor.execute (command_select)
                
                results = cursor.fetchall ()

                columns = [desc[0] for desc in cursor.description]
                
                os.system ('cls')
                print (tabulate (results, headers = columns, tablefmt = 'grid'))
                print ('\n')
                
            select_command ()
            
            while True:
                
                data_id = int (input ('data_id: '))
                
                command_delete = f"DELETE FROM {table_name} WHERE id = {data_id}"
                
                cursor.execute (command_update)
                connect.commit ()
                should_break = True
                break
            
            if should_break == True:
            
                break
                
            else:
            
                continue

        elif table_name == 'e' or table_name == 'E':
        
            break
            
        else:
        
            print ('table not found!')
            break

else:

    exit ()