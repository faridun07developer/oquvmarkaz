from django.urls import path
from blog.views import OqituvchilarRoyxatAPI, OqtuvchilarDetailAPIView, OquvchilarRoyxatAPI, \
    OquvchilarDetailAPIView, OylikRoyxatAPI, DarslarRoyxatAPI, DavomatRoyxatAPI, DarslarDetailAPIView, \
    DavomatDetailAPIView, QabulxonaRoyxatAPI, QabulxonaDetailAPIView, TolovlarRoyxatAPI, \
    XonalarRoyxatAPI


urlpatterns = [
    path('oqtuvchilar/', OqituvchilarRoyxatAPI.as_view()),
    path('oqtuvchilar/<int:pk>', OqtuvchilarDetailAPIView.as_view()),

    path('oquvchilar/', OquvchilarRoyxatAPI.as_view()),
    path('oquvchialr/<int:pk>', OquvchilarDetailAPIView.as_view()),

    path('oylik/', OylikRoyxatAPI.as_view()),

    path('darslar/', DarslarRoyxatAPI.as_view()),
    path('darslar/<int:pk>', DarslarDetailAPIView.as_view()),

    path('davomat/', DavomatRoyxatAPI.as_view()),
    path('davomat/<int:pk>', DavomatDetailAPIView.as_view()),

    path('qabulxoan/', QabulxonaRoyxatAPI.as_view()),
    path('qabulxona/<int:pk>', QabulxonaDetailAPIView.as_view()),

    path('tolovlar/', TolovlarRoyxatAPI.as_view()),

    path('xonalar/', XonalarRoyxatAPI.as_view()),
]
