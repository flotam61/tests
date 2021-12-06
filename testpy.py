from main import *


class TestPy:

    def test_check_document(self):
        assert check_document_existance("2207 876234") == True

    def test_add_new_doc(self):
        assert add_new_doc('1-1', 'passport RF', 'Dmitriy Polyakov', 2) == 2

    def test_delete_doc(self):
        assert delete_doc('2207 876234') == ('2207 876234', True)