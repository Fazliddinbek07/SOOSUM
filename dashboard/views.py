from django.shortcuts import render, redirect
from .models import *

def index(request):
    orders = Order.objects.all()
    context = {
        "orders_quantity": orders.count()
    }
    return render(request, "index.html", context)

def info_get(request):
    if Info.objects.all().count() > 0:
        info = [Info.objects.last()]
    else:
        info = []
    context = {
        "info": info
    }
    return render(request, "info-get.html", context)


def info_add(request):
    if request.method == "POST":
        text_uz = request.POST.get("text_uz")
        text_ru = request.POST.get("text_ru")
        logo = request.FILES.get("logo")
        if text_uz and text_ru and logo is not None:
            Info.objects.create(text_uz=text_uz, text_ru=text_ru, logo=logo)
            return redirect("info_get")
        else:
            return redirect("info_add")
    else:
        return render(request, "info-add.html")


def info_edit(request):
    if Info.objects.all().count() > 0:
        if request.method == "POST":
            info = Info.objects.last()
            text_uz = request.POST.get("text_uz")
            text_ru = request.POST.get("text_ru")
            logo = request.FILES.get("logo")
            if text_uz and text_ru and logo is not None:
                info.text_uz = text_uz
                info.text_ru = text_ru
                info.logo = logo
                info.save()
                return redirect("info_get")
            else:
                return redirect("info_edit")
        else:
            return render(request, "info-edit.html")
    else:
        return redirect("info_get")


def info_delete(request):
    if Info.objects.all().count() > 0:
        Info.objects.last().delete()
    return redirect("info_get")


def social_media_get(request):
    social_medias = SocialMedia.objects.all()
    context = {
        "social_medias": social_medias
    }
    return render(request, "social-media-get.html", context)


def social_media_add(request):
    if request.method == "POST":
        link = request.POST.get("link")
        img = request.FILES["img"]
        if link and img is not None:
            SocialMedia.objects.create(link=link, img=img)
        return redirect("social_media_add")
    else:
        return render(request, "social-media-add.html")


def social_media_edit(request, pk):
    if SocialMedia.objects.filter(id=pk).count() > 0:
        if request.method == "POST":
            social_media = SocialMedia.objects.last()
            link = request.POST.get("link")
            img = request.FILES.get("img")
            if link and img is not None:
                social_media.link = link
                social_media.img = img
                social_media.save()
                return redirect("social_media_get")
            else:
                return redirect("social_media_edit", pk=pk)
        else:
            return render(request, "social-media-edit.html")
    else:
        return redirect("social_media_get")

def social_media_delete(request, pk):
    if SocialMedia.objects.filter(id=pk).count() > 0:
        SocialMedia.objects.get(id=pk).delete()
    return redirect("social_media_get")


def order_get(request):
    orders = Order.objects.all()
    context = {
        "orders": orders
    }
    return render(request, "order-get.html", context)


def order_delete(request, pk):
    if Order.objects.filter(id=pk).count() > 0:
        Order.objects.get(id=pk).delete()
    return redirect("order_get")


def discount_get(request):
    if Discount.objects.all().count() > 0:
        discount = [Discount.objects.last()]
    else:
        discount = []
    context = {
        "discount": discount
    }
    return render(request, "discount-get.html", context)


def discount_add(request):
    if request.method == "POST":
        img = request.FILES.get("text_uz")
        if img is not None:
            Discount.objects.create(img=img)
            return redirect("discount_get")
        else:
            return redirect("discount_add")
    else:
        return render(request, "discount-add.html")


def discount_edit(request):
    if Discount.objects.all().count() > 0:
        if request.method == "POST":
            discount = Discount.objects.last()
            img = request.FILES.get("img")
            if img is not None:
                discount.img = img
                discount.save()
                return redirect("discount_get")
            else:
                return redirect("discount_edit")
        else:
            return render(request, "discount-edit.html")
    else:
        return redirect("discount_get")

def discount_delete(request):
    if Discount.objects.all().count() > 0:
        Discount.objects.last().delete()
    return redirect("info_get")