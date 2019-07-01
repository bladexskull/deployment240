import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','pro2.settings')

import django
django.setup()


from apptwo.models import User
from faker import Faker

fakeobj = Faker()


def populate(N=5):

    for k in range(N):
        Name = fakeobj.name()
        fname=Name.split()[0]
        lname=Name.split()[1]
        mail=fakeobj.email()

        obj = User.objects.get_or_create(firstname=fname,lastname=lname,email=mail)[0]

if __name__=='__main__':
print("populating")
populate(15)
print("population done")
