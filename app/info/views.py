from django.shortcuts import render, get_object_or_404
from info.models import About, Writing

def home(request):
    about = get_object_or_404(About, pk=1)
    context = {"about": about}
    return render(request, "info/home.html", context)

def writing_overview(request):
    writing_categories = Writing.Category
    writing_by_category = {}
    for category in writing_categories:
        in_category = (
            Writing.objects.filter(category=category)
                           .order_by("-date_published")
        )
        writing_by_category.update({category: in_category})
    context = {"writing_by_category": writing_by_category}
    return render(request, "info/writing_overview.html", context)

