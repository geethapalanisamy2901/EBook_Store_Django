from django.http.response import JsonResponse
from django.views import View
from django.conf import settings
from django.shortcuts import render
import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://hari:123@py.7qlld.mongodb.net/donjo_test?retryWrites=true&w=majority")


database = client['djongo_test']

bookdetails = database['book_library_bookdetails']
userdetails = database['book_library_userdetails']

book = []
cart_list = []
datad = client.djongo_test.book_library_userdetails.find_one({
    "id": 1})
data1 = datad['library']
data2 = datad['cart']
print(data1)
for books in data1:
    data = client.djongo_test.book_library_bookdetails.find_one({
        "id": books})
    book.append(data)
    # print(book)
for books in data2:
    data_cart = client.djongo_test.book_library_bookdetails.find_one({
        "id": books})
    cart_list.append(data_cart)
post_book = {
    'bookk': book,
    'cart_item': cart_list
}


def preview(request, idbook):
    datad = client.djongo_test.book_library_bookdetails.find_one({
                                                                 "id": idbook})
    context = {
        "book": datad
    }
    return render(request, 'preview/preview.html', context)


def cartlist(request):
    userdetails.update(
        {"id": 1},
        {"$push": {
            "cart": 4}
         }
    )
    return render(request, 'cart.html', post_book)


def lib(request):

    return render(request, 'libdesign.html', post_book)


def home(request):
    allbooks = client.djongo_test.book_library_bookdetails.find()
    books = []
    for data in allbooks:
        books.append(data)

    context = {
        "book": books
    }
    print(books)
    return render(request, 'home.html', context)
