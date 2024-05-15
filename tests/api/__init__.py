from faker import Faker

fake = Faker()


class UserCredentials:
    username = fake.simple_profile().get("username")
    password = fake.password
