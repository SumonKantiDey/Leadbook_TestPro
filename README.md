# Leadbook_TestPro
## Task 1 

### Prerequisites
```
python==3.6
Selenium
```

### part 1 

In that portion I have crawled **675** compnay tickeled symbol from [https://www.idx.co.id/en-us/listed-companies/company-profiles/](https://www.idx.co.id/en-us/listed-companies/company-profiles/). In that company basic information i have fetched these field.
<center>
<table>
    <tbody>
        <tr>
            <th align="center">ticker symbol</th>
            <th align="right">company name</th>
        </tr>
        <tr>
            <th align="center">url</th>
            <th align="right">listing_date</th>
        </tr>
        <tr>
            <th align="center">crawled_at</th>
            <th align="right"></th>
        </tr>
    </tbody>
    </table>
   </center>

* [company_index.py](https://github.com/SumonKantiDey/Leadbook_TestPro/blob/master/crawled_data/company_index.py)
* [company_index.json](https://github.com/SumonKantiDey/Leadbook_TestPro/blob/master/crawled_data/company_index.json)

### part 2
In that part i have fetched 675 detailed company profile based on the links i have crawled in part 1. In that detailed company profile included these field.
<center>
<table>
    <tbody>
        <tr>
            <th align="left">Name</th>
            <th align="center">Security Code</th>
            <th align="right">Office Address</th>
        </tr>
        <tr>
            <td align="left">Email Address</td>
            <td align="center">Phone</td>
            <td align="right">Fax</td>
        </tr>
        <tr>
            <td align="left">NPWP</td>
            <td align="center">Site</td>
            <td align="right">Listing Date</td>
        </tr>
        <tr>
            <td align="left">Board</td>
            <td align="center">Main Business Field</td>
            <td align="right">Sector</td>
        </tr>
        <tr>
            <td align="left">Sub Sektor</td>
            <td align="center">Registrar</td>
            <td align="right">Corporate Secretary</td>
        </tr>
        <tr>
            <td align="left">Director</td>
            <td align="center">Subsidiary</td>
            <td align="right"></td>
        </tr>
    </tbody>
</table>
</center>

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
For Database i have used postgresql which is object relational database.
```
- 
- Offers table joins and views for flexible data retrieval.
- Postgres handles concurrency better rather than other database.
- PostgreSQL performance well when executing complex queries.
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
### Unit testing scenarios
* Verify all companies information through GET request.
* Test to verify all company information by company name as a query parameter.
- Usage : **python manage.py test**
### Test this repository
```
- activate virtualenv
- virtualenv install -r requirements.txt
username : admin
password : 123456
```
### Notes
Some company is enlisted in the company index but in company details page I did not get any information. That's why I did not put that type of company info in the database.So I have got 675 company info through my crawler that I mentioned in task one but only 658 company has their details.

## Job Title Classification
In that task i have got **1.7k** data points where **1.4k** as a valid job titles and **300** as a invalid job titles also it is a imbalanced dataset. Firstly i have tried two machine learning model. I did not use extensive preprocessing because less data.
- First model i have tried [logistic regression](https://github.com/SumonKantiDey/Leadbook_TestPro/blob/master/Leadbook_Data_Challenge/model/Logistic%20Regression.ipynb)
 with ensable of char and word frequescy . **f_score:: 0.96**

- In second model i have tried [char n grams with cnn and lstm]
(https://github.com/SumonKantiDey/Leadbook_TestPro/blob/master/Leadbook_Data_Challenge/model/lstm%20%2B%20cnn%20%2B%20char_n_grams%20.ipynb). **f_score:: 0.98**
 
