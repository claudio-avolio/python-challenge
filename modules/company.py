import json

companies = json.loads(open('resources/companies.json').read())

def get_by_name(name):
	nameUpper = name.upper()
	company = next((c for c in companies if c["company"].upper() == nameUpper), None)
	return company
	
def get_by_index(index):
	company = next((c for c in companies if c["index"] == index), None)
	return company
