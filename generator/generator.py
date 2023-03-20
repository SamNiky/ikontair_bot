import uuid
from hashlib import md5, sha256


class SecurePassword:

    base_algorithm = uuid.uuid4

    @classmethod
    def generate(cls):
        """
        Генерирует пароль на базе uuid 4-го поколения
        :return: строковое представление uuid4
        """
        return str(cls.base_algorithm())

    @classmethod
    def _generate_by_hash_algorithm(cls, value, hash_type):
        """
        Хэширует значение по выбранному алгоритму
        :param value: строкове значение для хэширования
        :param hash_type: тип алогоритма для хэширования
        :return: строковое представление хэша
        """
        assert isinstance(value, str) and isinstance(hash_type, str), "value and hash_type must be string type"
        assert hash_type.lower() in ["md5", "sha256"], "hash_type must be one of instance (md5, sha256)"
        value = value.encode()
        hash_value = md5(value) if hash_type.lower() == "md5" else sha256(value)
        return hash_value.hexdigest()

    @classmethod
    def generate_by_MD5(cls):
        value = cls.generate()
        return cls._generate_by_hash_algorithm(value, "md5")

    @classmethod
    def generate_by_sha256(cls):
        value = cls.generate()
        return cls._generate_by_hash_algorithm(value, "sha256")
