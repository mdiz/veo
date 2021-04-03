
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



class AttrDict(dict):
	""" Dictionary subclass whose entries can be accessed like attributes
		(as well as normally).
		https://stackoverflow.com/questions/38034377/object-like-attribute-access-for-nested-dictionary
	"""
    
	def __init__(self, *args, **kwargs):
		super(AttrDict, self).__init__(*args, **kwargs)
		self.__dict__ = self

	def format_var_dict(var_dict):
		""" Adds additional keys and initial values to var_dicts 
			durring init.
		"""
		for key, value in var_dict.items():
			value.last_change = 0 # UPDATE set this to a time
			value.local_log = []
			value.last_update = 0 # UPDATE set this to a time
		return var_dict

	@staticmethod
	def from_nested_dicts(data):
		""" Construct nested AttrDicts from nested dictionaries. """
		if not isinstance(data, dict):
			return data
		else:
			return AttrDict({key: AttrDict.from_nested_dicts(data[key])for key in data})



class DGU(): # acu1 = App("acu", 1, acu_var_dict, "acu_code")
	def __init__(self, app, ref, mbus_rtu, dict, code):
		self._app = app
		self._ref = ref
		self._mbus_rtu = mbus_rtu
		self._dict = AttrDict.format_var_dict(AttrDict.from_nested_dicts(dict))
		
		importlib = __import__('importlib')
		self._code = importlib.import_module(code)
		
		for key, value in dict.items():
			setattr(self, key, value["value"])

	#def __repr__(self):
		#return f"{self._app}{self._ref} {DGU}"
	
	def print_message(self):
		self._code.acu_fan_def(self,f"It Worked for {self._app}{self._ref}")

	def update_dgu(self):
		""" Reads IO from DGU and sets var_dict values.
			Returns 1 for success or 0 for failure.			
		"""
		result = self._code.read_dgu_rtu(self)
		#if result == 1:
		#	for key, value in self._dict.items():
		#		value.rec_time = 0 # UPDATE set this to a time
		return result

	@classmethod
	def create_app(cls, app, ref, mbus_rtu): # Used to create instance of class
		#dgu1 = DGU.create_dgu("dgu", 1)
		if app == "dgu":
			return cls(app, ref, mbus_rtu, dgu_var_dict, "dgu_code")
		#elif app == "acu":
			#return cls(app, ref, mbus_rtu, acu_var_dict, "acu_code")
		#elif app == "arc":
			#return cls(app, ref, mbus_rtu, arc_var_dict, "arc_code")
	

# UPDATE - HAVE dgu_apps DICT SET TO A CLASS DICT.  THEN WE COULD ACCESS IT FROM GLOBAL SPACE


	@classmethod
	def app_factory(cls): # Used to create instance and store in dict
		#dgu_var_dict - dict of vars
		#dgu_setup_dict - setup dict, DGU apps to create
		#dgu_apps  - dict of instances
		def build_apps(dict_name, setup_dict):
			for key, value in setup_dict.items():
				app_name = value['app']+str(value['ref'])
				app = DGU.create_app(value['app'], value['ref'], value['mbus_rtu'])
				dict_name[app_name] = app

		if "dgu_setup_dict" in locals() or "dgu_setup_dict" in globals():
			print("dgu_app_dict found")
			global dgu_apps # REMOVE THIS AFTER TESTING AND CREATE METHOD FOR ACCESSING THE DATA OUTSIDE INSTANCE 
			dgu_apps = {}
			build_apps(dgu_apps, dgu_setup_dict)
		"""
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
		"""


"""

class ACU(): # acu1 = App("acu", 1, acu_var_dict, "acu_code")
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
"""

#DGU.app_factory()
#print(dgu_apps)
#print(acu_apps)
#print(acu_apps["acu1"])

"""
# Example of how to access from list
for key, value in acu_apps.items():
	#print(key, value)
	#print(f"{value._app}{value._ref}.acu_fan_def location is {value._code.acu_fan_def}")
	#print(value.iReturnTemp)
	value.code.acu_fan_def2(value,f"It Worked for {value.app}{value.ref}")
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

"""



#DGU(self, app, ref, mbus_rtu, dict, code)
dgu1 = DGU("dgu", 1, 5, dgu_var_dict, "dgu_code")
dgu2 = DGU("dgu", 2, 6, dgu_var_dict, "dgu_code")


#print("dgu1 vSerialNumber ", dgu1._dict.vSerialNumber.value)
#print("dgu2 vSerialNumber ", dgu2._dict.vSerialNumber.value)

#result = dgu1.update_dgu()
#print(f"read_dgu_rtu(dgu1) result is {result}")

for i in range(1):
	#result = dgu1.update_dgu() * dgu2.update_dgu()
	#print(f"read_dgu(dgu1) result is {result}")
	pass


for key, value in dgu1._dict.items():
	#print(key, value)
	if value.format == "Init16":
		 pass


#print(dgu1._dict.values())

# how do we do this for init16 only

########  clearly we need to understand dictionary comprehension better##########################
# need to know the min init16 register then the number of consecutive ones 

def ranges(nums):
	""" Returns consecutive numbers from a list """
	nums = sorted(set(nums))
	gaps = [[s, e] for s, e in zip(nums, nums[1:]) if s+1 < e]
	edges = iter(nums[:1] + sum(gaps, []) + nums[-1:])
	return list(zip(edges, edges))


init16_registers = [v["register"] for v in dgu1._dict.values() if v["format"] == "Init16"]
init16_registers2 = [v["register"] for v in dgu1._dict.values() if v["format"] == "Init16"]
float32_registers = [v["register"] for v in dgu1._dict.values() if v["format"] == "Float32"]
print(f"init16_registers are {init16_registers}")

my_range = ranges(init16_registers) # Use ranges() find consecutive numbers in list
print(f"my_range results are {my_range}")

test = []
for k,v in my_range:
	#print(k,v)
	k = k - 1
	v = v - k
	#print(k, v)
	print(k, v)
	test.append((k, v))

print(test) # list of register_start and register_count values
# [(2000, 41), (6566, 1)] 

print(f"test result is {test[0]}")
for k, v in test:
	#print(k,v)
	print(f"register is {k} and value is {v}")
print(test[0])

dgu1._code.update_dgu(dgu1)




min_Float32_register = [min(int(d['register']) for d in dgu1._dict.values() if d['format'] == 'Float32')]
min_Init16_register = min(int(d['register']) for d in dgu1._dict.values() if d['format'] == 'Init16')

max_Float32_register = max(int(d['register']) for d in dgu1._dict.values() if d['format'] == 'Float32')
max_Init16_register = max(int(d['register']) for d in dgu1._dict.values() if d['format'] == 'Init16')

#print(min_Float32_register)
#print(min_Init16_register)

#print(max_Float32_register)
#print(max_Init16_register)





init16, result = dgu1._code.read_init16_rtu(dgu1, 2000, 41,)
if result == 1:
	#print(init16)
	#print(f"init16 length is {len(init16)}")
	pass






#print("dgu1 vSerialNumber ", dgu1._dict.vSerialNumber.value)
#print("dgu2 vSerialNumber ", dgu2._dict.vSerialNumber.value)


#print(dgu1._dict.vSerialNumber.keys())


#print(dgu1._dict.vSerialNumber)
# keys
# values
# items
# update
# from_nested_dicts


for key, value in dgu1._dict.items():
	#print(key, value.value)
	pass

for key, value in dgu1._dict.items():
	#print(key, value.local_log)
	pass



"""
oAO1 Yes
oAO2 Yes
oAO3 Yes
oAO4 Yes
vSpaceTempOffset Yes
vBackupCoolingSetpoint Yes
vBackupHeatingSetpoint Yes
vBackupMaxHeatingSetpoint Yes
vBackupMinCoolingSetpoint Yes
oFanEnable Yes
oCompressor1Enable Yes
oCompressor2Enable Yes
oHeat1Enable Yes
oHeat2Enable Yes
vEnableHeatPumpControl Yes
vEnableRemoteSpaceTemp Yes
vEnableBackupControl Yes
vForceBackupControl Yes
vAlarmActive Yes
vTicketActive Yes
vSensorFail Yes
vCoolFail Yes
vHeatFail Yes
vDisableKeypad Yes
vEnableKeypadAdmin Yes
ALSC Yes
CPUALSC Yes
vLCDMessage Yes
vDegUnits Yes
vSiteID Yes
vModbusAddress Yes


iSpaceTemp 72.50194549560547
iReturnTemp 71.72992706298828
iSupplyTemp 71.72262573242188
iSpaceTempRemote -58.06752014160156
iAI5 -58.0
iAI6 -58.0
iAI7 -58.0
iAI8 -58.0
iLightLevel 60.25
oAO1 8.757414752797944e-41
oAO2 0.0
oAO3 0.0
oAO4 0.0
vCalculatedSpaceTemp 72.5
vSpaceTempOffset 4.223093181935701e-41
vBackupCoolingSetpoint 71.0
vBackupHeatingSetpoint 60.0
vBackupMaxHeatingSetpoint 70.0
vBackupMinCoolingSetpoint 73.0
iFanStatus 0
iPushButton 0
oFanEnable 0
oCompressor1Enable 0
oCompressor2Enable 0
oHeat1Enable 0
oHeat2Enable 0
vUnitStagesCooling 2
vUnitStagesHeating 1
vUnitIsHeatPump 0
vEnableHeatPumpControl 0
vUnitGasHeat 0
vUnitEconomizer 0
vUnitDehumidification 0
vEnableRemoteSpaceTemp 0
vEnableBackupControl 0
vForceBackupControl 0
vBackupControlActive 0
vUnitNumber 1
vUnitType 20
vAlarmActive 1
vTicketActive 1
vSensorFail 0
vCoolFail 0
vHeatFail 0
vDisableKeypad 0
vEnableKeypadAdmin 0
vALSC 0
vCPUALSC 0
vLCDMessage 0
vDegUnits 0
vSiteID 25
vModbusAddress 5
vSerialNumber 19348
vModbusCommFail 0
vDeviceResets 32
vModbusPacketError 0
vModbusCRCError 5
vModbusLastComm 0
vAverageCPULoopTime 100
vMaxCPULoopTime 235
vTemplateID 1


# Example of how to access from library
for key, value in dgu_apps.items():
	#print(key, value)
	#print(key)
	#print(value)



	x = value._dict["vSerialNumber"]["value"]
	print(f"Before updating {key} points {x}")

	value._code.fn_read_VeoStat_1(value._dict, value._mbus_rtu)
	value._code.fn_read_VeoStat_1(value._dict, value._mbus_rtu)

	x = value._dict["vSerialNumber"]["value"]
	print(f"After updating {key} points {x}")





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
		#print(value2)
		if not key2.startswith(("_")) and key2.endswith(("_value")):
			#print(key2)
			#print(value2)
			for key3, value3 in value2.items():
				#print(key3)
				if key3 == "register":
					#print(key3, value3)
					if value3 == 12:
						#print(value.oFanEnable)
						#value.print_message()
						#print(value.oFanEnable)
						pass
		elif not key2.startswith(("_")) and not key2.endswith(("_value")):
			#print(key2, value2)
			pass

	print()
"""