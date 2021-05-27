import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE','demoproject.settings')
django.setup()

from userdata.models import User
from faker import Faker

fakedata = Faker()

def populateData(n=10):

    for entry in range(n):
        fake_firstname=fakedata.first_name()
        fake_lastname = fakedata.last_name()
        fake_email = fakedata.email()

        fake_user = User.objects.get_or_create(firstname=fake_firstname, lastname=fake_lastname, email=fake_email)[0]
        fake_user.save()
        


if __name__ == '__main__':
    print("Populating data")
    populateData()
    print("Population complete")




