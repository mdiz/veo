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


#print(acu_dict.__file__) # to find where module is stored
#print(dir()) # print names in namespace
#print(dir(acu_dict)) # print names in module


from acu_dict import acu_var_dict
#from acu_code import acu_fan_def
#import acu_code


class AppCode():
	def acu_fan(self):
		if self.vDisableUnitControl.value == 0:
			lvFanCall = 0
			lvSafetyTripped = 0
			if self.vUnitFanRunMode.value == 1 and self.vScheduleStateLocal.value != 0:
				lvFanCall = 1
				print("Fan call active. Fan set to run continuously during occupied periods")


class Var():
	def __init__(self, id, name, description, value, units, last_change, local_log):
		self.id = id
		self.name = name
		self.description = description
		self.value = value
		self.units = units
		self.last_change = last_change
		self.local_log = local_log

	

class App():
	#def __init__(self, app_name, id, var_dict, app_code):
	def __init__(self, app_name, id, var_dict):
		self.app_name = app_name
		self.id = id
		for key, value in var_dict.items():
			setattr(self, key, Var(id=value["id"], name=value["name"], description=value["description"], value=value["value"], units=value["units"], last_change=value["last_change"], local_log=value["local_log"]))
		#setattr(self, acu_fan, app_code)
		#self.app_code = app_code
		from acu_code import acu_fan_def

# import app_code to global namespace and use with App class.  
# if that works try import into local class namespace




	def var_link(link, var):
		pass
		#print(self.)


	def save_app(self):
		# Saves attribute values to file
		print(self.app_name)
		#print(acu1.__dict__) # trying to use this to save to dict
		print(self.vLogFileDuration.name)
		if self.vLogFileDuration.value > 0:
			print(f"{self.vLogFileDuration.name} is {self.vLogFileDuration.value}")



#acu1 = App("acu1", 1, acu_var_dict, acu_fan_def)
#acu1 = App("acu1", 1, acu_var_dict, acu_code)
acu1 = App("acu1", 1, acu_var_dict)

#space_temp = Var(22, "space_temp", "Space Temperature", 74, 9, 1234, 1)
print("done")
print(dir(acu1))
#print(acu1.vUnitFanDeltatControlEnable.value)
#print(acu1.app_code)
#acu1.app_code(acu1)
#print(acu_code.acu_fan_def)
#print(acu1.app_code.acu_fan_def)
#acu1.app_code.acu_fan_def(acu1)
#acu1.acu_fan_def(acu1)