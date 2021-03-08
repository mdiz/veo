from dataclasses import dataclass

"""Class objects for points
"""



@dataclass
class xSite:
	physical_address: str
	building_number: str
	building_address: str
	sq_feet: int


@dataclass
class xDGU:
	name: str
	description: str
	modbus_type: str



@dataclass
class xIO:
	name: str
	description: str
	value: float
	type: str
	register: int


@dataclass
class xCPU:
	cpu_name: str
	cpu_id: int
	pole_rate: int
	ip_stuff: str
	sntp_stuff: str
	cpu_stuff: str
	memory_stuff: str


@dataclass
class xApplication:
	app_name: str
	type: str
	unit: int
	control_pg: str
	io: str
	var: None


@dataclass
class xPoint():
	point_name: str
	description: str
	value: float
	last_value: float
	last_change: float
	units: str
	# app: str = "ACU"
	dgu: int # this would only be connected to IO from the DGU class.  could use is_io attribute to know to look 

	def __str__(self):
		info=self.point_name + " " + self.description 
		return info

	def name_description(self):
		v = self.point_name + " " + self.description
		print(v)


# Var, Input, Output, input type, output type, 




class Point:
	def __init__(self, name, value):
		self.name = name
		self.value = value



class Application:
	def __init__(self, name, var):
		self.name = name
		self.var = var



AI1 = Point("SpaceTemp", 72)
AHU1 = Application("AHU",1)




