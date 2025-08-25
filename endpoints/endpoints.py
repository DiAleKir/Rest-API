BASE_URL = 'https://api.restful-api.dev/objects'


class Endpoints:
    ADD_OBJECT = BASE_URL
    GET_OBJECT_SINGLE = lambda self, obj_id: f'{BASE_URL}/{obj_id}'
    GET_ALL_OBJECTS = BASE_URL
    GET_OBJECTS_BY_IDS = lambda self, id1, id2: f'{BASE_URL}?id={id1}&id={id2}'
    UPDATE_OBJECT = lambda self, obj_id: f'{BASE_URL}/{obj_id}'
    DELETE_OBJECT = lambda self, obj_id: f'{BASE_URL}/{obj_id}'
