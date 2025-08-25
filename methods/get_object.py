import random

import requests

from methods.base_methods import BaseMethods


class GetObject(BaseMethods):

    def get_single_object(self, obj_id):
        self.response = requests.get(self.endpoints.GET_OBJECT_SINGLE(obj_id))

    def get_all_object(self):
        self.response = requests.get(self.endpoints.GET_ALL_OBJECTS)

    def get_objects_by_ids(self):
        id_1 = random.randint(1, 6)
        id_2 = random.randint(7, 13)
        self.response = (requests.get
                         (self.endpoints.GET_OBJECTS_BY_IDS(id_1, id_2)))
        return id_1, id_2
