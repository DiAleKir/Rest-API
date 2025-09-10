from tests.base_test import BaseTest


class TestCreateObject(BaseTest):

    def test_create_object(self):
        obj_id = self.create_object.create_object()
        self.create_object.check_response_is_200()
        self.create_object.check_name()
        self.delete_object.delete_object(obj_id)
        self.delete_object.check_response_is_200()
        self.get_object.get_single_object(obj_id)
        self.get_object.check_response_is_404()


class TestCreateObjectNegative(BaseTest):

    def test_create_empty_object(self):
        self.create_object_neg.create_empty_object()
        self.create_object_neg.check_response_is_400(), "Создался пустой объект"

    def test_create_object_without_name(self):
        self.create_object_neg.create_object_without_name()
        self.create_object_neg.check_response_is_400(), "Создался объект без имени"

    def test_create_object_with_invalid_name(self):
        self.create_object_neg.create_object_with_invalid_name()
        self.create_object_neg.check_response_is_400(), "Создался объект с невалидным именем"

    def test_create_object_without_data(self):
        self.create_object_neg.create_object_without_data()
        self.create_object_neg.check_response_is_400(), "Создался объект без data"

    def test_create_object_without_price(self):
        self.create_object_neg.create_object_without_price()
        self.create_object_neg.check_response_is_400(), "Создался объект без цены"

    def test_create_object_with_negative_price(self):
        self.create_object_neg.create_object_with_negative_price()
        self.create_object_neg.check_response_is_400(), "Создался объект с отрицательной ценой"

    def test_create_object_with_price_is_0(self):
        self.create_object_neg.create_object_with_price_is_0()
        self.create_object_neg.check_response_is_400(), "Создался объект с ценой равной 0"

    def test_create_object_with_invalid_price(self):
        self.create_object_neg.create_object_with_invalid_price()
        self.create_object_neg.check_response_is_400(), "Создался объект с невалидной ценой"

    def test_create_object_with_year_is_0(self):
        self.create_object_neg.create_object_with_year_is_0()
        self.create_object_neg.check_response_is_400(), "Создался объект с годом равным 0"

    def test_create_object_with_negative_year(self):
        self.create_object_neg.create_object_with_negative_year()
        self.create_object_neg.check_response_is_400(), "Создался объект с отрицательным годом"

    def test_create_object_with_invalid_year(self):
        self.create_object_neg.create_object_with_invalid_year()
        self.create_object_neg.check_response_is_400(), "Создался объект с невалидным годом"

    def test_create_object_with_invalid_cpu(self):
        self.create_object_neg.create_object_with_invalid_cpu()
        self.create_object_neg.check_response_is_400(), "Создался объект с невалидным cpu"

    def test_create_object_with_invalid_hard_disk(self):
        self.create_object_neg.create_object_with_invalid_hard_disk()
        self.create_object_neg.check_response_is_400(), "Создался объект с невалидным жестким диском"
