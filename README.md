# python-challenge

This solution implements 3 APIS:

1) http://<host>:<port>/paranuara/v1.0/company?name=CompanyName

Returns a JSON list with all employees from the company specified by the parameter 'name'
If the parameter 'name' is not provided, the API returns HTTP response code 400 (Bad Request)
If the company does not exist in the file companies.json, the API returns the HTTP response code 404 (Not Found)
If the company exists but it doesn't have any employee, the API returns an empty JSON list.

Example:

http://<host>:<port>/paranuara/v1.0/company?name=lovepad

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
