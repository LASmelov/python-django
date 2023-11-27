from django.shortcuts import render, get_object_or_404, redirect
from .models import Developer
from .models import Manager
from .models import Project, Card
from .forms import DescriptionForm, SectionForm, CardForm
from .forms import CardForm, SectionForm
from .models import Project



# Create your views here.


def index(request):
    sections = Project.objects.all()
    section_id = request.GET.get('section')
    if section_id:
        cards = Card.objects.filter(section_id=section_id).order_by('name')
    else:
        cards = Card.objects.all().order_by('name')
    context = {
        "sections": sections,
        "cards": cards,
        "selected_section_id": section_id
    }
    return render(request, "index.html", context)

def index(request):
    # if request.method == "POST":
    #     company.description = request.POST.get("description")
    #     company.save()
    projects = Project.objects.all()
    cards = Card.objects.all()
    return render(
        request,
        template_name="index.html",
        # context={"description": company.description},
        context={"projects": projects, "cards": cards},
    )


def projects(request):
    projects = Project.objects.all()
    return render(
        request,
        template_name="projects.html",
        context={"projects": projects},
    )



def projects_info(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects_info.html', context)

def develop_detail(request, pk):
    develop_id = (Developer.objects.get(pk=pk),)
    manager_id = Manager.objects.get(pk=pk)

    return render(
        request,
        template_name="develop_detail.html",
        context={"develop": develop_id, "manager": manager_id},
    )


def add_section(request):
    if request.method == "POST":
        form = SectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_card')
    else:
        form = SectionForm()
    context = {
        "form": form,
    }
    return render(request, "add_section.html", context)

def add_card(request):
    if request.method == "POST":
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            card = form.save(commit=False)
            section_id = request.POST.get('section')
            section = Project.objects.get(id=section_id)
            card.section = section
            card.save()
            return redirect('index')
    else:
        sections = Project.objects.all()
        form = CardForm(initial={'section': sections[0].id if sections else None})
    context = {
    "form": form,
    "sections": sections
    }
    return render(request, "add_card.html", context)

def catalog_develop(request):
    sections = Project.objects.all()  # получаем все секции из базы данных
    cards = Card.objects.all()  # получаем все карточки из базы данных
    develops = Developer.objects.all()
    return render(
        request,
        template_name="catalog_list.html",
        context={"develops": develops, "sections": sections, "cards": cards},
    )


def develop_detail(request, pk):
    develop_id = get_object_or_404(Developer, pk=pk)
    sections = Project.objects.filter(
        card__develop=develop_id
    )  # получаем все секции, связанные с данным разработчиком
    cards = Card.objects.filter(
        develop=develop_id
    )  # получаем все карточки, связанные с данным разработчиком
    return render(
        request,
        template_name="develop_detail.html",
        context={"develop": develop_id, "sections": sections, "cards": cards},
    )


def catalog_view(request):
    sections = Project.objects.all()
    cards = Card.objects.all()
    develops = Developer.objects.all()
    managers = Manager.objects.all()
    return render(
        request,
        template_name="catalog_list_view.html",
        context={
            "develops": develops,
            "managers": managers,
            "sections": sections,
            "cards": cards,
        },
    )


def catalog_list_view(request):
    develops = Developer.objects.all()
    managers = Manager.objects.all()
    return render(
        request,
        template_name="catalog_list_view.html",
        context={"develops": develops, "managers": managers},
    )


def manager(request):
    managers = Manager.objects.all()
    return render(
        request,
        template_name="manager.html",
        context={"managers": managers},
    )
