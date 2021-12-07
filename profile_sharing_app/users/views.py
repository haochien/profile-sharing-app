from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import Profile
from django.contrib.auth.models import User


def loginUser(request):

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password) # this check user name & password
        
        if user is not None:
            login(request, user)  #this create session and save as cookie in the browser
            return redirect('profile')
        else:
            messages.error(request, 'Username OR password is incorrect')

    return render(request, 'users/login_register.html')



def logoutUser(request):
    logout(request)  #this delete user session 
    messages.info(request, 'User was logged out!')
    return redirect('login')




def profiles(request):
    # profiles, search_query = searchProfiles(request)

    # custom_range, profiles = paginateProfiles(request, profiles, 3)
    # context = {'profiles': profiles, 'search_query': search_query,
    #            'custom_range': custom_range}
    context = {}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")

    context = {'profile': profile, 'topSkills': topSkills,
               "otherSkills": otherSkills}
    return render(request, 'users/user-profile.html', context)