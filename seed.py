from faker import Faker
import os
import django
import random
f= Faker()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'btre.settings')
django.setup()
from listings.choices import *
from listings.models import Listing
from realtors.models import Realtor

# for i in range(6):
#     Realtor.objects.get_or_create(name=f.name(), description=f.paragraph(nb_sentences=5), email=f.email(), phone=f.phone_number())

# all_realtors= Realtor.objects.all()
# for i in range(25):
#     Listing.objects.get_or_create(realtor=random.choice(all_realtors) ,title=f.paragraph(nb_sentences=1),address=f.address(), city=f.city(), state=f.state(), zipcode=f.zipcode(), description=f.paragraph(nb_sentences=5), price=random.choice(list(price_choices)), bedrooms=random.choice(list(bedroom_choices)), bathrooms=random.randint(1,4), garage=random.randint(1,3), sqrft=random.randint(800, 1500), lot_size=random.randint(1,5))


# for listing in Listings.objects.all():
#     Listing.objects.update(photo_main=)