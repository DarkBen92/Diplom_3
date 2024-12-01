from precondition.credentials_generators import generator_login_email, generator_password, generator_name


def body_data_user():
    payload = {
        "email": generator_login_email(),
        "password": generator_password(),
        "name": generator_name()
    }
    return payload


def change_number(new_number, first_number) -> bool:
    if new_number > first_number:
        return True
    else:
        return False
