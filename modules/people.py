import json

people = json.loads(open('resources/people.json').read())

def get_person(index):
	person = next((p for p in people if p["index"] == index), None)
	return person
	
def get_person_by_name(name):
	person = next((p for p in people if p["name"].upper() == name.upper()), None)
	return person
	
def get_friends(person):
	friends = [friend["index"] for friend in person["friends"]]
	return friends

def get_common_friends(index1, index2):
	friends_person1 = [];
	friends_person2 = [];
	person1 = get_person(index1)
	if person1 is not None:
		friends_person1 = get_friends(person1)
	person2 = get_person(index2)
	if person2 is not None:
		friends_person2 = get_friends(person2)
	common_friends_index = set(friends_person1) & set(friends_person2)
	common_friends = [get_person(common_friend) for common_friend in common_friends_index]
	return common_friends

def get_people_from_company(index):
	employees = [person for person in people if person["company_id"] == index]
	return employees
