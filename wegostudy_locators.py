import datetime
import subprocess
from faker import Faker
fake = Faker(locale=['en_CA','en_US'])


app = 'WeGoStudy'
wegostudy_url = 'https://www.wegostudy.ca/'
wegostudy_home_page_title = 'WeGoStudy'
user_name = 'Joshua Thomas Bailey'
user_email = 'svglaz@yahoo.ca'
user_password = 'testpassword2'
partner_home_page = 'https://www.wegostudy.ca/partner/home'
partner_student_details_page = 'https://www.wegostudy.ca/partners/student_details'
partner_new_student_page = 'https://www.wegostudy.ca/partners/student_details/new'
partner_details_page = 'https://www.wegostudy.ca/partners/partner_details/testpartner-a6d899cd-c8aa-4ed0-87c7-bafea8aca8ae'
partner_admissions ='https://www.wegostudy.ca/partners/admissions'

first_name = fake.first_name()
middle_name = fake.first_name()
last_name = fake.last_name()
preferred_name = f'{first_name} {last_name}'
full_name = f'{first_name} {middle_name} {last_name}'

date_of_birth = '2000-11-12'
passport_number = fake.pyint(111111,999999)

phone_number = fake.phone_number()[:10]

aprt_number = fake.pyint(1,300)
building_number = fake.building_number()
street = fake.street_name()
mailing_address = f'{building_number} {street}'
postal_code = fake.postalcode()
email_address = fake.email()

job_description = fake.sentence(nb_words=50)

path = subprocess.check_output('pwd', shell=True, text=True)

image_1 = path.strip()+'/upload/StudentImage.png'
image_2 = path.strip()+'/upload/avatar.jpg'
document_1 = path.strip()+'/upload/TestDocument_1.pdf'
document_2 = path.strip()+'/upload/TestDocument_2.pdf'

organization = fake.company()
birth_date = fake.day_of_month()+ '-' + fake.month() + '-' + fake.year()


def get_random_passport_number():
    return fake.pyint(111111, 999999)


invalid_logins = [
    {
        'email': 'chris.velasco78gmail.com',
        'password': 'P@r0la000'
    },
    {
        'email': 'chris.velasco78@gmail.com',
        'password': 'P@r0la000'
    },
    {
        'email': ' ',
        'password': 'P@r0la000'
    },
    {
        'email': 'constantinrox.iasi@gmail.com',
        'password': '123password'
    },
    {
        'email': 'constantinrox.iasi@gmail.com',
        'password': ' '
    },
    {
        'email': ' ',
        'password': ' '
    },
    {
        'email': 'chris.velasco78gmail.com',
        'password': '123password'
    },
    {
        'email': ' ',
        'password': '123password'
    },
    {
        'email': 'chris.velasco78@gmail.com',
        'password': ' '
    },
    {
        'email': 'chris.velascigmail.com',
        'password': ' '
    }
]

apartment_num = fake.building_number()

schoollist = ["CCTB", "UBC", "SFU", "VCC", "MMU"]
programlist = ["MBA", "SQA","web design", "UI/UX"]
credentiallist = ["Certificate", "Diploma", "Degree", "Master", "Doctoral"]
GPAscales = [4, 5, 10, 100]
languages = ["English", "French", "Spanish"]
service = fake.catch_phrase()
iccrc = fake.ean(length=8)


student_name = 'Kenneth Andrew Kim'
college_ID = fake.pyint(1, 200)
study_permit = fake.pyint(1, 500)
admitted_date = '06-20-2022'
band_score = '6'
listening_score = '5'
reading_score = '4'
writing_score = '5'
speaking_score = '6'
relationship = 'Uncle'

std_name = 'Jonathan'
a = datetime.datetime(2022, 6, 5)
start_date = a.strftime("%Y/%m/%d")
b = datetime.datetime(2022, 6, 30)
end_date = b.strftime("%Y/%m/%d")

