from django.urls import path, include
from .controllers import person, collection


urlpatterns = [
    # path('hello/', person.say_hello),
    # path('html/', person.say_html),

    path('userLogin/', person.PersonController.userLogin),

    path('uploadFileCollection/', collection.CollectionController.uploadFileCollection ),
    path('getAllCollection/', collection.CollectionController.getAllCollection),
    path('deleteCollection/', collection.CollectionController.deleteCollection),

]