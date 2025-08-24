BASE_URL = 'https://api.restful-api.dev/objects'

class Endpoints:

    ADD_OBJECT = BASE_URL
    GET_OBJECT_SINGLE = lambda self, obj_id: f'{BASE_URL}/{obj_id}'
    UPDATE_OBJECT = lambda self, obj_id: f'{BASE_URL}/{obj_id}'
    DELETE_OBJECT = lambda self, obj_id: f'{BASE_URL}/{obj_id}'