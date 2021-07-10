from django.db import models
from django.conf import settings
from PIL import Image
# Create your models here.

Bus_choice = [
    ('Club','Club/Pub'),
    ('Cosmetics','Cosmetics'),
    ('Food','Food'),
    ('LiquorStore','liquor store'),
    ('Salon','Salon'),


]

Province_choice = [
    ('Northwest', 'Northwest'),
    ('Gauteng', 'Gauteng'),
    ('FreeState', 'FreeState'),
    ('EasternCape', 'EasternCape '),
    ('KwaZulu-Natal', 'KwaZulu-Natal'),
    ('Limpopo', 'Limpopo'),
    ('Mpumalanga', 'Mpumalanga'),
    ('NorthernCape', 'NorthernCape'),
    ('WesternCape', 'WesternCape'),
]

City_choice = [
    ('Mafikeng', 'Mafikeng northwest'),
    ('Mmabatho', 'Mmabatho northwest'),
    ('Rustenburg', 'Rustenburg northwest'),
    ('Potchefstroom', 'Potchefstroom northwest'),
    ('Klerksdorp', 'Klerksdorp northwest'),

    ('Johannesburg', 'Johannesburg Gauteng'),
    ('Krugersdorp', 'Krugersdorp Gauteng'),
    ('Pretoria', 'Pretoria Gauteng'),
    ('Randburg', 'Randburg Gauteng'),
    ('Randfontein', 'Randfontein Gauteng'),
    ('Roodepoort', 'Roodepoort Gauteng'),
    ('Soweto', 'Soweto Gauteng'),
    ('Springs', 'Springs Gauteng'),
    ('Vanderbijlpark', 'Vanderbijlpark Gauteng'),
    ('Vereeniging', 'Vereeniging Gauteng'),
    ('Germiston', 'Germiston Gauteng'),
    ('Carletonville', 'Carletonville Gauteng'),
    ('Brakpan', 'Brakpan Gauteng'),
    ('Boksburg', 'Boksburg Gauteng'),
    ('Benoni', 'Benoni Gauteng'),

    ('Bloemfontein', 'Bloemfontein FreeState'),
    ('Bethlehem', 'Bethlehem FreeState'),
    ('Jagersfontein', 'Jagersfontein FreeState'),
    ('Kroonstad', 'Kroonstad FreeState'),
    ('Odendaalsrus', 'Odendaalsrus FreeState'),
    ('Parys', 'Parys FreeState'),
    ('Phuthaditjhaba', 'Phuthaditjhaba FreeState'),
    ('Sasolburg', 'Sasolburg FreeState'),
    ('Virginia', 'Virginia FreeState'),
    ('Welkom', 'Welkom FreeState'),

    ('Alice', 'Alice EasternCape'),
    ('Butterworth', 'Butterworth EasternCape'),
    ('EastLondon', 'EastLondon EasternCape'),
    ('Graaff-Reinet', 'Graaff Reinet EasternCape'),
    ('Grahamstown', 'Grahamstown EasternCape'),
    ('King-William’s-Town', 'King-William’s-Town EasternCape'),
    ('Mthatha', 'Mthatha EasternCape'),
    ('Port-Elizabeth', 'Port-Elizabeth EasternCape'),
    ('Queenstown', 'Queenstown EasternCape'),
    ('Uitenhage', 'Uitenhage EasternCape'),
    ('Zwelitsha', 'Zwelitsha EasternCape'),

    ('Durban', 'Durban KwaZulu-Natal'),
    ('Empangeni', 'Empangeni KwaZulu-Natal'),
    ('Ladysmith', 'Ladysmith KwaZulu-Natal'),
    ('Newcastle', 'Newcastle KwaZulu-Natal'),
    ('Pietermaritzburg', 'Pietermaritzburg KwaZulu-Natal'),
    ('Pinetown', 'Pinetown KwaZulu-Natal'),
    ('Ulundi', 'Ulundi KwaZulu-Natal'),
    ('Umlazi', 'Umlazi KwaZulu-Natal'),

    ('Giyani', 'Giyani Limpopo'),
    ('Lebowakgomo', 'Lebowakgomo Limpopo'),
    ('Musina', 'Musina Limpopo'),
    ('Phalaborwa', 'Phalaborwa Limpopo'),
    ('Polokwane', 'Polokwane Limpopo'),
    ('Seshego', 'Seshego Limpopo'),
    ('Sibasa', 'Sibasa Limpopo'),
    ('Thabazimbi', 'Thabazimbi Limpopo'),

    ('Emalahleni', 'Emalahleni Mpumalanga'),
    ('Nelspruit', 'Nelspruit Mpumalanga'),
    ('Secunda', 'Secunda Mpumalanga'),

    ('Kimberley', 'Kimberley NorthernCape'),
    ('Kuruman', 'Kuruman NorthernCape'),
    ('PortNolloth', 'PortNolloth NorthernCape'),

    ('Cape-Town', 'Cape-Town WesternCape'),
    ('Bellville', 'Bellville WesternCape'),
    ('Constantia', 'Constantia WesternCape'),
    ('George', 'George WesternCape'),
    ('Hopefield', 'Hopefield WesternCape'),
    ('Oudtshoorn', 'Oudtshoorn WesternCape'),
    ('Paarl', 'Paarl WesternCape'),
    ('Simon’s-Town', 'Simon’s-Town WesternCape'),
    ('Stellenbosch', 'Stellenbosch WesternCape'),
    ('Swellendam', 'Swellendam WesternCape'),
    ('Worcester', 'Worcester WesternCape'),

]

gender_choice = [

    ('Female','Female'),
    ('Male','Male'),
]


class BusinessProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='businesspro')
    business_name = models.CharField(max_length=100, blank=False, null=False, default='businessName')
    logo = models.ImageField(upload_to='businesslogos', height_field=None, width_field=None, max_length=None,
                             default='businesslogos/business.jpg')
    Product1 = models.ImageField(upload_to='profileproducts', height_field=None, width_field=None, max_length=None, default='profileproducts/product.png')
    Product2 = models.ImageField(upload_to='profileproducts', height_field=None, width_field=None, max_length=None, default='profileproducts/product.png')
    Product3 = models.ImageField(upload_to='profileproducts', height_field=None, width_field=None, max_length=None, default='profileproducts/product.png')
    Product4 = models.ImageField(upload_to='profileproducts', height_field=None, width_field=None, max_length=None, default='profileproducts/product.png')
    type_of_business = models.CharField(max_length=200, choices=Bus_choice, blank=False, null=True)
    description = models.TextField(blank=False, null=False,default="description")
    phone_number = models.IntegerField(null=True, blank=False)
    business_email = models.EmailField(null=True, max_length=254, blank=True)
    office_number =models.IntegerField(null=True, blank=True)
    fax = models.IntegerField(null=True, blank=True)
    operating_hours = models.TextField(blank=True, null=True)
    recommendations = models.IntegerField(default=0,blank=True)
    streetname = models.CharField(max_length=200, default="streetname")
    suburb = models.CharField(max_length=200,default="suburb")
    city = models.CharField(max_length=200, choices=City_choice,default="city")
    province = models.CharField(max_length=200, choices=Province_choice,default="province")
    latitude = models.FloatField(default=0.0,blank=True)
    longitude = models.FloatField(default=0.0,blank=True)
    Complete = models.IntegerField(default=0,blank=True)

    def __str__(self):
        return f'{self.user} profile'


class CustomerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='customerpro')
    gender  = models.CharField(choices=gender_choice, max_length=50,null=True,blank=False)
    age = models.IntegerField(null=True, blank=False)
    residence= models.CharField(choices=City_choice, max_length=200,null=True,blank=False)
    cellPhone_number = models.IntegerField(verbose_name="cell phone number",null=True)


    def __str__(self):
        return f'{self.user} profile'

