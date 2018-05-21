import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'level2project.settings')

import django
django.setup()

from app_users.models import User
from faker import Faker
fakegen = Faker()


# fakegen is the object of class faker

def populate(N):
    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()
        new_user = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]
if __name__=='__main__':
    populate(20)