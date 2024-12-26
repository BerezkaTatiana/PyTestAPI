import json
import requests
import os
from settings import VALID_EMAIL, VALID_PASSWORD, PET_NAME, PET_AGE, PET_NAME_UPDATED, PET_AGE_UPDATED, COMMENT

class Pets:
    """ API library for http://34.141.58.52:8080/#/ """

    def __init__(self):
        self.base_url = 'http://34.141.58.52:8000/'

    def get_token(self) -> json:
        """ Request to the swagger's site  to obtain a unique user token using the specified password and email"""
        data = {'email': VALID_EMAIL, 'password': VALID_PASSWORD}
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        my_token = res.json()['token']
        my_id = res.json()['id']
        status = res.status_code
        return  my_token, my_id, status

    def get_list_users(self) -> []:
        """ Request to the swagger's site  to obtain user_id using the specified token"""
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + 'users', headers=headers)
        status = res.status_code
        my_id = res.text
        return status, my_id

    def post_pet(self) -> json:
        """ Request to the swagger's site  to create pet using the specified token"""
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[1]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"name": PET_NAME, "type": "hamster", "age": PET_AGE, "owner_id": my_id}
        res = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        return pet_id, status

    def post_image(self) -> json:
        """ Request to the swagger's site  to upload pet's image using the specified pet_id"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        file_path = os.path.join(os.path.dirname(__file__), 'tests', 'Photo', 'Caracal.jpg')
        files = {'pic': ('Caracal.jpg', open(file_path, 'rb'), 'image/jpg')}
        res = requests.post(self.base_url + f'pet/{pet_id}/image', headers=headers, files=files)
        status = res.status_code
        link = res.json()['link']
        return status, link

    def update_pet(self) -> json:
        """ Request to the swagger's site  to update pet using the specified pet_id"""
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[1]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": pet_id, "name": PET_NAME_UPDATED, "type": "hamster", "age": PET_AGE_UPDATED, "owner_id": my_id}
        res = requests.patch(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        status = res.status_code
        pet_id = res.json()['id']
        return status, pet_id

    def put_like(self):
        """ Request to the swagger's site  to add like using the specified pet_id"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res =requests.put(self.base_url + f'pet/{pet_id}/like', headers=headers)
        status = res.status_code
        return status

    def put_comment(self) -> json:
        """ Request to the swagger's site  to add comment using the specified pet_id"""
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[1]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"pet_id": pet_id, "message": COMMENT, "user_id": my_id}
        res =requests.put(self.base_url + f'pet/{pet_id}/comment', headers=headers, data=json.dumps(data))
        status = res.status_code
        comment_id = res.json()['id']
        return status, comment_id

    def delete_pet(self) -> json:
        """ Request to the swagger's site to delete pet using the specified pet_id"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.delete(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        return status




