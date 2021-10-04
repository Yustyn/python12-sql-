from typing import Dict

from settings import *
from check_login import check_login
from admin import *

login = 'admin'
password = '1234'
check_login(login, password)


class Unreg_customer(Admin):

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def register_self(self, data):
        table = 'customer'
        result = self.postData(table, data)
        return result

    def get_product_info(self, selector=''):
        table = ('product',)
        fields = ('*',)
        selector = ''
        result = self.getData(table, fields, selector)
        return result
