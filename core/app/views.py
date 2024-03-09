from django.contrib.auth import login
from rest_framework import status
from .models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView, Response
from .models import Recipes, ProductList, Category, TypeMeal
from .serializers import RecipesListSerializer, RecipesDetailSerializer, \
    RecipesPostSerializer, RecipeUpdateSerializer, ProductsListSerializer, \
    TypeMealSerializer, UserListSerializer, UserCreateSerializer, UserLoginSerializer


# Create your views here.
class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserCreateView(APIView):
    def post(self, request):
        new_user = UserCreateSerializer(data=request.data, context={'request': request})

        if new_user.is_valid(raise_exception=True):
            new_user.save()
            return Response(new_user.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data, context={'request': request})

        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            login(request, user)
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.session.flush()
        return Response(data='goodbye', status=status.HTTP_200_OK)

class RecipesListView(APIView):
    def get(self, request):
        recipes = Recipes.objects.all()
        serializer = RecipesListSerializer(recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RecipesDetailView(APIView):
    def get(self, request, id):
        recipe = Recipes.objects.filter(pk=id).first()
        serializer = RecipesDetailSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RecipesPostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        new_recipe = RecipesPostSerializer(data=request.data, context={'request':request})
        if new_recipe.is_valid(raise_exception=True):
            new_recipe.save()
            return Response(new_recipe.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        recipe = get_object_or_404(Recipes.objects.all(), pk=id)
        recipe.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class RecipesUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, id):
        recipe = get_object_or_404(Recipes.objects.all(), pk=id)
        serializer = RecipeUpdateSerializer(recipe, data=request.data, context={'request': request})

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class TypeMealView(APIView):

    def get(self, request):
        meals = TypeMeal.objects.all()
        serializer = TypeMealSerializer(meals)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductListView(APIView):
    def get(self, request):
        products = ProductList.objects.all()
        serializer = ProductsListSerializer(products)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializers = UserSerializer(users, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


