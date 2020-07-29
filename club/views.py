from django.shortcuts import render, render_to_response, reverse, redirect, get_object_or_404
from club.models import Project, CFIProject
from club.forms import ProjectForm, ContactusForm
from django.core.paginator import Paginator
import datetime


def index(request):
    """

    :param request:
    :return:

    Home page
    Contains 2 form: Idea Submission, Contact us
    """

    project_list = Project.objects.order_by('-views')[:3]
    now = datetime.datetime.now()
    sristi_date = now.year - 2009

    form = ContactusForm()
    if request.method == 'POST':
        form = ContactusForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('club:index')
        else:
            print(form.errors)

    form2 = ProjectForm()
    if request.method == 'POST':
        form2 = ProjectForm(request.POST, request.FILES)

        if form2.is_valid():
            data = form2.save(commit=False)
            data.save()

            return redirect('club:index')
        else:
            print(form2.errors)

    cfi_projects = CFIProject.objects.all()[:8]

    context_dict = {
        'projects': project_list,
        'cfi_projects': cfi_projects,
        'year': now.year,
        'sristi_date': sristi_date,
        'form': form,
        'form2': form2
    }
    return render(request, 'club/index.html', context=context_dict)

def blog(request, title_slug):
    """

    :param request:
    :param title_slug:
    :return:

    Idea page
    """

    blog = get_object_or_404(Project, slug=title_slug)
    context_dict = {
        'blog' : blog
    }
    return render(request, 'club/blog.html', context=context_dict)


def blog_list(request):
    """

    :param request:
    :return:

    List of all blog
    Cotain 1 form: Idea Submission
    """

    blogs = Project.objects.order_by("-created")
    paginator = Paginator(blogs, 5)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)

    form2 = ProjectForm()
    if request.method == 'POST':
        form2 = ProjectForm(request.POST, request.FILES)

        if form2.is_valid():
            data = form2.save(commit=False)
            data.save()

            return redirect('club:index')
        else:
            print(form2.errors)

    context_dict = {
        'blogs' : blogs,
        'form2' : form2
    }

    return render(request, "club/blog-list.html", context=context_dict)


def submit_ideas(request):
    """

    :param request:
    :return:
    Submit an Idea
    """

    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.save(commit=False)
            data.save()

            return redirect('club:index')
        else:
            print(form.errors)

    context_dict = {'form': form}
    return render(request, "club/submit_idea.html", context=context_dict)


def goto_url(request):
    """

    :param request:
    :return:

    Views counter for blog
    """
    blog = None
    url='/club/'
    if request.method == 'GET':

        blog_id = request.GET['blog_id']

        try:
            blog = Project.objects.get(pk=blog_id)
            blog.views += 1
            blog.save()
            url = f'/club/{blog.slug}'
        except Project.DoesNotExist:
            return redirect(reverse('club:index'))
        return redirect(reverse('club:blog', args=(blog.slug,)))

def handler404(request, exception, template_name="club/error404.html"):
    """

    :param request:
    :param exception:
    :param template_name:
    :return:

    Error404 custom page
    """
    response = render_to_response("club/error404.html")
    response.status_code = 404
    return response