
import sys
#print(sys.path)
sys.path.append('/home/mikedismore/projects/veo/dgu')
sys.path.append('/home/mikedismore/projects/veo/config')
from acu_dict import acu_var_dict
from dgu_dict import dgu_var_dict
from setup import acu_setup_dict
from setup import dgu_setup_dict

# Need group name for DGU, ACU, ARC, PFC...
	# applications


class DGU(): # acu1 = App("acu", 1, acu_var_dict, "acu_code")
	def __init__(self, app, ref, dic, code):
		self._app = app
		self._ref = ref
		#setattr(self, "dic", Var2(dic=dic))
		
		importlib = __import__('importlib')
		self._code = importlib.import_module(code)
		
		for key, value in dic.items():
			#setattr(self, key+"_value", Var2(ref=value["ref"], name=value["name"], description=value["description"], value=value["value"], units=value["units"], last_change=value["last_change"], local_log=value["local_log"]))
			setattr(self, key, value["value"])
			setattr(self, key+"_value", value)

	def __repr__(self):
		return f"{self._app}{self._ref} {DGU}"

	def print_message(self):
		self._code.acu_fan_def(self,f"It Worked for {self._app}{self._ref}")

	@classmethod
	def create_app(cls, app, ref): # Used to create instance of class
		#dgu1 = DGU.create_dgu("dgu", 1)
		if app == "dgu":
			return cls(app, ref, dgu_var_dict, "dgu_code")
		elif app == "acu":
			return cls(app, ref, acu_var_dict, "acu_code")
		elif app == "arc":
			return cls(app, ref, arc_var_dict, "arc_code")
	

# UPDATE - HAVE dgu_apps DICT SET TO A CLASS DICT.  THEN WE COULD ACCESS IT FROM GLOBAL SPACE


	@classmethod
	def app_factory(cls): # Used to create instance and store in dict
		#dgu_var_dict - dict of vars
		#dgu_setup_dict - setup dict, DGU apps to create
		#dgu_apps  - dict of instances
		def build_apps(dict_name, setup_dict):
			for key, value in setup_dict.items():
				app_name = value['app']+str(value['ref'])
				app = DGU.create_app(value['app'], value['ref'])
				dict_name[app_name] = app

		if "dgu_setup_dict" in locals() or "dgu_setup_dict" in globals():
			print("dgu_app_dict found")
			global dgu_apps # REMOVE THIS AFTER TESTING AND CREATE METHOD FOR ACCESSING THE DATA OUTSIDE INSTANCE 
			dgu_apps = {}
			build_apps(dgu_apps, dgu_setup_dict)

		if "acu_setup_dict" in locals() or "acu_setup_dict" in globals():
			print("acu_app_dict found")
			global acu_apps # REMOVE THIS AFTER TESTING AND CREATE METHOD FOR ACCESSING THE DATA OUTSIDE INSTANCE 
			acu_apps = {}
			build_apps(acu_apps, acu_setup_dict)

		if "arc_setup_dict" in locals() or "arc_setup_dict" in globals():
			print("arc_app_dict found")
			global arc_apps # REMOVE THIS AFTER TESTING AND CREATE METHOD FOR ACCESSING THE DATA OUTSIDE INSTANCE 
			arc_apps = {}
			build_apps(arc_apps, arc_setup_dict)


DGU.app_factory()
#print(dgu_apps)
#print(acu_apps)
#print(acu_apps["acu1"])

"""
# Example of how to access from list
for key, value in acu_apps.items():
	#print(key, value)
	#print(f"{value._app}{value._ref}.acu_fan_def location is {value._code.acu_fan_def}")
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
	#print(f"{value._app}{value._ref}.acu_fan_def location is {value._code.acu_fan_def}")
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
						print(value.oFanEnable)
						value.print_message()
						print(value.oFanEnable)
						pass
	print()
"""