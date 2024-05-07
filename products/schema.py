import graphene
from graphene_django import DjangoObjectType
from .models import Category, Product, Unit, Vat

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("cat_title", "cat_description", "active")

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = (
            "pro_title",
            "pro_description",
            "category",
            "price",
            "vat",
            "code_plu",
            "ean_code",
            "qanty",
            "image",
            "active",
        )

class UnitType(DjangoObjectType):
    class Meta:
        model = Unit
        fields = ("unit_title", "char")

class VatType(DjangoObjectType):
    class Meta:
        model = Vat
        fields = ("vat_title", "value")

class Query(graphene.ObjectType):
    all_categories = graphene.List(CategoryType)
    all_products = graphene.List(ProductType)
    all_units = graphene.List(UnitType)
    all_vats = graphene.List(VatType)

    def resolve_all_categories(self, info):
        return Category.objects.all()

    def resolve_all_products(self, info):
        return Product.objects.all()

    def resolve_all_units(self, info):
        return Unit.objects.all()

    def resolve_all_vats(self, info):
        return Vat.objects.all()

schema = graphene.Schema(query=Query)