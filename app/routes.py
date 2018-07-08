from app import app
from flask import abort
from flask import request
from flask import make_response
from flask import jsonify
from modules import people
from modules import company
from modules import food

@app.route('/paranuara/v1.0/company-employees', methods=['GET'])
def get_employees():
	company_name = request.args.get('name')
	if company_name is None or len(company_name) == 0:
		abort(400)
	comp = company.get_by_name(company_name)
	if comp is None:
		abort(404)
	employees = people.get_people_from_company(comp["index"])
	return jsonify(employees)

@app.route('/paranuara/v1.0/people-info', methods=['GET'])
def get_people_info():
	person1_name = request.args.get('person1Name')
	person2_name = request.args.get('person2Name')
	if person1_name is None or person2_name is None or len(person1_name) == 0 or len(person2_name) == 0:
		abort(400)
	person1 = people.get_person_by_name(person1_name)
	if person1 is None:
		abort(404)
	person2 = people.get_person_by_name(person2_name)
	if person2 is None:
		abort(404)
	common_friends = people.get_common_friends(person1["index"], person2["index"])
	filtered_friends = people.get_people_with_filter(lambda p: not p["has_died"] and p["eyeColor"].lower() == "brown", common_friends)
	return jsonify({ "person1" : { "name" : person1["name"], "age" : person1["age"], "address" : person1["address"], "phone" : person1["phone"] }, "person2" : { "name" : person2["name"], "age" : person2["age"], "address" : person2["address"], "phone" : person2["phone"] }, "common_friends" : filtered_friends })

@app.route('/paranuara/v1.0/person-info', methods=['GET'])
def get_person_info():
	name = request.args.get('name')
	if name is None or len(name) == 0:
		abort(400)	
	person = people.get_person_by_name(name)
	if person is None:
		abort(404)
	fruits = []
	vegetables = []
	for favfood in person["favouriteFood"]:
		if food.is_fruit(favfood):
			fruits.append(favfood)
		elif food.is_vegetable(favfood):
			vegetables.append(favfood)			
	return jsonify({"username": person["name"], "age": person["age"], "fruits": fruits, "vegetables": vegetables})

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)
	