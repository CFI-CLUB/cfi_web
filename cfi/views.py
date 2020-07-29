from django.shortcuts import render

def index(request):
    """
    CFI Home page
    :param request:
    :return:
    """
    return render(request, 'cfi/index.html')