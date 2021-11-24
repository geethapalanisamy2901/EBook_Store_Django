from django.http.response import HttpResponse, JsonResponse
from django.views import View
from django.conf import settings
from django.shortcuts import render
import pymongo
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages

# from ebook_store.ebookstore.preview.models import BookDetails
from .forms import SignUpForm
import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://hari:123@py.7qlld.mongodb.net/donjo_test?retryWrites=true&w=majority")


database = client['djongo_test']

# bookdetails = database['book_library_bookdetails']
userdetails = database['book_library_userdetails']


def home(request):
    bookdetails = client.djongo_test.book_library_bookdetails.find({})
    post_book = {
        'bookdetail': bookdetails
    }
    return render(request, 'home.html', post_book)


def preview(request, idbook):
    datad = client.djongo_test.book_library_bookdetails.find_one({
                                                                 "id": idbook})
    context = {
        "book": datad
    }
    return render(request, 'preview/preview.html', context)


def cartupdate(request, user, idbook):
    userdetails.update(
        {"id": user},
        {"$push": {
            "cart": idbook}
         }
    )
    return HttpResponse('Successfully updated', request)


def cartlist(request, iduser):

    cart_list = []
    datad = client.djongo_test.book_library_userdetails.find_one({
        "id": iduser})
    data2 = datad['cart']
    for books in data2:
        data_cart = client.djongo_test.book_library_bookdetails.find_one({
            "id": books})
        cart_list.append(data_cart)
        post_book = {
            'cart_item': cart_list,
        }

    return render(request, 'cart.html', post_book)


def lib(request, iduser):
    book = []
    datad = client.djongo_test.book_library_userdetails.find_one({
        "id": iduser})
    data1 = datad['library']

    for books in data1:
        data = client.djongo_test.book_library_bookdetails.find_one({
            "id": books})
        book.append(data)
        post_book = {
            'bookk': book,
        }
    return render(request, 'libdesign.html', post_book)


def login_user(request):

    if request.method == 'POST':  # if someone fills out form , Post it
        username = request.POST.get('username')
        password = request.POST.get('password3')

        if username is not None:  # if user exist
            # login(request,username)
            #current_user = request.user
            #user_id = current_user.id
            # print(user_id)
            text = 'Hello, World'
            messages.success(request, text)
            return redirect('home')  # routes to 'home' on successful login
        else:
            messages.success(request, ('Error logging in'))
            # re routes to login page upon unsucessful login
            return redirect('login')
    else:
        return render(request, 'login/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ('You''re now logged out'))
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Youre now registered'))
            return redirect('home')
    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'login/register.html', context)
