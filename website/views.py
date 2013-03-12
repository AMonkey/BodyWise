from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import *
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
import logging
from models import User
#from django.contrib.auth.models import User

logger = logging.getLogger('term')

class HomePage(View):
    def get(self, request):
        if request.user.is_authenticated():
            log = request.GET.get('logout', None)
            if log is not None:
                logout(request)
                return redirect('/splash')

            return render(request, 'website/homepage.html')

        else:
            return redirect('/splash')

class Splash(View):
    def get(self, request):
        return render(request, 'website/splash.html')

    def post(self, request):
        # Get values
        user = request.POST.get('username', None)
        passwd = request.POST.get('password', None)
        check = request.POST.get('password_check', None)
        email = request.POST.get('email', None)

        # Email doesn't exist, POST was for login
        if email is None and user is not None and passwd is not None:
            logger.debug('Login POST recieved!')
            u = authenticate(username=user, password=passwd)
            if u is not None:
                if u.is_active:
                    login(request, u)
                    return redirect('/')

                else:
                    error = 'Account is disabled. Please contact admins for' +\
                        ' more information.'
                    return render(request, 'website/splash.html',
                        {'login_error': error})
            else:
                error = 'Username or password is incorrect.'
                return render(request, 'website/splash.html',
                    {'login_error': error})

                

        # Email exists, POST was for registration
        if passwd == check and passwd is not None and user is not None:
            logger.debug('Register POST recieved!')
            # Create user
            try:
                makeUser(user, email, passwd)
            except:
                error = 'Problem creating user'
                return render(request, 'website/splash.html', {'register_error':
                    error})
            u = authenticate(username=user, password=passwd)

            # Log user in-> TODO: send verifciation email
            login(request, u)
            return redirect('/')

        logger.warning('Reached end of POST, not supposed to.')
        logger.warning('user: %s | passwd: %s | check: %s | email: %s ' %
            (user, passwd, check, email))

def makeUser(u, e, p):
    if u is not '' and p is not '':
        u = User.objects.create_user(u, email=e)
        u.set_password(p)
        u.is_active = True
        u.save()
