from django.db import models
from django.core.validators import URLValidator
import uuid



# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)
    enable_loc = models.BooleanField(default=False, null=False, blank=False)
    frequently_visited = models.CharField(max_length=200, null=False, blank=False)
    use_created = models.DateTimeField(auto_now_add=True)
    use_id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, db_index=True, editable=False
    )
    
    def __str__(self):
        return self.username
    
class Passenger(models.Model):
    current_loc_lat = models.FloatField(null=True, blank=True)
    current_loc_lng = models.FloatField(null=True, blank=True)
    home_loc_lat = models.FloatField( null=True, blank=True)
    home_loc_lng = models.FloatField( null=True, blank=True)
    pas_user = models.OneToOneField(User, on_delete=models.CASCADE)
    pas_created = models.DateTimeField(auto_now_add=True)
    pas_id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, db_index=True, editable=False
    )
    
    def __str__(self):
        return str(self.pas_user)

class Driver(models.Model):
    fullname = models.CharField(max_length=100, null=True, blank=True)
    home_lat = models.FloatField( null=True, blank=True)
    home_lng = models.FloatField( null=True, blank=True)
    license = models.CharField(max_length=200, null=False, blank=False)
    image = models.URLField(max_length=200, null=True, blank=True, validators=[URLValidator()])
    dri_user = models.OneToOneField(User, on_delete=models.CASCADE)
    dri_created = models.DateTimeField(auto_now_add=True)
    dri_id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, db_index=True, editable=False
    )
    
    def __str__(self):
        return self.fullname
    
class Location(models.Model):
    loc_name = models.CharField(max_length=255, null=True, blank=True)
    loc_latitude = models.FloatField(null=True, blank=True)
    loc_longitude = models.FloatField( null=True, blank=True)
    driver = models.ManyToManyField(Driver, blank=True)
    loc_created = models.DateTimeField(auto_now_add=True)
    loc_id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, db_index=True, editable=False
    )
    
    def __str__(self):
        return self.loc_id

class Destination(models.Model):
    des_name = models.CharField(max_length=255, null=True, blank=True)
    des_latitude = models.FloatField(null=True, blank=True)
    des_longitude = models.FloatField( null=True, blank=True)
    passenger = models.OneToOneField(User, on_delete=models.CASCADE)
    des_created = models.DateTimeField(auto_now_add=True)
    des_id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, db_index=True, editable=False
    )
    
    def __str__(self):
        return self.des_name
    
def get_user_details(request):
    pass