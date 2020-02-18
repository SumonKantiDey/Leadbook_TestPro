import json
import os
from django.core.management.base import BaseCommand
from api.models import CompanyInfo, CorporateSecretary, Director
import time
from datetime import date, datetime


def _read_json_file():
    company_info_field = ['Name', 'Security Code', 'Office Address', 'Email Address', 'Phone', 'Fax', 'NPWP',
                          'Site', 'Listing Date', 'Board', 'Main Business Field', 'Sector', 'Sub Sektor',
                          'Registrar']
    company_secretary_filed = 'Corporate Secretary'
    director_field = 'Director'
    with open('api/management/commands/company_profile.json', 'r') as f:
        data = json.load(f)
    companies = len(data)
    for index in range(companies):
        print("index = ", index, data[index]["Security Code"])
        if index == 0:
            continue
        company_name = data[index][company_info_field[0]]
        security_code = data[index][company_info_field[1]]
        office_address = data[index][company_info_field[2]]
        email = data[index][company_info_field[3]]
        phone = data[index][company_info_field[4]]
        fax = data[index][company_info_field[5]]
        npwp = data[index][company_info_field[6]]
        site = data[index][company_info_field[7]]
        try:
            listing_date = datetime.strptime(
                data[index][company_info_field[8]], '%d %b %Y').date()
        except:
            listing_date = None
        board = data[index][company_info_field[9]]
        business_field = data[index][company_info_field[10]]
        sector = data[index][company_info_field[11]]
        sub_sector = data[index][company_info_field[12]]
        registrar = data[index][company_info_field[13]]
        if len(company_name) > 0 and len(security_code) > 0:
            company_info = CompanyInfo.objects.get_or_create(
                company_name=company_name,
                security_code=security_code,
                office_address=office_address,
                email=email,
                country="Indonesia",
                phone=phone,
                fax=fax,
                npwp=npwp,
                site=site,
                listing_date=listing_date,
                board=board,
                business_field=business_field,
                sector=sector,
                sub_sector=sub_sector,
                registrar=registrar
            )[0]
            company_info.save()
        directors = data[index]['Director']
        for val in range(len(directors)):
            name = directors[val]['name']
            position = directors[val]['Position']
            director = Director.objects.get_or_create(
                company=company_info,
                name=name,
                position=position
            )[0]
            director.save()
        secretaries = data[index]['Corporate Secretary']
        #print(secretaries)
        for val in range(len(secretaries)):
            name = secretaries[val]['name']
            email = secretaries[val]['email']
            phone = secretaries[val]['phone']
            #print(name, email, phone)
            secretary = CorporateSecretary.objects.get_or_create(
                company=company_info,
                name=name,
                email=email,
                phone=phone
            )[0]
            secretary.save()


class Command(BaseCommand):
    def handle(self, *args, **options):
        _read_json_file()
        print("Completed")
