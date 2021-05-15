from django.db import models

# Create your models here.

class ship_record(models.Model):
	name = models.CharField(max_length=300)
	def __str__(self):
		return self.name
	last_service = models.DateTimeField(null=True)
	# voyage1 = models.TextField(null=True)
	# voyage2 = models.TextField(null=True)
	# voyage3 = models.TextField(null=True)
	# voyage4 = models.TextField(null=True)
	# day1 = models.DateTimeField(null=True)
	# day2 = models.DateTimeField(null=True)
	# day3 = models.DateTimeField(null=True)
	# day4 = models.DateTimeField(null=True)
	# day5 = models.DateTimeField(null=True)
	# day6 = models.DateTimeField(null=True)
	# day7 = models.DateTimeField(null=True)
	# day8 = models.DateTimeField(null=True)
	# day9 = models.DateTimeField(null=True)
	# day10 = models.DateTimeField(null=True)
	# day11 = models.DateTimeField(null=True)
	# cons = models.TextField(null=True)
	# speed = models.TextField(null=True)

class ship_voyage(models.Model):
	ship = models.ForeignKey(ship_record,null=True,on_delete=models.PROTECT)
	# ship_name =models.TextField(null=True)
  	def __str__(self):
		return self.id
	voyage_no = models.TextField(null=True)


class noon_report(models.Model):
	voyage = models.ForeignKey(ship_voyage,on_delete=models.PROTECT)
	date = models.TextField(null=True)
	cons = models.TextField(null=True)
	speed = models.TextField(null=True)
	currents = models.TextField(null=True)
	winds = models.TextField(null=True)
	def __str__(self):
		return self.id
	