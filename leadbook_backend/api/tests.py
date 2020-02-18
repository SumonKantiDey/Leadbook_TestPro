from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import CompanyInfo, CorporateSecretary, Director


class CompanyListTestcase(APITestCase):

    def setUp(self):
        company_info = CompanyInfo.objects.create(
            company_name="Astra Agro Lestari Tbk",
            security_code="AALI",
            office_address="Jl Pulo Ayang Raya Blok OR No. 1 Kawasan Industri Pulogadung Jakarta",
            email="Investor@astra-agro.co.id",
            country="Indonesia",
            phone="461-65-55",
            fax="461-6655, 461-6677, 461-6688",
            npwp="01.334.427.0-054.000",
            site="http://www.astra-agro.co.id",
            listing_date="2018-12-12",
            board="UTAMA",
            business_field="Agriculture Plantation",
            sector="AGRICULTURE",
            sub_sector="PLANTATION",
            registrar="PT. Raya Saham Registrar (dulu bernama PT. Risjad Salim Registra")
        director = Director.objects.create(
            company=company_info,
            name="New User",
            position="Position"
        )
        secretary = CorporateSecretary.objects.create(
            company=company_info,
            name="new secretary",
            email="secretary@gmail.com",
            phone="13256487"
        )
        self.list_url = reverse('company_list')

    def test_company_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_company_detail(self):
        response = self.client.get(
            self.list_url, {'company_name': 'Astra Agro'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_company_detail_notfound(self):
        response = self.client.get(
            self.list_url, {'company_name': 'Mista agra'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
