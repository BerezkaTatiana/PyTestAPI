from api import Pets

pet = Pets()

def test_get_token():
    status = pet.get_token()[2]
    token = pet.get_token()[0]
    assert token
    assert status == 200

def test_get_list_users():
    my_id = pet.get_list_users()[1]
    status = pet.get_list_users()[0]
    assert my_id
    assert status == 200

def test_post_pet():
    status = pet.post_pet()[1]
    pet_id = pet.post_pet()[0]
    assert pet_id
    assert status == 200

def test_post_image():
    status = pet.post_image()[0]
    link = pet.post_image()[1]
    assert link
    assert status == 200

def test_update_pet():
    status = pet.update_pet()[0]
    pet_id = pet.update_pet()[1]
    assert pet_id
    assert status == 200

def test_put_like():
    status = pet.put_like()
    assert status == 200

def test_put_comment():
    status = pet.put_comment()[0]
    comment_id = pet.put_comment()[1]
    assert status == 200
    assert comment_id

def test_delete_pet():
    status = pet.delete_pet()
    assert status == 200
