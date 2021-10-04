from typing import Dict
import psycopg2

from settings import *
from check_login import check_login

login = 'admin'
password = '1234'
check_login(login, password)


class Admin():

    def __init__(self, login, password):
        self.login = login
        self.password = password

    @classmethod
    def openDB(cls):
        connection = psycopg2.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            database='shop_db'
        )
        cursor = connection.cursor()
        return connection, cursor

    @classmethod
    def closeDB(cls, connection, cursor):
        cursor.close()
        connection.close()

    def getData(self, table: tuple, fields: tuple, selector=''):
        connection, cursor = self.openDB()
        select_query = f"""SELECT {','.join(fields)} FROM {','.join(table)} {selector};"""
        cursor.execute(select_query)
        connection.commit()
        result = cursor.fetchall()
        self.closeDB(connection, cursor)
        return result

    def postData(self, table, data: list):
        connection, cursor = self.openDB()
        next_id = self.get_Next_Id(table)
        fields = list(data[0].keys())
        fields.append('id')
        values = ''
        for row in data:
            value = f"""({','.join(map(lambda item: f"'{item}'", row.values()))}, {next_id}),"""
            next_id += 1
            values += value
        insert_query = f"""INSERT INTO {table}  ({','.join(fields)}) VALUES {values[:-1]};"""
        cursor.execute(insert_query)
        connection.commit()
        self.closeDB(connection, cursor)
        return 'Insert done.'

    def updateData(self, table, data: dict, selector: str):
        connection, cursor = self.openDB()
        set_items = ''
        for key in data:
            set_items += f"{key} = '{data[key]}',"

        update_query = f"""UPDATE {table} SET {set_items[:-1]} WHERE {selector}  """
        cursor.execute(update_query)
        connection.commit()
        self.closeDB(connection, cursor)
        return 'Update done.'

    def deleteData(self, table, selector=''):
        connection, cursor = self.openDB()
        delete_query = f"""DELETE FROM {table} WHERE {selector};"""
        cursor.execute(delete_query)
        connection.commit()
        self.closeDB(connection, cursor)
        return "Item deleted."

    def get_Next_Id(self, table):
        table = (table,)
        fields = ('id',)
        result = self.getData(table, fields)[-1][0] + 1
        return result

    def get_order_info(self, selector=''):
        table = ('orders',)
        fields = ('*',)
        selector = ''
        result = self.getData(table, fields, selector)
        return result

    def add_pr_category(self, data):
        table = 'product_category'
        result = self.postData(table, data)
        return result

    def edit_pr_category(self, data, selector):
        table = 'product_category'
        result = self.updateData(table, data, selector)
        return result

    def delete_pr_category(self, selector):
        table = 'product_category'
        selector = f"category_name = '{selector}'"
        result = self.deleteData(table, selector)
        return result

    def add_product(self, data):
        table = 'product'
        result = self.postData(table, data)
        return result

    def delete_product(self, selector):
        table = 'product'
        selector1 = f"product_name = '{selector}'"
        result = self.deleteData(table, selector1)
        return result

    def add_employee(self, data):
        table = 'employee'
        result = self.postData(table, data)
        return result

    def delete_employee(self, selector):
        table = 'employee'
        selector = f"id = '{selector}'"
        result = self.deleteData(table, selector)
        return result

    def delete_customer(self, selector):
        table = 'customer'
        selector = f"id = '{selector}'"
        result = self.deleteData(table, selector)
        return result

    def edit_product(self, data, selector):
        table = 'product'
        result = self.updateData(table, data, selector)
        return result

    def edit_employee(self, data, selector):
        table = 'employee'
        result = self.updateData(table, data, selector)
        return result

    def register_self(self, data):
        table = 'login'
        result = self.postData(table, data)
        return result

# data = [
#     {
#         'first_name': "Ibrahim",
#         'last_name': 'Muhamed',
#         'date_of_birth': '1993-12-11',
#         'city_id': '3',
#         'chief_id': 2
#     }
# ]


data = {
    'product_name': 'Green tea'
}


if __name__ == '__main__':
    admin1 = Admin('Admin1', '1234')
    # orders = admin1.get_order_info()
    # print(orders)
    # put = admin1.add_pr_category(data)
    # print(put)
    # id = admin1.get_Next_Id('product_category')
    # print(id)
    # data = {
    #     'category_name': "Rum"
    # }
    # edit = admin1.edit_pr_category(data, "category_name = 'Water'")
    # print(edit)
    # delete = admin1.delete_pr_category('sweets')
    # print(delete)
    # add_product = admin1.add_product(data)
    # print(add_product)
    # add_employe = admin1.add_employee(data)
    # print(add_employe)
    # delete_product = admin1.delete_product('Water')
    # print(delete_product)
    # delete_emp = admin1.delete_employee('11')
    # print(delete_emp)
    # del_customer = admin1.delete_customer('10')
    # print(del_customer)
    # data = {
    #     'first_name': 'Kristoff'
    # }
    # edit_employee = admin1.edit_employee(data, "first_name = 'Nathanael'")
    # print(edit_employee)

    data = [{
        'login': 'admin1',
        'password': '123456'
    }]
    register_self = admin1.register_self(data)
    print(register_self)
