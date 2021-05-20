from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpRequest
from django.shortcuts import render, render_to_response
from . import models
import json
# import JsonResponse
# Create your views here.
is_auth=False
def open(request):
	global is_auth
	print is_auth
	if 'username' in request.GET:
		username = request.GET['username']
		password = request.GET['password']
		print "=====worinkngknnsad"
		login = [username,password]
		is_auth = check_authentication(login)
		return HttpResponse(json.dumps(is_auth))
	if is_auth:
		if 'ship_name' in request.GET:
			ship_name = request.GET['ship_name']
			last_service = request.GET['last_service']
			ship_obj = models.ship_record()
			ship_obj.name = ship_name
			ship_obj.last_service = last_service
			ship_obj.save()

		if 'ship_id' in request.GET and 'voyage_no' in request.GET:
			ship_id = request.GET['ship_id']
			voyage_no = request.GET['voyage_no']
			make_new_voyage(ship_id,voyage_no)
		ship_obj = models.ship_record.objects.all()
		context = dict()
		context['ship_obj'] = ship_obj
		# noon_obj = models.noon_report.objects.filter(voyage=7)
		# print "noon",noon_obj
		# context['noon_obj'] = noon_obj
		# for key in noon_obj:
		# 	print key.voyage.voyage_no,key.speed,key.cons,key.date,key.id
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
		if 'ship_id_noon' in request.GET:
			ship_id = request.GET['ship_id_noon']
			voyage = models.ship_voyage.objects.filter(ship=ship_id).all()
			voyage_dict = {}
			for key in voyage:
				voyage_dict[key.id] = key.voyage_no
			print voyage_dict,"===dict"
			return HttpResponse(json.dumps(voyage_dict))
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

		if 'voyage_id_vd' in request.GET:
			voyage_id = request.GET['voyage_id_vd']
			noon_obj = models.noon_report.objects.filter(voyage=voyage_id)
			noon_dict = {}
			for noons in noon_obj:
				print noons.id
				noon_dict[noons.id] = noons.date
			return HttpResponse(json.dumps(noon_dict))
		comp_dict = compare()
		context['comp_dict'] = comp_dict
		return render_to_response('hospital_recors/home.html',context)
	# return HttpResponse('no')
def make_new_voyage(ship_id,voyage_no):
	voyage = models.ship_voyage()
	voyage.ship = models.ship_record.objects.filter(id=ship_id)[0]
	voyage.voyage_no = voyage_no
	voyage.save()
	return 0
# def save_noon_data(request):


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

# authentication = False
def index(request):
	return render_to_response('hospital_recors/login_page.html')

def check_authentication(request):
	login_cridetials={
	'Anshuman':'Password',
	}
	if request[0] in login_cridetials and login_cridetials[request[0]] == request[1]:
		return True
	else:
		return False