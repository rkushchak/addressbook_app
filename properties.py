import random_test_data


user="admin"
password="secret"
_url="http://localhost/index.php"

e_mail = (random_test_data.random_letters(6) + '@' + random_test_data.random_letters(5) + '.com') # generate random email
phone_number = random_test_data.random_number(11)  # generate random phone number
f_name = random_test_data.random_letters(6) # generate First name
m_name = random_test_data.random_letters(5) # generate Middle name
l_name = random_test_data.random_letters(7) # generate Last name