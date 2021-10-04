from typing import Dict

from settings import *
from check_login import check_login
from admin import *

login = 'admin'
password = '1234'
check_login(login, password)


class Employee(Admin):

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def edit_self_info(self, data, selector):
        table = 'employee'
        result = self.updateData(table, data, selector)
        return result

    def change_order_status(self, data, selector):
        table = 'orders'
        result = self.updateData(table, data, selector)
        return result
