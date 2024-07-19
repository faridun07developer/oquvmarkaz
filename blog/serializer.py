from rest_framework import serializers
from blog.models import Oqtuvchilar, Oylik, Oquvchilar, Davomat, Tolovlar, Xonalar, Qabulxona, \
    Darslar, Account
from django.core.exceptions import ValidationError


class OqituvchilarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oqtuvchilar
        fields = "__all__"

    def validate(self, data):
        name = data.get('name', None)
        surname = data.get('surname', None)
        phonenumber = data.get('phonenumber', None)
        if not (name.isalpha() and surname.isalpha()):
            raise ValidationError({
                'status': False,
                'messege': "Ism yoki Familiyada raqamlar qatnashihsi mumkin emas!!!"
            })
        if (phonenumber.isnumeric()):
            raise ValidationError({
                'status': False,
                'messege': "Telefon raqamda harflar qatnashihsi mumkin emas!!!"
            })

        return data


class OquvchilarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oquvchilar
        fields = "__all__"

    def validate(self, data):
        name = data.get('name', None)
        surname = data.get('surname', None)
        phonenumber = data.get('phonenumber', None)
        if not (name.isalpha() and surname.isalpha()):
            raise ValidationError({
                'status': False,
                'messege': "Ism yoki Familiyada raqamlar qatnashihsi mumkin emas!!!"
            })
        if not (phonenumber.isnumeric()):
            raise ValidationError({
                'status': False,
                'messege': "Telefon raqamda harflar qatnashihsi mumkin emas!!!"
            })

        return data


class OylikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oylik
        fields = "__all__"

    def validate(self, data):
        oquvchilar_soni = data.get('oquvchilar_soni', None)
        if not (oquvchilar_soni.isnumeric()):
            raise ValidationError({
                'status': False,
                'message': "Faqat raqam kiritilsin"
            })
        return data


class DarslarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Darslar
        fields = "__all__"


class XonalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xonalar
        fields = "__all__"


class DavomatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Davomat
        fields = "__all__"


class QabulxonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qabulxona
        fields = "__all__"


class TolovlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tolovlar
        fields = "__all__"


class AccountSerializer(serializers.ModelSerializer):
    class Mete:
        match = Account
        fields = "__all__"

        def validate(self, data):
            username = data.get('name', None)
            email = data.get('email', None)

            Kattaharf = False
            for x in username:
                code = ord(x)
                if (code >= 65 and code <= 90 or (code == 32)):
                    Kattaharf = True
                if(Kattaharf):
                    raise ValidationError({
                        'status': False,
                        'messege': "katta harf va bosh joy bolishi mumkin emas!!!"
                    })

                if Account.object.filter(username=username, email=email).exists():
                    raise ValidationError({
                        'status': False,
                        'message': "Username va email qaytarilishi mumkin emas!!!"
                    })
                return data
# git init
# git add *
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/faridun07developer/oquvmarkaz.git
# git push -u origin main