from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .models import Product
from .serializers import *

# Create your views here.
class ProductView(APIView):

    def get(self,request):
        all_product = Product.objects.all()
        serializers_porduct = Product_Serializers2(all_product,many=True).data
        print(serializers_porduct)
        return Response(serializers_porduct)
    

    # def get(self,request):
    #     all_product = Product.objects.all()

    #     product_data=[]

    #     for product in all_product:
    #         single_product ={
    #             'id' : product.id,
    #             'product_name':product.product_name,
    #             'code' : product.code,
    #             'price' : product.price
    #         }

    #         product_data.append(single_product)

    #         print(single_product)


    #     return Response(product_data)

    def post(self,request):
        new_product = Product(product_name =request.data["product_name"],code = request.data["code"],price = request.data["price"],category_reference_id = request.data['category'])
        new_product.save() 

        return Response('Data saved!')

class ProductViewById(APIView):
    def get(self,request,id):
        product = Product.objects.get(id = id)

        single_product ={
                'id' : product.id,
                'product_name':product.product_name,
                'code' : product.code,
                'price' : product.price
            }

        return Response(single_product)

    def patch(self,request,id):
        product = Product.objects.filter(id = id)
        product.update(product_name =request.data["product_name"],code = request.data["code"],price = request.data["price"]) 

        return Response('UPDATED!')
    
    def delete(self,request,id):
        product = Product.objects.get(id = id)
        product.delete()

        return Response("DELETED!")


