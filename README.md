# Leadbook_TestPro
## Task 1 
### Prerequisites
```
python==3.6
Selenium
```

### part 1 

In that portion I have crawled 675 compnay tickeled symbol from [https://www.idx.co.id/en-us/listed-companies/company-profiles/](https://www.idx.co.id/en-us/listed-companies/company-profiles/). 

* [company_index.py](https://github.com/SumonKantiDey/Leadbook_TestPro/blob/master/crawled_data/company_index.py)
* [company_index.json](https://github.com/SumonKantiDey/Leadbook_TestPro/blob/master/crawled_data/company_index.json)

### part 2
In that part i have fetched 675 detailed company profile based on the links i have crawled in part 1.
* [company_profile.py](https://github.com/SumonKantiDey/Leadbook_TestPro/blob/master/crawled_data/company_profile.py)
* [company_subsidiary.py](https://github.com/SumonKantiDey/Leadbook_TestPro/blob/master/crawled_data/company_subsidiary.py)
* [company_profile.json](https://github.com/SumonKantiDey/Leadbook_TestPro/blob/master/crawled_data/company_profile.json)


## Task 2 
### Prerequisites
```
python==3.6
Django==3.0.3
djangorestframework==3.11.0
djangorestframework-simplejwt==4.4.0
postgresql
```
- [leadbook_backend](https://github.com/SumonKantiDey/Leadbook_TestPro/tree/master/leadbook_backend)

For developing backend API I have used Django python web Framework. Some reason i have choosed Django.
```
- It offers a full-featured Model-View-Controller framework
- Provide robust ORM (object-relational mapper) that helps to interact with databases
- It has excellent directory structure, dynamic CRUD (create, read, update and delete) interface and functional admin panel
- Huge third party application support
- Unit testing and Serialization opportunity 
```
For Database i have used postgresql.
```
Table joins and views for flexible data retrieval
PostgreSQL is complete ACID compliant.
PostgreSQL performance well when executing complex queries.
```

### Database architecture
<p align="center">
<img src="https://user-images.githubusercontent.com/16388826/74765962-abe63780-52ae-11ea-9d06-0a18177d58ea.png">
</p>

### API endpoints
```
GET/ http://127.0.0.1:8000/api/v1/companies
GET/ http://127.0.0.1:8000/api/v1/companies?company_name=Agro Lestari
```
First API can fetch a list of all companies. For the second API, I have used encapsulates Django Q object filter  which can find
all company info if query parameters word exists in the company name.
### Instructions
```
- activate virtualenv
- virtualenv install -r requirements.txt
username : admin
password : 123456
```
### Notes
Some company is enlisted in the company index but in company details page I did not get any information. That's why I did not put that type of company info in the database.So I have got 675 company info through my crawler that I mentioned in task one but only 658 company has their details.

## Job Title Classification
Machine learning
