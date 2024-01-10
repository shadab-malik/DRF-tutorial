from django.urls import path

from book_api.views import BookList, BookCreate, ById
# from book_api.views import book, getList, create

urlpatterns = [
    path('', BookCreate.as_view()),
    path('list/', BookList.as_view()),
    path('<int:pk>', ById.as_view()),
    # path("", create),
    # path("list/", getList),
    # path("<int:pk>", book),
]
