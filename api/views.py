from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

@api_view(["GET"])
def get_info(request):
    info = Info.objects.last()
    info_ser = InfoSerializer(info)
    data = {
        "data": info_ser.data
    }
    return Response(data)

@api_view(["GET"])
def get_social_media(request):
    social_medias = SocialMedia.objects.all()
    social_medias_ser = SocialMediaSerializer(social_medias, many=True)
    data = {
        "data": social_medias_ser.data
    }
    return Response(data)

@api_view(["POST"])
def create_order(request):
    name = request.POST.get("name")
    phone = request.POST.get("phone")
    if name and phone is not None:
        Order.objects.create(name=name, phone=phone)
        data = {
            "success": True
        }
    else:
        data = {
            "error": "Name and number can't be None"
        }
    return Response(data)

@api_view(["GET"])
def get_discount(request):
    discount = Discount.objects.last()
    discount_ser = DiscountSerializer(discount)
    data = {
        "data": discount_ser.data
    }
    return Response(data)

@api_view(["GET"])
def get_product(request):
    product = Product.objects.last()
    product_ser = ProductSerializer(product)
    data = {
        "data": product_ser.data
    }
    return Response(data)

@api_view(["GET"])
def get_about_product(request):
    about_product = AboutProduct.objects.all()
    about_product_ser = AboutProductSerializer(about_product, many=True)
    data = {
        "data": about_product_ser.data
    }
    return Response(data)

@api_view(["GET"])
def get_about(request):
    about = About.objects.last()
    about_ser = AboutSerializer(about)
    data = {
        "data": about_ser.data
    }
    return Response(data)

@api_view(["GET"])
def get_who_use(request):
    who_use = WhoUse.objects.last()
    who_use_ser = WhoUseSerializer(who_use)
    data = {
        "data": who_use_ser.data
    }
    return Response(data)

@api_view(["GET"])
def get_how_to_use(request):
    how_to_use = HowToUse.objects.last()
    how_to_use_ser = HowToUseSerializer(how_to_use)
    data = {
        "data": how_to_use_ser.data
    }
    return Response(data)

@api_view(["GET"])
def get_fact(request):
    facts = Fact.objects.all()
    facts_ser = FactSerializer(facts, many=True)
    data = {
        "data": facts_ser.data
    }
    return Response(data)