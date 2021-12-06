from api import create_folder

class TestApi:

    def test_create_folder(self):
        assert create_folder('name_path') == 201, 'Error!'