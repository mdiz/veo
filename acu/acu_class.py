
import sys
#print(sys.path)
sys.path.append('/home/mikedismore/projects/veo/dgu')
sys.path.append('/home/mikedismore/projects/veo/config')
from acu_dict import acu_var_dict
from dgu_dict import dgu_var_dict
from setup import acu_app_dict
from setup import dgu_app_dict


class DGU(): # acu1 = App("acu", 1, acu_var_dict, "acu_code")
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



class App(): # acu1 = App("acu", 1, acu_var_dict, "acu_code")
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
		self.__code.acu_fan_def(self,f"It Worked for {self._app}{self._ref}")



# Example using a library to instantiate class
# THESE CAN BE CLASS METHODS USED TO CREATE THE INSTANCE
dgu_apps = {}
for key, value in dgu_app_dict.items():
	app_name = value['app']+str(value['ref'])
	app = App(value['app'], value['ref'], dgu_var_dict, "acu_code")
	dgu_apps[app_name] = app

acu_apps = {}
for key, value in acu_app_dict.items():
	app_name = value['app']+str(value['ref'])
	app = App(value['app'], value['ref'], acu_var_dict, "acu_code")
	acu_apps[app_name] = app


# Example of how to access from list
for key, value in acu_apps.items():
	#print(key)
	#print(f"{key.app}{key.ref}.acu_fan_def location is {key.code.acu_fan_def}")
	#print(key.vScheduleStateLocal.value)
	#key.code.acu_fan_def(key,f"It Worked for {key.app}{key.ref}")
	#print(key.code.acu_fan_def)
	#print(key.app, key.ref)
	#key.vScheduleStateLocal.value = 67
	#print(key.vScheduleStateLocal.value)
	#print()
	for key2, value2 in value.__dict__.items():
		#print(key2)
		if not key2.startswith(("_")) and key2.endswith(("_value")):
			#print(key2)
			for key3, value3 in value2.items():
				#print(key3)
				if key3 == "ref":
					#print(key3, value3)
					if value3 == 1:
						print(value.vScheduleStateLocal)
						value.print_message()
						print(value.vScheduleStateLocal)
						pass
	print()


# Example of how to access from library
for key, value in dgu_apps.items():
	#print(key, value)
	#print(f"{value.app}{value.ref}.acu_fan_def location is {value.code.acu_fan_def}")
	#print(value.iReturnTemp)
	#value.code.acu_fan_def2(value,f"It Worked for {value.app}{value.ref}")
	#print(value.print_message)
	#print(value.oFanEnable)
	#value.print_message()
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




acu11 = App("acu", 1, acu_var_dict, "acu_code")
stat11 = App("stat", 11, dgu_var_dict, "acu_code")


for key, value in stat11.__dict__.items():
	#if not key.startswith(("_")) and not key.endswith(("_value")):
	#if not key.endswith(("_value")):
	if not key.startswith(("_")) and key.endswith(("_value")):
		#print(key)
		for key2, value2 in value.items():
			if key2 == "register":
				#print(key2, value2)
				pass










