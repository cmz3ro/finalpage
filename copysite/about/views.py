from django.shortcuts import render
from django.contrib import auth
from about.models import Contact_page
# Create your views here.
def new1(request):
    return render(request, 'about.html')

def contacts(request):
    args ={}
    args['first_pages'] = 'active'
    args['username'] = auth.get_user(request).username
    args['page_cont'] = Contact_page.objects.all()
    return render(request, 'contacts.html',args)

def add_contact(request):
    contac = {'message_acess':"Ваше сообщение отправленно"}
    if request.method == 'POST':
        user_name = request.POST.get('name')
        user_email = request.POST.get('email')
        user_message = request.POST.get('message')
        b = Contact_page(name=user_name,email = user_email ,message= user_message )
        b.save()

    return render(request, 'contacts.html',contac)