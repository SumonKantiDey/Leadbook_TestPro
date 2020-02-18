from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CompanyInfo, CorporateSecretary, Director
from functools import reduce
# Create your views here.


def index(request):
    return HttpResponse("Leadbook code test")


class CompanyList(APIView):
    def get(self, request, *args, **kwargs):
        query_param = request.query_params.get('company_name')
        if query_param:
            query_param = query_param.split(' ')
            # queryset = CompanyInfo.objects.filter(name=query_param))
            queryset = CompanyInfo.objects.filter(reduce(
                lambda x, y: x & y, [Q(company_name__contains=word) for word in query_param]))
        else:
            queryset = CompanyInfo.objects.all()
        company_list = []
        if len(queryset) >= 1:
            for company in queryset:
                company_info = CompanyInfo.objects.filter(
                    pk=company.id).values()[0]
                secretaries = company.secretaries.all()
                secretary_list = []
                for secretary in secretaries:
                    secretary_info = CorporateSecretary.objects.filter(
                        id=secretary.id).values('name', 'email', 'phone')[0]
                    secretary_list.append(secretary_info)
                company_info.update({"Corporate Secretary": secretary_list})

                directors = company.dicrectors.all()
                director_list = []
                for director in directors:
                    director_info = Director.objects.filter(
                        id=director.id).values('name', 'position')[0]
                    director_list.append(director_info)

                company_info.update({"Director": director_list})
                company_list.append(company_info)
            return Response({"Data": company_list}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'Data Not Found'}, status=status.HTTP_404_NOT_FOUND)
