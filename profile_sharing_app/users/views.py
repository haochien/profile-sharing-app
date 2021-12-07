from django.shortcuts import render

def profiles(request):
    # profiles, search_query = searchProfiles(request)

    # custom_range, profiles = paginateProfiles(request, profiles, 3)
    # context = {'profiles': profiles, 'search_query': search_query,
    #            'custom_range': custom_range}
    return render(request, 'users/profiles.html', context)
