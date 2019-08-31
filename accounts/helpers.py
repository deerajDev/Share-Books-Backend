from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validatePhoneNum(contact_num):
    number = str(contact_num)
    if number[0]==0 or len(number)<10:
        raise ValidationError(f'{number} is Invalid contact number')


def  updateUser(instance, new_data):
        instance.email = new_data.get('email', instance.email)
        instance.college = new_data.get('college', instance.college)
        contact_num  = new_data.get('contact_num', instance.contact_num)
        if not(str(contact_num)[0]==0) and (len(str(contact_num))==10):
                print(len(str(contact_num)))
                instance.contact_num = contact_num
        instance.save()
        return instance
