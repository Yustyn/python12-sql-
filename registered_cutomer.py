from typing import Dict

from settings import *
from check_login import check_login
from admin import *

login = 'admin'
password = '1234'
check_login(login, password)


class Reg_customer(Admin):

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def edit_self_info(self, data, selector):
        table = 'customer'
        result = self.updateData(table, data, selector)
        return result

    def create_order(self, data):
        table = 'orders'
        result = self.postData(table, data)
        return result

    def delete_order(self, selector):
        table = 'orders'
        selector = f"id = '{selector}'"
        result = self.deleteData(table, selector)
        return result

    def get_product_info(self, selector=''):
        table = ('product',)
        fields = ('*',)
        selector = ''
        result = self.getData(table, fields, selector)
        return result
