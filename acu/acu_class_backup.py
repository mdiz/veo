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

# provides discussion on how to reduce overhead of many class instances https://pythonspeed.com/articles/python-object-memory/

# ~/.dropbox-dist/dropboxd



#print(acu_dict.__file__) # to find where module is stored
#print(dir()) # print names in namespace
#print(dir(acu_dict)) # print names in module


from acu_dict import acu_var_dict
#from acu_code import acu_fan_def
#import acu_code



stat1_io_dict = {
"iReturnTemp":{"register":1, "format":"Float32", "type":"input", "ref":1, "name":"iReturnTemp", "description":"Return Temperature", "value":9999, "units":64, "last_change":1234, "local_log":0},
"iSupplyTemp":{"register":2, "format":"Float32", "type":"input", "ref":2, "name":"iSupplyTemp", "description":"Supply Temperature", "value":9999, "units":64, "last_change":1234, "local_log":0},
"iSpaceTemp":{"register":3, "format":"Float32", "type":"input", "ref":3, "name":"iSpaceTemp_ScheduleOverride", "description":"Space Temperature", "value":9999, "units":64, "last_change":1234, "local_log":0},
"iUnitAmperage":{"register":4, "format":"Float32", "type":"input", "ref":4, "name":"iUnitAmperage", "description":"Unit Amperage", "value":9999, "units":3, "last_change":1234, "local_log":0},
"iLocalTempAdjust":{"register":5, "format":"Float32", "type":"input", "ref":5, "name":"iLocalTempAdjust", "description":"Local Space Temperature Adjustment", "value":9999, "units":64, "last_change":1234, "local_log":0},
"iAuxUnitStatus":{"register":6, "format":"Float32", "type":"input", "ref":6, "name":"iAuxUnitStatus", "description":"Aux Unit Status", "value":9999, "units":64, "last_change":1234, "local_log":0},
"oFanEnable":{"register":7, "format":"Float32", "type":"output", "ref":1, "name":"oFanEnable", "description":"Fan Enable", "value":9999, "units":95, "last_change":1234, "local_log":0},
"oCompressor1Enable":{"register":8, "format":"Float32", "type":"output", "ref":2, "name":"oCompressor1Enable", "description":"Compressor 1 Enable", "value":9999, "units":95, "last_change":1234, "local_log":0},
"oCompressor2Enable":{"register":9, "format":"Float32", "type":"output", "ref":3, "name":"oCompressor2Enable", "description":"Compressor 2 Enable", "value":9999, "units":95, "last_change":1234, "local_log":0},
"oHeat1Enable":{"register":10, "format":"Float32", "type":"output", "ref":4, "name":"oHeat1Enable", "description":"Heat 1 Enable", "value":9999, "units":95, "last_change":1234, "local_log":0},
"oHeat2Enable":{"register":11, "format":"Float32", "type":"output", "ref":1, "name":"oHeat2Enable", "description":"Heat 2 Enable", "value":9999, "units":95, "last_change":1234, "local_log":0},
"oEconomizerEnable":{"register":12, "format":"Float32", "type":"output", "ref":2, "name":"oEconomizerEnable", "description":"Economizer Enable", "value":9999, "units":95, "last_change":1234, "local_log":0},
}


#"vReturnTempConditionedValue":{"id":1, "name":"vReturnTempConditionedValue", "description":"Return Temperature Conditioned Value", "value":70.863, "units":64, "last_change":1234, "local_log":0},
"""
dgu_apps["dgu1"].iReturnTemp.value = 1234
dgu_apps["dgu1"].iReturnTemp.value = 1234
dgu_apps["dgu1"].iReturnTemp.value = 1234


dgu = "dgu1"
dgu_point_ref = 1

acu_apps["acu1"].vReturnTempConditionedValue.value = dgu_apps["dgu1"].iReturnTemp.value
"""
"""
for key, value in stat1_io_dict.items():
	pass
	#print(key)
	#print(value["register"])
	if value["register"] == 1:
		print(value["name"])



pairs = {1: "apple",
  "orange": [2, 3, 4], 
  True: False, 
  None: "True",
}
print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))

print(pairs[1])

print("orange" in pairs)
print("three" in pairs)
print(4 not in pairs)

primes = {1: 2, 2: 3, 4: 7, 7:17}
print(primes[primes[4]])
"""


class TestDict():
	first = "Mike"
	last = "Dismore"
	my_dict = {
"iReturnTemp":{"register":1, "format":"Float32", "type":"input", "ref":1, "name":"iReturnTemp", "description":"Return Temperature", "value":9999, "units":64, "last_change":1234, "local_log":0},
"iSupplyTemp":{"register":2, "format":"Float32", "type":"input", "ref":2, "name":"iSupplyTemp", "description":"Supply Temperature", "value":9999, "units":64, "last_change":1234, "local_log":0},
"iSpaceTemp":{"register":3, "format":"Float32", "type":"input", "ref":3, "name":"iSpaceTemp_ScheduleOverride", "description":"Space Temperature", "value":9999, "units":64, "last_change":1234, "local_log":0},
"iUnitAmperage":{"register":4, "format":"Float32", "type":"input", "ref":4, "name":"iUnitAmperage", "description":"Unit Amperage", "value":9999, "units":3, "last_change":1234, "local_log":0},
"iLocalTempAdjust":{"register":5, "format":"Float32", "type":"input", "ref":5, "name":"iLocalTempAdjust", "description":"Local Space Temperature Adjustment", "value":9999, "units":64, "last_change":1234, "local_log":0},
"iAuxUnitStatus":{"register":6, "format":"Float32", "type":"input", "ref":6, "name":"iAuxUnitStatus", "description":"Aux Unit Status", "value":9999, "units":64, "last_change":1234, "local_log":0},
"oFanEnable":{"register":7, "format":"Float32", "type":"output", "ref":1, "name":"oFanEnable", "description":"Fan Enable", "value":9999, "units":95, "last_change":1234, "local_log":0},
"oCompressor1Enable":{"register":8, "format":"Float32", "type":"output", "ref":2, "name":"oCompressor1Enable", "description":"Compressor 1 Enable", "value":9999, "units":95, "last_change":1234, "local_log":0},
"oCompressor2Enable":{"register":9, "format":"Float32", "type":"output", "ref":3, "name":"oCompressor2Enable", "description":"Compressor 2 Enable", "value":9999, "units":95, "last_change":1234, "local_log":0},
"oHeat1Enable":{"register":10, "format":"Float32", "type":"output", "ref":4, "name":"oHeat1Enable", "description":"Heat 1 Enable", "value":9999, "units":95, "last_change":1234, "local_log":0},
"oHeat2Enable":{"register":11, "format":"Float32", "type":"output", "ref":1, "name":"oHeat2Enable", "description":"Heat 2 Enable", "value":9999, "units":95, "last_change":1234, "local_log":0},
"oEconomizerEnable":{"register":12, "format":"Float32", "type":"output", "ref":2, "name":"oEconomizerEnable", "description":"Economizer Enable", "value":9999, "units":95, "last_change":1234, "local_log":0},
}


me = TestDict()

#print(me.my_dict["iReturnTemp"]["value"])



class IO():
	def __init__(self, register, format, type, ref, name, description, value, units, last_change, local_log):
		self.register = register
		self.format = format
		self.type = type
		self.ref = ref
		self.name = name
		self.description = description
		self.value = value
		self.units = units
		self.last_change = last_change
		self.local_log = local_log


class DGU(): # stat1 = DGU("stat", 1, stat1_io_dict, "acu_code")
# Want a non-application specific Application, Var and DGP class
# This provides for fewer classes, Creates standards for how Applications, Var and Code are interacted with

	def __init__(self, app, ref, dic, code):
		self.app = app
		self.ref = ref

		importlib = __import__('importlib')
		self.code = importlib.import_module(code)
		
		for key, value in dic.items():
			#setattr(self, key, IO(register=value["register"], format=value["format"], type=value["type"], ref=value["ref"], name=value["name"], description=value["description"], value=value["value"], units=value["units"], last_change=value["last_change"], local_log=value["local_log"]))
			#setattr(self, key+"_value", value["value"])
			setattr(self, key, value["value"])


class Var():
	def __init__(self, ref, name, description, value, units, last_change, local_log):
		self.ref = ref
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


class Var2():
	__slots__ = ["dic", "__dict__"]
	def __init__(self, dic):
		self.dic = dic

	def print_values(self):
		print("def print_values is working")
		print(self.description)

	def print_var_values(self):
		#setattr(self, name+"_value", value["value"])
		for key, value in self.__dict__.items():
			print(key, value)


#myDict = dict(ref="ref", name="name", description="description")
#myDict = {"ref":"ref", "name":"name", "description":"description"}
#print(myDict["ref"])



class App(): # acu1 = App("acu", 1, acu_var_dict, "acu_code")
# Want a non-application specific Application, Var and DGP class
# This provides for fewer classes, Creates standards for how Applications, Var and Code are interacted with

	def __init__(self, app, ref, dic, code):
		self.app = app
		self.ref = ref

		importlib = __import__('importlib')
		self.code = importlib.import_module(code)
		
		for key, value in dic.items():
			#setattr(self, key, Var(ref=value["ref"], name=value["name"], description=value["description"], value=value["value"], units=value["units"], last_change=value["last_change"], local_log=value["local_log"]))
			#setattr(self, key+"_value", value["value"])
			setattr(self, key, value["value"])
			#setattr(self, key+"_Var2", Var2(value=value["value"]))



class App2(): # acu1 = App("acu", 1, acu_var_dict, "acu_code")
# Want a non-application specific Application, Var and DGP class
# This provides for fewer classes, Creates standards for how Applications, Var and Code are interacted with

	def __init__(self, app, ref, dic, code):
		self._app = app
		self._ref = ref
		#setattr(self, "dic", Var2(dic=dic))
		

		importlib = __import__('importlib')
		self.__code = importlib.import_module(code)
		
		for key, value in dic.items():
			#setattr(self, key+"_value", Var2(ref=value["ref"], name=value["name"], description=value["description"], value=value["value"], units=value["units"], last_change=value["last_change"], local_log=value["local_log"]))
			#setattr(self, key+"_value", value["value"])
			setattr(self, key, value["value"])
			setattr(self, key+"_value", value)

			#setattr(self, key+"_Var2", Var2(value=value["value"]))
	#@classmethod
	def print_message(self):
		self.__code.acu_fan_def3(self,f"It Worked for {self._app}{self._ref}")


# 1 - Store var.value on App and var_dict on Var
# 2 - Store var_dict on App and var.value on Var
# 3 - Store var.value and var_dict on App
# 4 - Store var.value on VarValue and var_dict on VarDict

# If all the vars are in a dict then it's much less overhead
# if vars are not objects how will code access them without junking up code?
# If var.value is object but var_dict is in App dict then App code is simple and accessing var_dict is done through methods



# acu1.vScheduleStateLocal
# acu1.vScheduleStateLocal_id
# acu1.vScheduleStateLocal_name
# acu1.vScheduleStateLocal_description
# acu1.vScheduleStateLocal_value
# acu1.vScheduleStateLocal_units
# acu1.vScheduleStateLocal_time
# acu1.vScheduleStateLocal_log





		#self.code=self
		#self.code.self=self

# ACU1.AV1_Object_Name.value - updated each IO scan?
# ACU1.AV1_Description.value
# ACU1.AV1_Present_Value.value
# ACU1.AV1_Units.value
# ACU1.AV1_Input_Type.value
# ACU1.AV1_Configuration.value
# ACU1.AV1 - updated before and after each program scan

#ME.CFG1_Node_Instance.value
#DEV5000.CFG1_Time_Sync_String
#ME.CFG1_Firmware_Version.value
#ME.CFG1_Serial_Number.value
#ME.CFG1_Model.value
#ME.CFG1_CPU_Usage_Lua_Script.value 



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


# Example using a library to instantiate class
# THESE CAN BE CLASS METHODS USED TO CREATE THE INSTANCE
dgu_apps = {}
for key, value in dgu_app_dict.items():
	#print(key)
	app_name = value['app']+str(value['ref'])
	app = App2(value['app'], value['ref'], value['dic'], value['code'],)
	dgu_apps[app_name] = app

# Example using a list to instantiate class
#acu_apps = []
#for key in acu_app_dict:
#    u = acu_app_dict[key]
#    app = u['app']+str(u['ref'])
#    app = App(u['app'], u['ref'], u['dic'], u['code'],)
#    acu_apps.append(app)

acu_apps = {}
for key, value in acu_app_dict.items():
	#print(key)
	app_name = value['app']+str(value['ref'])
	app = App(value['app'], value['ref'], value['dic'], value['code'],)
	acu_apps[app_name] = app



# Example of how to access from list
for key in acu_apps:
	#print(key)
	#print(f"{key.app}{key.ref}.acu_fan_def location is {key.code.acu_fan_def}")
	#print(key.vScheduleStateLocal.value)
	#key.code.acu_fan_def(key,f"It Worked for {key.app}{key.ref}")
	#print(key.code.acu_fan_def)
	#print(key.app, key.ref)
	#key.vScheduleStateLocal.value = 67
	#print(key.vScheduleStateLocal.value)
	#print()
	pass

# Example of how to access from library
for key, value in dgu_apps.items():
	#print(key, value)
	#print(f"{value.app}{value.ref}.acu_fan_def location is {value.code.acu_fan_def}")
	#print(value.iReturnTemp)
	#value.code.acu_fan_def2(value,f"It Worked for {value.app}{value.ref}")
	print(value.print_message)
	#print(value.oFanEnable)
	value.print_message()
	#print(value.oFanEnable)
	#print(value._app, value._ref)
	#value.iReturnTemp = 76
	#print(value.iReturnTemp)
	for key2, value2 in value.__dict__.items():
		#print(key2)
		if not key2.startswith(("_")) and key2.endswith(("_value")):
			#print(key2)
			for key3, value3 in value2.items():
				if key3 == "register":
					#print(key3, value3)
					if value3 == 12:
						#print(value.oFanEnable)
						#value.print_message()
						#print(value.oFanEnable)
						pass

	print()
	pass



# Example of how to set App Var objects to DGP IO objects
#for dgu, dgu_object in dgu_apps.items():
	#print(dgu_object)
	#for dgu_vars, io_object in dgu_object.__dict__.items():
		#print(io_object)
		#for key in io_object:
			#print(io_object[key])



	for dgu, dgu_object in dgu_apps.items():
		#for key, value in dgu_object.__dict__.items(): # to only return iter items
		for key, value in vars(dgu_object).items(): # There is a function that exposes the __dict__ method. It's equivalent, but probably more pythonic. The vars built-in function 
			if not key.startswith(("app", "ref", "code")):
				#print(key, value)
				#print(dgu_object.iReturnTemp.value)
				pass






#im here in my review - https://codereview.stackexchange.com/questions/126100/recording-all-instances-of-a-class-python/225775
#trying to iterate over the instantiated class to find App Vars that need to be updated by DGU IO
#hink the issue is the way i'm iterating or the way it's stored in the Var and IO Class instance.













# Example of how to access from global namespace
#print(acu_apps[1].vScheduleStateLocal.value) # if in list

#print(dgu_apps["dgu1"].iReturnTemp.value) # if in library
#dgu_apps["dgu1"].iReturnTemp.value = 1234
#print(dgu_apps["dgu1"].iReturnTemp.value) # if in library

# Example of setting ACU var value to DGU point value
#print(acu_apps["acu1"].vReturnTempConditionedValue.value)
#acu_apps["acu1"].vReturnTempConditionedValue.value = dgu_apps["dgu1"].iReturnTemp.value
#print(acu_apps["acu1"].vReturnTempConditionedValue.value)

# Example of instantiated class in global namespace 
#acu1 = App("acu", 1, acu_var_dict, "acu_code")
#acu2 = App("acu", 2, acu_var_dict, "acu_code")
#stat1 = DGU("stat", 1, stat1_io_dict, "acu_code")
#stat2 = DGU("stat", 2, stat1_io_dict, "acu_code")


acu11 = App2("acu", 1, acu_var_dict, "acu_code")
stat11 = App2("stat", 11, stat1_io_dict, "acu_code")


#stat11._code.acu_fan_def3(stat11,f"It Worked for {stat11.app}{stat11.ref}")
#stat11.print_message()

#print(acu11.var)
#print(acu11.var.vScheduleStateLocal.value)
#print(acu11.var.vScheduleStateLocal.value)
#print(acu11.vScheduleStateLocal_value.name)

#stat11.dic["iReturnTemp"]["description"] = "new description"
#print(stat11.dic["iReturnTemp"]["description"])

#print(stat11.iReturnTemp)
#print(stat11.iReturnTemp_value)
#rint(stat11.iReturnTemp_value["name"])


for key, value in stat11.__dict__.items():
	#if not key.startswith(("_")) and not key.endswith(("_value")):
	#if not key.endswith(("_value")):
	if not key.startswith(("_")) and key.endswith(("_value")):
		#print(key)
		for key2, value2 in value.items():
			if key2 == "register":
				#print(key2, value2)
				pass









# Example of 
#if __name__ == "main": # execute some code only if the file was run directly, and not imported
	

for var, var_object in stat11.__dict__.items():
	#print(var_object)
	#print([a for a in dir(var) if not a.startswith('0')])
	#print([a for a in dir(var_object) if a.startswith('__main__.Var object')])
	#if var_object.startswith('__main__.IO object'): 
		#print(var_object)
	#for a in dir(var_object):
		#print(a)
		#if not a.startswith('__'):
			pass
			#print(a)


for key in dir(stat11):
	#print(key)
	if not key.startswith("__") and not key.startswith("app") and not key.startswith("code") and not key.startswith("ref"):
		#print(stat1.key)
		pass












#print([a for a in dir(acu1) if not a.startswith('ref') and not a.startswith('__')])



use_var_class = 0

# examples of how to access if instantiated in global namespace
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




