

def test_user_status_code(user_response):
    assert user_response.status_code == 200
def test_user_name(user_response):
    data = user_response.json()
    assert data["name"] == "Leanne Graham"
def test_user_email(user_response):
    data = user_response.json()
    assert data["email"] == "Sincere@april.biz"

#################Making two seperate classes  for scope class ###############
class Test_user_details:
    def test_user_details(self, user_response):
        assert user_response.status_code == 200
        data = user_response.json()
        assert data["name"] == "Leanne Graham"
        assert data["email"] == "Sincere@april.biz"
class Test_user_account:
    def test_user_account(self ,user_response):
        data = user_response.json()
        assert data["username"] == "Bret"
        assert data["id"] == 1

######################Making two seperate classes where each class uses diffrent requests##################################
class Test_user_1details:
    def test_user_details(self, user_response):
        data = user_response.json()
        if data["id"] == 1:
            assert data["username"] == "Bret"
            assert data["name"] == "Leanne Graham"
        elif data["id"] == 2:
            assert data["username"]== "Antonette"
            assert data["name"]=="Ervin Howell"

