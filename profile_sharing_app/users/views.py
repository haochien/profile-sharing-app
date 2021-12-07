from django.shortcuts import render
from .models import Profile


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