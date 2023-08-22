import json
import os


class ManageDB:
    __address_file = os.path.dirname(__file__)
    __address_json = os.path.join(__address_file, '../bd/dbContacts.json')

    def Read_contacts(self):
        with open(self.__address_json, 'r') as archivo:
            return json.loads(archivo.read())

    def write_contacts(self, new_data):
        with open(self.__address_json, 'w') as archivo:
            archivo.write(json.dumps(new_data))