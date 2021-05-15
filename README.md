# Django-Djoser-User-Registration-Module
Rewriting a user registration is stressful. So I have created this module that would help you carry out user registration using Django Djoser. 

In your you Django project, install Djoser and Django rest-framework.

Copy the `accounts` folder and place it in your django project.

Add the following to your INSTALLED_APPS in the `settings.py` file.
```
    # rest API implementation lib for django
    'rest_framework',
    'rest_framework.authtoken',

    # third party package for user registration and authentication endpoints
    'djoser',

    # created apps
    'accounts',
 ```
 Also add the following at the bottom of the `settings.py` file:
 
 ```
     ##################################
     # CUSTOM AUTHENTICATION SETTINGS #
     ##################################

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.TokenAuthentication',
        ),
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.IsAuthenticated',
        ),
    }

    DJOSER = {
        'LOGIN_FIELD': 'email',
        'SERIALIZERS': {
            # 'user_registration': 'accounts.serializers.NewUserSerializer',  
            # 'user': 'accounts.serializers.UserCreateSerializer',
            # 'current_user': 'authentication.serializers.CurrentUserSerializer' 
        }
    }
    AUTH_USER_MODEL = 'accounts.NewUser'
    
```

RUN `python manage.py makemigrations` and after that `python manage.py migrate` in the terminal

START THE SERVER `python manager.py runserver`

TEST IN POSTMAN:
![Screenshot 2021-05-15 at 23 50 33](https://user-images.githubusercontent.com/58259539/118380269-5a734800-b5d8-11eb-851b-45d04b785847.png)


You can add more fields to `accounts/models.py` by adding more fiedls to the following sections:

```
class NewUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    username = models.CharField(null=True, blank=True, max_length=30, unique=True)
    [more fields like first_name, last_name, phone_number etc]
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = NewUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email
```

FEEL FREE TO CONTRIBUTE TO THIS AND MAKE IT BETTER.
THANK YOU.

    
   
    
 
