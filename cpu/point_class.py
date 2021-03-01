from dataclasses import dataclass

"""Class objects for points
"""



@dataclass
class Site:
	physical_address: str
	building_number: str
	building_address: str
	sq_feet: int


@dataclass
class CPU:
	cpu_name: str
	cpu_id: int
	pole_rate: int
	ip_stuff: str
	sntp_stuff: str
	cpu_stuff: str
	memory_stuff: str


@dataclass
class Application:
	app_name: str
	type: str = "ACU"
	unit: int = 1


@dataclass
class Point(Application):
	point_name: str = "PointName"
	description: str = "PointDescription"
	value: float = 0.0
	last_value: float = 0.0
	last_change: float = 0.0
	units: str = "degF"
	# app: str = "ACU"
	dgu: int = 1 # this would only be connected to IO from the DGU class.  could use is_io attribute to know to look 

	def name_description(self):
		v = self.point_name + " " + self.description
		print(v)


# Var, Input, Output, input type, output type, 


ACU1.AV1.value


mytest = Point("return_temp", unit=2, app_name="degC")
mytest2 = Point(33)

mytest.point_name="mike"
print(mytest)
print(mytest2)
mytest.name_description()
