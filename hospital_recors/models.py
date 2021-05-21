
# all the database fiels are here
# ship_record,ship_voyage and noon_report are inter-related
# ship_record contails record of ships
# ship_voyage is connected to ship_record as it contains voyage record of each ship
# While noon_report is connected to ship_voyage because it contains voyage details of each voyage


from django.db import models

# this is ship_record model which contains record of all the ships in data base
# their name and last service dat
class ship_record(models.Model):
	name = models.CharField(max_length=300)
	def __str__(self):
		return self.name
	last_service = models.DateTimeField(null=True)

# this is ship_voyage model which contains the voyage no of each ship in data base
# it has ship_record ForeignKey which marks for all ships in database
class ship_voyage(models.Model):
	ship = models.ForeignKey(ship_record,null=True,on_delete=models.PROTECT)
	# ship_name =models.TextField(null=True)
  	def __str__(self):
		return self.id
	voyage_no = models.TextField(null=True)

# this is noon_reports model which contains voyage detials of each voyage in database
# it has ship_voyage ForiegnKey which marks for each voyage in databse
class noon_report(models.Model):
	voyage = models.ForeignKey(ship_voyage,on_delete=models.PROTECT)
	date = models.TextField(null=True)
	cons = models.TextField(null=True)
	speed = models.TextField(null=True)
	currents = models.TextField(null=True)
	winds = models.TextField(null=True)
	def __str__(self):
		return self.id
	