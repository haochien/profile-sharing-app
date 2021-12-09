from .models import Project, Tag
from django.db.models import Q

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def searchProjects(request):

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains=search_query)

    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tags__in=tags)
    )
    return projects, search_query


def paginateProjects(request, projects, results):

    page = request.GET.get('page')
    paginator = Paginator(projects, results)  # x results per page

    try:
        projects = paginator.page(page)   # show the records for the x page (use projects.number can get number x)
    except PageNotAnInteger:  # if page number is not provided
        page = 1
        projects = paginator.page(page)
    except EmptyPage:  # if page number out of max page
        page = paginator.num_pages  # how many pages we have. i.e. last page
        projects = paginator.page(page)

    # only show certain range of pagination list to prevent too many pagination button
    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:   # paginator.num_pages provides range of page, i.e. list(1,3)
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, projects