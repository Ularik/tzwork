from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import Recipes, ProductList, Category, TypeMeal
from django.contrib.auth.models import User

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        for filed, value in validated_data.items():
            if filed == 'password':
                instance.set_password(value)
            else:
                setattr(instance, filed, value)
        instance.save()
        return instance

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=True,
        write_only=True
    )
    def validate(self, attrs):
        # Take username and password from request
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs['user'] = user
        return attrs

class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductList
        fields = '__all__'

class RecipesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = ('id', 'title', 'time_cook', 'type_meal')

class RecipesDetailSerializer(serializers.ModelSerializer):
    user = UserListSerializer()
    products = ProductsListSerializer(many=True)
    category_name = serializers.CharField(source='category.name')
    dish_type = serializers.CharField(source='type_meal.name')
    class Meta:
        model = Recipes
        # fields = ('id', 'user', 'title', 'descriptions', 'time_cook', 'products', 'type_meal',
        #          'category', 'created_add', 'updated_add')
        exclude = ('category', 'type_meal')


class RecipesPostSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Recipes
        fields = '__all__'

class TypeMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeMeal
        fields = '__all__'

class RecipeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = ('descriptions', 'title', 'time_cook', 'products', 'type_meal', 'category')