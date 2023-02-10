from rest_framework import serializers
from myapp.models import User, Category, Brand, Country, State, City, Product
from allauth.utils import generate_unique_username

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'first_name','last_name', 'email','password', 'phone_no', 'is_mobile_verified', 'business_name',)
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            },
            'email': {
                'required': True,
                'allow_blank': False,
            },
            "username": {
                "read_only": True,
            }
        }

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data.get('email'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            phone_no=validated_data.get('phone_no'),
            is_mobile_verified=validated_data.get('is_mobile_verified'),
            business_name=validated_data.get('business_name'),
            username=generate_unique_username([
                validated_data.get('first_name'),
                validated_data.get('email'),
                'user'
            ])
        )

        user.set_password(validated_data.get('password'))
        user.save()

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'phone_no', 'is_mobile_verified', 'business_name', 'is_active', 'last_login', 'date_joined']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'     


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'           


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'        

