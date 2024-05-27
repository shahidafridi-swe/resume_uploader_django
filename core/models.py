from django.db import models

STATE_CHOICE = (
    ('Dhaka', 'Dhaka'),
    ('Rajshahi', 'Rajshahi'),
    ('Chittagong', 'Chittagong'),
    ('Khulna', 'Khulna'),
    ('Barisal', 'Barisal'),
    ('Sylhet', 'Sylhet'),
    ('Rangpur', 'Rangpur'),
    ('Mymensing', 'Mymensing'),
)

class Resume(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=10)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField()
    state = models.CharField(choices=STATE_CHOICE, max_length=50)
    mobile = models.CharField(max_length=11)
    email = models.EmailField()
    job_city = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='profileImages', blank=True)
    file = models.FileField(upload_to='files', blank=True)


