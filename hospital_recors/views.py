from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpRequest
from django.shortcuts import render, render_to_response
from . import models
import json

# index function is to show the login page 
def index(request):
	return render_to_response('hospital_recors/login_page.html')

# check_authentication function is to check if user is in login_cridetials dictionry or not this dictiory
# is of current authenticated users it contains their logins and passwords
def check_authentication(request):
	login_cridetials={
	'Anshuman':'Password',
	'ShreyanshChamoli':'Password1'
	}
	if request[0] in login_cridetials and login_cridetials[request[0]] == request[1]:
		return True
	else:
		return False

# open function is the function to focus on all the requests form ajax comes to this function and then this functions
# performs according to the requests give in ajax
def open(request):
	# this is to check user authentication 
	if 'username' in request.GET:
		is_auth=False
		username = request.GET['username']
		password = request.GET['password']
		login = [username,password]
		is_auth = check_authentication(login)
		return HttpResponse(json.dumps(is_auth))
	
	# this is to save ship in database
	if 'ship_name' in request.GET:
		ship_name = request.GET['ship_name']
		last_service = request.GET['last_service']
		ship_obj = models.ship_record()
		ship_obj.name = ship_name
		ship_obj.last_service = last_service
		ship_obj.save()

	# this is to make new voyage for the given ship in database
	if 'ship_id' in request.GET and 'voyage_no' in request.GET:
		ship_id = request.GET['ship_id']
		voyage_no = request.GET['voyage_no']
		make_new_voyage(ship_id,voyage_no)

	# line 50-53 calls all the ships in database and makes dictionary of ships objects
	ship_obj = models.ship_record.objects.all()
	context = dict()
	context['ship_obj'] = ship_obj

	# this  is to get the voyage details of the ship
	if 'noon_id' in request.GET:
		noon_id = request.GET['noon_id']
		noon_obj = models.noon_report.objects.filter(id=noon_id).first()
		speed = noon_obj.speed
		cons  = noon_obj.cons
		good_cons = compare()
		for key in good_cons:
			if float(key) ==  float(noon_obj.speed):
				good_cons = good_cons[key]
		noon_data_dict={
			'speed'    : noon_obj.speed,
			'cons'	   : noon_obj.cons,
			'currents' : noon_obj.currents,
			'winds'	   : noon_obj.winds,
			'good_cons':good_cons,
		}
		return HttpResponse(json.dumps(noon_data_dict))

	#this returns the list of voyages for that ship 
	if 'ship_id_noon' in request.GET:
		ship_id = request.GET['ship_id_noon']
		voyage = models.ship_voyage.objects.filter(ship=ship_id).all()
		voyage_dict = {}
		for key in voyage:
			voyage_dict[key.id] = key.voyage_no
		return HttpResponse(json.dumps(voyage_dict))

	#this is to save noon details of that voyage 
	if 'noon_date' in request.GET:
		voyage_id = request.GET['voyage_id_noon']
		noon_obj = models.noon_report()
		noon_obj.voyage = models.ship_voyage.objects.filter(id=voyage_id)[0]
		noon_obj.date = request.GET['noon_date']
		noon_obj.speed = request.GET['speed']
		noon_obj.cons = request.GET['cons']
		noon_obj.currents = request.GET['currents']
		noon_obj.winds = request.GET['winds']
		noon_obj.save()

	#this returns the noon detials for that voyage 
	if 'voyage_id_vd' in request.GET:
		voyage_id = request.GET['voyage_id_vd']
		noon_obj = models.noon_report.objects.filter(voyage=voyage_id)
		noon_dict = {}
		for noons in noon_obj:
			noon_dict[noons.id] = noons.date
		return HttpResponse(json.dumps(noon_dict))

	# comp dict has the details of good ship consumptions
	comp_dict = compare()
	context['comp_dict'] = comp_dict

	# this returns the context dictionary and the home.html file
	return render_to_response('hospital_recors/home.html',context)

# this function is to save new voyage details in database
def make_new_voyage(ship_id,voyage_no):
	voyage = models.ship_voyage()
	voyage.ship = models.ship_record.objects.filter(id=ship_id)[0]
	voyage.voyage_no = voyage_no
	voyage.save()
	return 0

#compare function has a dictonary cons_dict which contails all the good ship consumptions
def compare():
	cons_dict={
	7.0:'18',
	8.0: '18',
	9.0: '19',
	10.0:'21',
	11.0:'22',
	12.0:'25',
	12.0:'25',
	13.0:'27',
	14.0:'29',
	15.0:'31',
	16.0:'37',
	17.0:'41',
	}
	
	return cons_dict



