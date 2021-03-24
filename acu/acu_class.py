#import sys
#sys.path.append(r'/Users/chris/ModulesAndPackages')
#sys.path.append(r'/home/mikedismore/projects/veo/')
#print(sys.path)

#import acu_dict
#import acu_dict as acu_all_dict
#from acu_dict import acu_dict2
#from acu_dict import acu_dict2 as acu_var_dict, acu_dict1 as acu_io_dict

# can also call from within function so module not available outside that namespace

# Import a package
# package is a group of modules in a folder
# package initialization
# inside the folder of modules add a file called __init__.py
# inside __init__.py add import statents for modules to import when "import folderName" is used


# to import all with __init__.py, add this to file.
#	__all__ = [
#	"module1",
#	"module2",
#	"module3",
#	]
# then use "from folderName import *" in module you want to import to
# while import * is a bad practice, this allows you to control what happens when it's used
# can do same thing for a module to control what "import *" imports
# can add sub packages by adding subfolders
# can use a relative import with .. to evaluate to parent package or sub package.  "from .. import package" to import from parent
# "from ..subPackage import package to import from sub package"

# provides discussion on how files are used to organize global variables across modules    https://www.programiz.com/python-programming/global-keyword 

# ~/.dropbox-dist/dropboxd



#print(acu_dict.__file__) # to find where module is stored
#print(dir()) # print names in namespace
#print(dir(acu_dict)) # print names in module


from acu_dict import acu_var_dict
#from acu_code import acu_fan_def
#import acu_code



stat1_io_dict = {
"iReturnTemp":{"register":1, "format":"Float32", "type":"input", "id":1, "name":"iReturnTemp", "description":"Return Temperature", "value":9999, "units":64, "last_change":1234, "local_log":0},
"iSupplyTemp":{"register":2, "format":"Float32", "type":"input", "id":2, "name":"iSupplyTemp", "description":"Supply Temperature", "value":9999, "units":64, "last_change":1234, "local_log":0},
"iSpaceTemp":{"register":3, "format":"Float32", "type":"input", "id":3, "name":"iSpaceTemp_ScheduleOverride", "description":"Space Temperature", "value":9999, "units":64, "last_change":1234, "local_log":0},
"iUnitAmperage":{"register":4, "format":"Float32", "type":"input", "id":4, "name":"iUnitAmperage", "description":"Unit Amperage", "value":9999, "units":3, "last_change":1234, "local_log":0},
"iLocalTempAdjust":{"register":5, "format":"Float32", "type":"input", "id":5, "name":"iLocalTempAdjust", "description":"Local Space Temperature Adjustment", "value":9999, "units":64, "last_change":1234, "local_log":0},
"iAuxUnitStatus":{"register":6, "format":"Float32", "type":"input", "id":6, "name":"iAuxUnitStatus", "description":"Aux Unit Status", "value":9999, "units":64, "last_change":1234, "local_log":0},
"oFanEnable":{"register":7, "format":"Float32", "type":"output", "id":1, "name":"oFanEnable", "description":"Fan Enable", "value":9999, "units":95, "last_change":1234, "local_log":0},
"oCompressor1Enable":{"register":8, "format":"Float32", "type":"output", "id":2, "name":"oCompressor1Enable", "description":"Compressor 1 Enable", "value":9999, "units":95, "last_change":1234, "local_log":0},
"oCompressor2Enable":{"register":9, "format":"Float32", "type":"output", "id":3, "name":"oCompressor2Enable", "description":"Compressor 2 Enable", "value":9999, "units":95, "last_change":1234, "local_log":0},
"oHeat1Enable":{"register":10, "format":"Float32", "type":"output", "id":4, "name":"oHeat1Enable", "description":"Heat 1 Enable", "value":9999, "units":95, "last_change":1234, "local_log":0},
"oHeat2Enable":{"register":11, "format":"Float32", "type":"output", "id":1, "name":"oHeat2Enable", "description":"Heat 2 Enable", "value":9999, "units":95, "last_change":1234, "local_log":0},
"oEconomizerEnable":{"register":12, "format":"Float32", "type":"output", "id":2, "name":"oEconomizerEnable", "description":"Economizer Enable", "value":9999, "units":95, "last_change":1234, "local_log":0},
}


#"vReturnTempConditionedValue":{"id":1, "name":"vReturnTempConditionedValue", "description":"Return Temperature Conditioned Value", "value":70.863, "units":64, "last_change":1234, "local_log":0},
#dgu1.ref
#gu1.iReturnTemp.value


# NEED A COMMOM PLACE TO INTERACT WITH ALL SITE OBJECTS.  THIS MAY HAPPEN ANYWAY AS IT WILL ALL BE IN THE SAME NAMESPACE

# need dict of each DGU type.  Like a profile
# that dict would be imported to a DGU class to define it and named for the DGU
# code would update the DGU instance values
# all DGU values would be combined into a single dict?
# App instance will use a lookup dict to find IO 
# App instance would querry and update DGU instance

# how does App know where to find its IO on DGU?


class IO():
	def __init__(self, register, format, type, id, name, description, value, units, last_change, local_log):
		self.register = register
		self.format = format
		self.type = type
		self.id = id
		self.name = name
		self.description = description
		self.value = value
		self.units = units
		self.last_change = last_change
		self.local_log = local_log


class DGU(): # stat1 = DGU("stat", 1, stat1_io_dict, "acu_code")
	def __init__(self, app, ref, dic, code):
		self.app = app
		self.ref = ref

		importlib = __import__('importlib')
		self.code = importlib.import_module(code)
		
		for key, value in dic.items():
			setattr(self, key, IO(register=value["register"], format=value["format"], type=value["type"], id=value["id"], name=value["name"], description=value["description"], value=value["value"], units=value["units"], last_change=value["last_change"], local_log=value["local_log"]))
			setattr(self, key+"_value", value["value"])


class Var():
	def __init__(self, id, name, description, value, units, last_change, local_log):
		self.id = id
		self.name = name
		self.description = description
		self.value = value
		self.units = units
		self.last_change = last_change
		self.local_log = local_log

	def print_values(self):
		print("def print_values is working")
		print(self.description)

	def print_var_values(self):
		#setattr(self, name+"_value", value["value"])
		for key, value in self.__dict__.items():
			print(key, value)


class App(): # acu1 = App("acu", 1, acu_var_dict, "acu_code")
	def __init__(self, app, ref, dic, code):
		self.app = app
		self.ref = ref

		importlib = __import__('importlib')
		self.code = importlib.import_module(code)
		
		for key, value in dic.items():
			setattr(self, key, Var(id=value["id"], name=value["name"], description=value["description"], value=value["value"], units=value["units"], last_change=value["last_change"], local_log=value["local_log"]))
			setattr(self, key+"_value", value["value"])


# Want a non-application specific Application, Var and Code class
# This provides for fewer classes, Creates standards for how Applications, Var and Code are interacted with







		#self.code=self
		#self.code.self=self

# ACU1.AV1_Object_Name.value
# ACU1.AV1_Description.value
# ACU1.AV1_Present_Value.value
# ACU1.AV1_Units.value
# ACU1.AV1_Input_Type.value
# ACU1.AV1_Configuration.value
# ACU1.AV1


# acu_code could have it's own var dic that we later use to set the app values???

use_var_class = 0



#acu1 = App("acu", 1, acu_var_dict, "acu_code")
#acu2 = App("acu", 2, acu_var_dict, "acu_code")
#stat1 = DGU("stat", 1, stat1_io_dict, "acu_code")
#stat2 = DGU("stat", 2, stat1_io_dict, "acu_code")

acu_app_dict = {
    "acu1": {"app":"acu", "ref": 1, "dic": acu_var_dict, "code": "acu_code"},
    "acu2": {"app":"acu", "ref": 2, "dic": acu_var_dict, "code": "acu_code"},
    "acu3": {"app":"acu", "ref": 3, "dic": acu_var_dict, "code": "acu_code"}
}

dgu_app_dict = {
    "dgu1": {"app":"dgu", "ref": 1, "dic": stat1_io_dict, "code": "acu_code"},
    "dgu2": {"app":"dgu", "ref": 2, "dic": stat1_io_dict, "code": "acu_code"},
    "dgu3": {"app":"dgu", "ref": 3, "dic": stat1_io_dict, "code": "acu_code"}
}




#dgu_apps = []
dgu_apps = {}
for key in dgu_app_dict:
    u = dgu_app_dict[key]
    app = u['app']+str(u['ref'])
    app = DGU(u['app'], u['ref'], u['dic'], u['code'],)
    dgu_apps.append(app)


acu_apps = []
for key in acu_app_dict:
    u = acu_app_dict[key]
    app = u['app']+str(u['ref'])
    app = App(u['app'], u['ref'], u['dic'], u['code'],)
    acu_apps.append(app)


for key in acu_apps:
	#print(key)
	print(f"{key.app}{key.ref}.acu_fan_def location is {key.code.acu_fan_def}")
	#print(key.vScheduleStateLocal.value)
	#key.code.acu_fan_def(key,f"It Worked for {key.app}{key.ref}")
	#print(key.vScheduleStateLocal)
	print()


for key in dgu_apps:
	#print(key)
	print(f"{key.app}{key.ref}.acu_fan_def location is {key.code.acu_fan_def}")
	#print(key.vScheduleStateLocal.value)
	#key.code.acu_fan_def(key,f"It Worked for {key.app}{key.ref}")
	#print(key.iReturnTemp.value)
	print()


print(dgu_apps[1].iReturnTemp.value)


if use_var_class == 1:
	print(acu1.vScheduleStateLocal)
	print(acu1.vScheduleStateLocal_id)
	print(acu1.vScheduleStateLocal_name)
	print(acu1.vScheduleStateLocal_description)
	print(acu1.vScheduleStateLocal_value)
	print(acu1.vScheduleStateLocal_units)
	print(acu1.vScheduleStateLocal_time)
	print(acu1.vScheduleStateLocal_log)


	print(f"ACU1 vScheduleStateLocal is {acu1.vScheduleStateLocal}")
	acu1.code.acu_fan_def2(acu1,"It Worked for ACU1!")
	print(f"ACU1 vScheduleStateLocal is {acu1.vScheduleStateLocal}")


	print(f"ACU2 vScheduleStateLocal is {acu2.vScheduleStateLocal}")
	#acu2.code.acu_fan_def2(acu2,"It Worked for ACU2!")
	#print(f"ACU2 vScheduleStateLocal is {acu2.vScheduleStateLocal}")

elif use_var_class == 2:
	print(f"ACU1 vScheduleStateLocal is {acu1.vScheduleStateLocal.value}")
	acu1.code.acu_fan_def(acu1,"It Worked for ACU1!")
	print(f"ACU1 vScheduleStateLocal is {acu1.vScheduleStateLocal.value}")


	print(f"ACU2 vScheduleStateLocal is {acu2.vScheduleStateLocal.value}")
	#acu2.code.acu_fan_def(acu2,"It Worked for ACU2!")
	#print(f"ACU2 vScheduleStateLocal is {acu2.vScheduleStateLocal.value}")




