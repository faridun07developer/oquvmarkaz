from django.shortcuts import render
from rest_framework.response import Response
from django.http import Http404
from blog.serializer import OqituvchilarSerializer, OquvchilarSerializer, OylikSerializer, TolovlarSerializer, \
    DavomatSerializer, XonalarSerializer, QabulxonaSerializer, DarslarSerializer, AccountSerializer
from blog.models import Account, Oquvchilar, Oqtuvchilar, Oylik, Tolovlar, Davomat, \
    Qabulxona, Xonalar, Darslar
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
# Create your views here.


class OqituvchilarRoyxatAPI(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        oqtuvchilar = Oqtuvchilar.objects.all()
        oqtuvchilar = OqituvchilarSerializer(oqtuvchilar, many=True).data
        oqtuvchilar = {
            "status": f"Qaytarilgan malumotlar soni {len(oqtuvchilar)} ga teng",
            "natijalar": oqtuvchilar
        }
        return Response(oqtuvchilar)

    def post(self, request):
        oqtuvchilar = OqituvchilarSerializer(data=request.data)
        if oqtuvchilar.is_valid():
            oqtuvchilar.save()
            return Response(oqtuvchilar.data, status=status.HTTP_201_CREATED)
        return Response(oqtuvchilar.errors, status=status.HTTP_400_BAD_REQUEST)


class OqtuvchilarDetailAPIView(APIView):
    #bironta id dagi malumotni charish uchun
    def get_object(self, pk):
        try:
            return Oqtuvchilar.objects.get(pk=pk)
        except Oqtuvchilar.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        oqtuvchilar = self.get_object(pk)
        serializer = OqituvchilarSerializer(oqtuvchilar).data
        data = {
            'natija': serializer
        }
        return Response(data)

    # bironta id dagi malumotni o'zgartirish uchun
    def put(self, request, pk):
        oqtuvchilar = self.get_object(pk)
        serializer = OqituvchilarSerializer(oqtuvchilar, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': f"{oqtuvchilar.name} o'zgartirildi",
                'natija': serializer.data
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # bironta id dagi malumotni o'chirish uchun
    def delete(self, request, pk):
        oqtuvchilar = self.get_object(pk)

        data = {
            'xabar': f"{oqtuvchilar.name}ning malumotlari o'chirildi!"
        }
        oqtuvchilar.delete()
        return Response(data)


class OquvchilarRoyxatAPI(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        oquvchilar = Oquvchilar.objects.all()
        oquvchilar = OquvchilarSerializer(oquvchilar, many=True).data
        oquvchilar = {
            "status": f"Qaytarilgan malumotlar soni {len(oquvchilar)} ga teng",
            "natijalar": oquvchilar
        }
        return Response(oquvchilar)

    def post(self, request):
        oquvchilar = OquvchilarSerializer(data=request.data)
        if oquvchilar.is_valid():
            oquvchilar.save()
            return Response(oquvchilar.data, status=status.HTTP_201_CREATED)
        return Response(oquvchilar.errors, status=status.HTTP_400_BAD_REQUEST)


class OquvchilarDetailAPIView(APIView):
    #bironta id dagi malumotni charish uchun
    def get_object(self, pk):
        try:
            return Oquvchilar.objects.get(pk=pk)
        except Oquvchilar.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        oquvchilar = self.get_object(pk)
        serializer = OquvchilarSerializer(oquvchilar).data
        data = {
            'natija': serializer
        }
        return Response(data)

    # bironta id dagi malumotni o'zgartirish uchun
    def put(self, request, pk):
        oquvchilar = self.get_object(pk)
        serializer = OquvchilarSerializer(oquvchilar, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': f"{oquvchilar.name} o'zgartirildi",
                'natija': serializer.data
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # bironta id dagi malumotni o'chirish uchun
    def delete(self, request, pk):
        oquvchilar = self.get_object(pk)

        data = {
            'xabar': f"{oquvchilar.name}ning malumotlari o'chirildi!"
        }
        oquvchilar.delete()
        return Response(data)


class OylikRoyxatAPI(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        oylik = Oylik.objects.all()
        oylik = OylikSerializer(oylik, many=True).data
        oylik = {
            "status": f"Qaytarilgan malumotlar soni {len(oylik)} ga teng",
            "natijalar": oylik
        }
        return Response(oylik)

    def post(self, request):
        oylik = OylikSerializer(data=request.data)
        if oylik.is_valid():
            oylik.save()
            return Response(oylik.data, status=status.HTTP_201_CREATED)
        return Response(oylik.errors, status=status.HTTP_400_BAD_REQUEST)


class TolovlarRoyxatAPI(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        tolovlar = Tolovlar.objects.all()
        tolovlar = TolovlarSerializer(tolovlar, many=True).data
        tolovlar = {
            "status": f"Qaytarilgan malumotlar soni {len(tolovlar)} ga teng",
            "natijalar": tolovlar
        }
        return Response(tolovlar)

    def post(self, request):
        tolovlar = TolovlarSerializer(data=request.data)
        if tolovlar.is_valid():
            tolovlar.save()
            return Response(tolovlar.data, status=status.HTTP_201_CREATED)
        return Response(tolovlar.errors, status=status.HTTP_400_BAD_REQUEST)


class DavomatRoyxatAPI(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        davomat = Davomat.objects.all()
        davomat = DavomatSerializer(davomat, many=True).data
        davomat = {
            "status": f"Qaytarilgan malumotlar soni {len(davomat)} ga teng",
            "natijalar": davomat
        }
        return Response(davomat)

    def post(self, request):
        davomat = DavomatSerializer(data=request.data)
        if davomat.is_valid():
            davomat.save()
            return Response(davomat.data, status=status.HTTP_201_CREATED)
        return Response(davomat.errors, status=status.HTTP_400_BAD_REQUEST)


class DavomatDetailAPIView(APIView):
    #bironta id dagi malumotni charish uchun
    def get_object(self, pk):
        try:
            return Davomat.objects.get(pk=pk)
        except Davomat.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        davomat = self.get_object(pk)
        serializer = DavomatSerializer(davomat).data
        data = {
            'natija': serializer
        }
        return Response(data)

    # bironta id dagi malumotni o'zgartirish uchun
    def put(self, request, pk):
        davomat = self.get_object(pk)
        serializer = DavomatSerializer(davomat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': f"{davomat.name} o'zgartirildi",
                'natija': serializer.data
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # bironta id dagi malumotni o'chirish uchun
    def delete(self, request, pk):
        davomat = self.get_object(pk)

        data = {
            'xabar': f"{davomat.name}ning malumotlari o'chirildi!"
        }
        davomat.delete()
        return Response(data)


class XonalarRoyxatAPI(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        xonalar = Xonalar.objects.all()
        xonalar = XonalarSerializer(xonalar, many=True).data
        xonalar = {
            "status": f"Qaytarilgan malumotlar soni {len(xonalar)} ga teng",
            "natijalar": xonalar
        }
        return Response(xonalar)

    def post(self, request):
        xonalar = XonalarSerializer(data=request.data)
        if xonalar.is_valid():
            xonalar.save()
            return Response(xonalar.data, status=status.HTTP_201_CREATED)
        return Response(xonalar.errors, status=status.HTTP_400_BAD_REQUEST)


class QabulxonaRoyxatAPI(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        qabulxona = Qabulxona.objects.all()
        qabulxona = QabulxonaSerializer(qabulxona, many=True).data
        qabulxona = {
            "status": f"Qaytarilgan malumotlar soni {len(qabulxona)} ga teng",
            "natijalar": qabulxona
        }
        return Response(qabulxona)

    def post(self, request):
        qabulxona = QabulxonaSerializer(data=request.data)
        if qabulxona.is_valid():
            qabulxona.save()
            return Response(qabulxona.data, status=status.HTTP_201_CREATED)
        return Response(qabulxona.errors, status=status.HTTP_400_BAD_REQUEST)


class QabulxonaDetailAPIView(APIView):
    #bironta id dagi malumotni charish uchun
    def get_object(self, pk):
        try:
            return Qabulxona.objects.get(pk=pk)
        except Qabulxona.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        qabulxona = self.get_object(pk)
        serializer = QabulxonaSerializer(qabulxona).data
        data = {
            'natija': serializer
        }
        return Response(data)

    # bironta id dagi malumotni o'zgartirish uchun
    def put(self, request, pk):
        qabulxona = self.get_object(pk)
        serializer = QabulxonaSerializer(qabulxona, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': f"{qabulxona.name} o'zgartirildi",
                'natija': serializer.data
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # bironta id dagi malumotni o'chirish uchun
    def delete(self, request, pk):
        qabulxona = self.get_object(pk)

        data = {
            'xabar': f"{qabulxona.name}ning malumotlari o'chirildi!"
        }
        qabulxona.delete()
        return Response(data)


class DarslarRoyxatAPI(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        darslar = Darslar.objects.all()
        darslar = DarslarSerializer(darslar, many=True).data
        darslar = {
            "status": f"Qaytarilgan malumotlar soni {len(darslar)} ga teng",
            "natijalar": darslar
        }
        return Response(darslar)

    def post(self, request):
        darslar = DavomatSerializer(data=request.data)
        if darslar.is_valid():
            darslar.save()
            return Response(darslar.data, status=status.HTTP_201_CREATED)
        return Response(darslar.errors, status=status.HTTP_400_BAD_REQUEST)


class DarslarDetailAPIView(APIView):
    #bironta id dagi malumotni charish uchun
    def get_object(self, pk):
        try:
            return Darslar.objects.get(pk=pk)
        except Darslar.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        darslar = self.get_object(pk)
        serializer = DarslarSerializer(darslar).data
        data = {
            'natija': serializer
        }
        return Response(data)

    # bironta id dagi malumotni o'zgartirish uchun
    def put(self, request, pk):
        darslar = self.get_object(pk)
        serializer = DarslarSerializer(darslar, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': f"{darslar.name} o'zgartirildi",
                'natija': serializer.data
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # bironta id dagi malumotni o'chirish uchun
    def delete(self, request, pk):
        darslar = self.get_object(pk)

        data = {
            'xabar': f"{darslar.name}ning malumotlari o'chirildi!"
        }
        darslar.delete()
        return Response(data)


class AccountRoyxatAPIView(APIView):
    def get(self, request):
        account = Account.objects.all()
        print("account -> ", account)
        account = AccountSerializer(account, many=True).data
        malumotlar = {
            "status": f"Qaytarilgan malumotlar soni {len(account)} ga teng",
            "natijalar": account
        }
        return Response(malumotlar)

    def post(self, request):
        account = AccountSerializer(data=request.data)
        if account.is_valid():
            account.save()
            return Response(account.data, status=status.HTTP_201_CREATED)
        return Response(account.errors, status=status.HTTP_400_BAD_REQUEST)















































