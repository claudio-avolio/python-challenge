# python-challenge

Known limitations:

===

The format of the Person record returned to the client has the same format of original stored in the file people.json; this means that the APIs return more data than necessary.
In a real world scenario, the format of the output will follow a interface defined by the API specification, usually provinding only the information that is or might eventually be necessary.

===

In a real world scenario of an API Approach solution (using Mulesoft naming convention) we would have two layers of APIs:

1 - System APIs responsible for retrieving Person and Company resources in a (close to) pure RESTful way, for example:

GET http://<host>:<port>/paranuara/v1.0/company (retrieve all companies)  
GET http://<host>:<port>/paranuara/v1.0/company/<index> (retrieve the company UNIQUELY identifed by the id <index>)  
GET http://<host>:<port>/paranuara/v1.0/company/<index>/employees (retrieve all the employes that work for the company UNIQUELY identifed by the id <index>)  
GET http://<host>:<port>/paranuara/v1.0/person (retrieve all persons from repository)  
GET http://<host>:<port>/paranuara/v1.0/person/<index> (retrieve the person UNIQUELY identifed by the id <index>)  
GET http://<host>:<port>/paranuara/v1.0/person/<index>/friends (retrieve all friends of the person UNIQUELY identifed by the id <index>)  

The APIs that return a collection can also accept query strings to return a subset of entities.

2 - Process APIs responsible for fulfilling business requirements - they orchestrate System APIs calls and provide services to the upper layer...

3 - Experience APIs, responsible to be the direct endpoint for applications that will consume the services.

GET http://<host>:<port>/paranuara/v1.0/company-employees?name=CompanyName  
GET http://<host>:<port>/paranuara/v1.0/people-info?person1Name=Name1&person2Name=Name2  
GET http://<host>:<port>/paranuara/v1.0/person-info?name=Name  

For this challenge, in order to keep things simple, there is no separation for APIS layers. All APIs retrieve sata stright from the repository and enforce any rules specified in the requirements.

** THE SOLUTION **

This solution implements 3 APIS:

1) http://<host>:<port>/paranuara/v1.0/company-employees?name=CompanyName

Returns a JSON list with all employees from the company specified by the parameter 'name'
If the parameter 'name' is not provided, the API returns HTTP response code 400 (Bad Request)
If the company does not exist in the file companies.json, the API returns the HTTP response code 404 (Not Found)
If the company exists but it doesn't have any employee, the API returns an empty JSON list.

Example:

http://<host>:<port>/paranuara/v1.0/company-employees?name=lovepad

Note: the parameter 'name' is case insensitive

2) http://<host>:<port>/paranuara/v1.0/people-info?person1Name=Name1&person2Name=Name2

Returns a JSON object with the following format:

{ 
	person1 : {  
		name : ...,  
		age : ...,  
		address : ...,  
		phone : ...  
	},  
	person2 : {  
		name : ...,  
		age : ...,  
		address : ...,  
		phone : ...  
	},  
	common_friends : [  
		list of common frieds still alive and with brown eyes  
	]  
}  

If the parameter 'person1Name' or parameter 'person2Name' is not provided, the API returns HTTP response code 400 (Bad Request)
If person1 or person2 does not exist in the file people.json, the API returns the HTTP response code 404 (Not Found)
If person1 and person2 have no friends in common still alive and with brown eyes the list common_friends will be empty.

3) http://<host>:<port>/paranuara/v1.0/person-info?name=Name

Returns some information abour the person indicated by the parameter 'name' and also which fruits and vegetables he/she likes.

Returns a JSON object with the following format:

{ 
	username : ...,  
	age : ...,  
	fruits : [  
		list of favorite fruits  
	],  
	vegetables : [  
		list of favorite vegetables  
	]  
}  

If the parameter 'name' is not provided, the API returns HTTP response code 400 (Bad Request)
If there is no person with name 'Name' in the file people.json, the API returns the HTTP response code 404 (Not Found)

Downloading the code:

1 - Go to an empty directory ($THE_DIR) clone the repository

> git clone https://github.com/claudio-avolio/python-challenge

2 - Go to the root application directory

> cd python-challenge

3 - Install Dependencies

> pip install -r requirements.txt

4 - Run the application

> flask run

THe server must start as in the following:

 >flask run
 * Serving Flask app "python-challenge.py"
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

The API url, based on the host and port above:

http://127.0.0.1:5000/paranuara/v1.0/company-employees?name=CompanyName
http://127.0.0.1:5000/paranuara/v1.0/people-info?person1Name=Name1&person2Name=Name2
http://127.0.0.1:5000/paranuara/v1.0/person-info?name=Name

******* Test executed using Postman *******

http://127.0.0.1:5000/paranuara/v1.0/company-employees?name=lovepad

Result - see file company-lovepad-employees.txt

http://127.0.0.1:5000/paranuara/v1.0/people-info?person1Name=Grace Kelly&person2Name=Bonnie Bass

Result - see file people-info-result.json

http://127.0.0.1:5000/paranuara/v1.0/person-info?name=Bonnie Bass

Result:

{  
	"age": 54,  
	"fruits": [  
		"orange",  
		"banana",  
		"strawberry"  
	],  
	"username": "Bonnie Bass",  
	"vegetables": [  
		"beetroot"  
	]  
}  
