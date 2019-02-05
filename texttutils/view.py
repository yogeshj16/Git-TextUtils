
from django.http import HttpResponse


def index(request):
    return HttpResponse("Home to back <a href='/'>back</a>")

def playlist1(request):
    text = """<h1>Python Django Tutorials In Hindi!</h1> <br> <a 
    href="https://www.codewithharry.com/videos/python-django-tutorials-hindi-0">1. Django Course Announcemen...</a> """
    return HttpResponse(text)

def playlist2(request):
    text = """<h1>Python Django Tutorials In Hindi!</h1> <br> <a 
    href="https://www.codewithharry.com/videos/python-django-tutorials-hindi-1">2. Django Installation &amp; Get...</a> """
    return HttpResponse(text)

def playlist3(request):
    text = """<h1>Python Django Tutorials In Hindi!</h1> <br> <a 
    href="https://www.codewithharry.com/videos/python-django-tutorials-hindi-2">3. Creating Our First Django...</a> """
    return HttpResponse(text)

def playlist4(request):
    text = """<h1>Python Django Tutorials In Hindi!</h1> <br> <a 
    href="https://www.codewithharry.com/videos/python-django-tutorials-hindi-3">4. How Django Websites Work ...</a> """
    return HttpResponse(text)

def playlist5(request):
    text = """<h1>Python Django Tutorials In Hindi!</h1> <br> <a 
    href="https://www.codewithharry.com/videos/python-django-tutorials-hindi-4">5. Our First Django Website ...</a> """
    return HttpResponse(text)

def playlist6(request):
    text = """<h1>Python Django Tutorials In Hindi!</h1> <br> <a 
    href="https://www.codewithharry.com/videos/python-django-tutorials-hindi-5">6. Views &amp; Urls In Django| P...</a> """
    return HttpResponse(text)

def playlist7(request):
    text = """<h1>Python Django Tutorials In Hindi!</h1> <br> <a 
    href="https://www.codewithharry.com/videos/python-django-tutorials-hindi-6">7. Django Exercise 1: Person...</a> """
    return HttpResponse(text)

def playlist8(request):
    text = """<h1>Python Django Tutorials In Hindi!</h1> <br> <a 
    href="https://www.codewithharry.com/videos/python-django-tutorials-hindi-7">8. Django Website: Laying Th...</a> """
    return HttpResponse(text)

def playlist9(request):
    text = """<h1>Python Django Tutorials In Hindi!</h1> <br> <a 
    href="https://www.codewithharry.com/videos/python-django-tutorials-hindi-8">9. Django Templates | Python...</a> """
    return HttpResponse(text)

def playlist10(request):
    text = """<h1>Python Django Tutorials In Hindi!</h1> <br> <a 
    href="https://www.codewithharry.com/videos/python-django-tutorials-hindi-9">10. Creating Homepage of our...</a> """
    return HttpResponse(text)


def home(request):
    text = '''<h1>Python Django Tutorials In Hindi! By harry</h1><br/><br/><a href="https://www.codewithharry.com/videos/python-django-tutorials-hindi-0">1. Django Course 
    Announcemen...</a><br/><a href="https://www.codewithharry.com/videos/python-django-tutorials-hindi-1" class="btn 
    btn-light mt-3" role="button">2. Django Installation &amp; Get...</a><br/><a 
    href="https://www.codewithharry.com/videos/python-django-tutorials-hindi-2" class="btn btn-light mt-3" 
    role="button">3. Creating Our First Django...</a><br/><a 
    href="https://www.codewithharry.com/videos/python-django-tutorials-hindi-3" class="btn btn-light mt-3" 
    role="button">4. How Django Websites Work ...</a><br/><a 
    href="https://www.codewithharry.com/videos/python-django-tutorials-hindi-4" class="btn btn-light mt-3" 
    role="button">5. Our First Django Website ...</a><br/><a 
    href="https://www.codewithharry.com/videos/python-django-tutorials-hindi-5" class="btn btn-light mt-3" 
    role="button">6. Views &amp; Urls In Django| P...</a><br/><a 
    href="https://www.codewithharry.com/videos/python-django-tutorials-hindi-6" class="btn btn-light mt-3" 
    role="button">7. Django Exercise 1: Person...</a><br/><a 
    href="https://www.codewithharry.com/videos/python-django-tutorials-hindi-7" class="btn btn-light mt-3" 
    role="button">8. Django Website: Laying Th...</a><br/><a 
    href="https://www.codewithharry.com/videos/python-django-tutorials-hindi-8" class="btn btn-light mt-3" 
    role="button">9. Django Templates | Python...</a><br/><a 
    href="https://www.codewithharry.com/videos/python-django-tutorials-hindi-9" class="btn btn-light mt-3" 
    role="button">10. Creating Homepage of our ...</a> <br/><br/>HOME <a href='/'>Back</a>'''
    return HttpResponse(text)