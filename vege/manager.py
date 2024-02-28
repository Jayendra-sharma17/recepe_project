# from django.contrib.auth.base_user import BaseUserManager

# class Usermanager(BaseUserManager):
#     def create_user(self,Phonenumber,password=None, **extra_fields):
#         if not Phonenumber:
#             raise ValueError("phone number is req")
        
#         extra_fields['emaill']=self.normalize_email(extra_fields['emaill'])
#         user=self.model(Phonenumber=Phonenumber,**extra_fields)
#         user.set_password(password)
#         user.save(using=self.db)
#         return user
    
#     def create_superuser(self,Phonenumber,password=None,**extra_fields):
#         extra_fields.setdefault('is_staff',True)
#         extra_fields.setdefault('is_superuser',True)
#         extra_fields.setdefault('is_active',True)

#         return self.create_user(Phonenumber,password,**extra_fields)



