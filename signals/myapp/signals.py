from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
 
'''
User login signal implimentated here

'''

@receiver(user_logged_in,sender=User) #2nd way to connect signal using decorator
def login_success(sender, request,user,**kwargs):
    print("-----------------------------------------------------")

    print("logged-in-signals.......Run Intro.")
    print("Sender:",sender)
    print("request:",request)
    print("user:",user)
    print(f'kwargs: {kwargs}')




# user_logged_in.connect(login_success , sender=User) #connect signal using manually connector 1st way



'''
User logout signal implimentated here
'''

@receiver(user_logged_out,sender=User) #2nd way to connect signal using decorator
def log_out(sender, request,user,**kwargs):
    print("-----------------------------------------------------")

    print("logged -out-signals.......Run outro.")
    print("Sender:",sender)
    print("request:",request)
    print("user:",user)
    print(f'kwargs: {kwargs}')


# user_logged_out.connect(log_out , sender=User) #connect signal using manually connector 1st way




'''
User loginfaild signal implimentated here
'''

@receiver(user_login_failed) #2nd way to connect signal using decorator
def login_faild(sender, request,credentials,**kwargs):
    print("-----------------------------------------------------")

    print("logged-in-faild- signals.")
    print("Sender:",sender)
    print("request:",request)
    print("credentials:",credentials)
    print(f'kwargs: {kwargs}')


# user_login_failed.connect(log_out , sender=User) #connect signal using manually connector 1st way
