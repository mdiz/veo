def acu_fan_def(self,print_it):
	print(f"Printing {print_it} to the screen for {self._app}{self._ref}")
	if self.iReturnTemp == 9999:
		lvFanCall = 0
		lvSafetyTripped = 9999
		if self.iSupplyTemp == 9999 and self.iSpaceTemp == 9999:
			lvFanCall = 1
			print("Fan call active. Fan set to run continuously during occupied periods")
		if lvFanCall == 1:
			print(f"lvFanCall is now set to {lvFanCall}")
			self.oFanEnable = lvFanCall


#import logging
#import logging.handlers as Handlers
#from collections import OrderedDict
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.client.sync import ModbusTcpClient as ModbusTCPClient
from pymodbus.compat import iteritems
import pymodbus.exceptions
import re
import time
#from dgu_dict import dgu_var_dict

def fn_rtu_scan(my_start=1, my_stop=256, my_timeout=0.1,my_baudrate=9600):
	"""Scan for RTU devices"""
	client = ModbusClient(method='rtu', port=fn_serial_port_list(), timeout=my_timeout, baudrate=my_baudrate)
	client.connect()
	error=0
	list=[]
	for i in range(my_start,my_stop):
		try:
			result = client.read_input_registers(1,1, unit=i)
			
			if result.registers:
				list.append(i)
		
		except:
			error=+ 1

	client.close()
	return list


def fn_serial_port_list():
	"""Return list of available serial ports"""
	#port = "/dev/ttyUSB0"
	# UPDATE add try: method to escape error
	import serial.tools.list_ports
	comport=[comport.device for comport in serial.tools.list_ports.comports()]
	if comport:
		port=comport[0]
	return port

def connect_rtu(my_port=fn_serial_port_list(), my_timeout=1, my_baudrate=9600):
	"""Connect to first available serial port with RTU protocol"""
	client = ModbusClient(method='rtu', port=my_port, timeout=my_timeout, baudrate=my_baudrate)
	client.connect()
	return client

def write_dgu_rtu(self):
	# UPDATE this needs work
	client = connect_rtu()
	if client.connect():

		rq = client.write_registers(2002, [0]*5, unit = self._mbus_rtu)
		# print(rq) # WriteMultipleRegisterResponse (2002,5)


		for key, value in self._dict.items(): # run througn writable vars and sent to DGU
			if value.writable == "Yes":
				#if value.name == "vSpaceTempOffset":
					#print(value.name, value.writable, " is writable")
					#rq = client.write_register(value.register - 1, value.value, unit = self._mbus_rtu)
					pass
	client.close()

def check_result(count, object):
	"""Check object based length"""
	x = 0
	if len(object) == count:
		x = 1
	return x

def ranges(nums):
	""" Returns consecutive numbers from a list"""
	nums = sorted(set(nums))
	gaps = [[s, e] for s, e in zip(nums, nums[1:]) if s+1 < e]
	edges = iter(nums[:1] + sum(gaps, []) + nums[-1:])
	return list(zip(edges, edges))

def merge_list(list1, list2):
	""" Merge two lists into list of tuples"""
    result = [(list1[i], list2[i]) for i in range(0, len(list1))]
    return result

def register_init16_read_pattern(self):
	""" Returns register read patterns from list of registers """
	init16_registers = [v["register"] for v in self._dict.values() if v["format"] == "Init16"] # list of init16 registers in dgu_dict
	patterns = ranges(init16_registers) # list of consecutive registers
	read_patterns = []
	for k,v in patterns: # Converts patterns for modbus read function
		k = k - 1
		v = v - k
		read_pattern.append((k, v))
	return read_patterns



def update_dgu(self):
# need function to build list or dict that will run read_init16_rtu and pair its result with register number for writing to dgu_dict
	read_patterns = register_init16_read_pattern(self)
	for register_start, register_count in read_patterns:
		read_result, check = read_init16_rtu(register_start, register_count)
		if check == 1:
			registers = (list(range(register_start + 1, register_start + register_count + 1))) # build list of registers
			update_list = merge_list(registers, read_result) # combine return of read_patterns with return of read_init16_rtu() into paired list to update dgu_dict 
			# use update_list to update dgu_dict







def read_init16_rtu(self, register_start, register_count, my_port=fn_serial_port_list(), my_timeout=1, my_baudrate=9600):
	client = connect_rtu()
	x = 0
	try:
		rr = client.read_input_registers(2000, 41, unit = self._mbus_rtu) # Read 16bit values.

		# may need to sleep here

		x = check_result(41,rr.registers)

	except (AttributeError, pymodbus.exceptions.ModbusIOException):
		print("DGU not found. DGU did not respond to network request")
		x = 0

	except (pymodbus.exceptions.ConnectionException):
		print("Commport connection failed.")
		x = 0

	except IndexError:
		print("DGU response does not match request")
		x = 0

	finally:
		client.close()

	return rr.registers, x





def read_dgu_rtu(self):
	client = connect_rtu()
	#if client.connect():
	x = 0
	try:
		float_registers = client.read_input_registers(1000, 38, unit = self._mbus_rtu) # Read 32bit float values
		float_registers = fn_decode_float2(float_registers.registers) # Decode 32bit float values  # fails here if no device 

		rr = client.read_input_registers(2000, 41, unit = self._mbus_rtu) # Read 16bit values.
		tt = client.read_input_registers(6566, 1, unit = self._mbus_rtu) # Read TemplateID

		time.sleep(1)

		x = check_result(41,rr.registers) * check_result(1,tt.registers) * check_result(38 // 2,float_registers)

		# UPDATE  THINK ABOUT DEFAULT VALUE FOR KEY IF SCAN RETURNS VALUES BUT SOME ARE MISSING
		# UPDATE  GUARD AGAINST FAILED SCANS
		# UPDATE GUARD AGAINST SCANS THAT RETURN NUMBER OF VALUES THAT DONT MATCH THE NUMBER OF KEYS
		# UPDATE INCLUDE TIME STAMP FOR HEARTBEAT


##### UPDATE #######  WE SHOULD HAVE THESE FUNCTIONS JUST RETURN THE VALUE LIST.  THEN PROCESS THE RESULTS IN AN INSTANCE FUNCTION TO ADD last_change AND local_log



		count = 0
		for key, value in self._dict.items():
			if value.format == "Float32" and value.register <= 1038 and count <= len(float_registers):  # fails here if no connection
				value.value = float_registers[count]
				count += 1
				
		count = 0
		for key, value in self._dict.items():
			if value.format == "Init16" and value.register <= 2041 and count <= len(rr.registers):
				value.value = rr.registers[count]
				count += 1
			elif value.format == "Init16" and value.register == 6567:
				value.value = tt.registers[0]

	except (AttributeError, pymodbus.exceptions.ModbusIOException):
		print("DGU not found. DGU did not respond to network request")
		x = 0

	except (pymodbus.exceptions.ConnectionException):
		print("Commport connection failed.")
		x = 0

	except IndexError:
		print("DGU response does not match request")
		x = 0

	finally:
		client.close()

	return x



def fn_read_VeoStat_1(self, my_dict, my_unit, my_port=fn_serial_port_list(), my_timeout=1, my_baudrate=9600):
	client = ModbusClient(method='rtu', port=my_port, timeout=my_timeout, baudrate=my_baudrate)
	client.connect()
	
	if client.connect():

		#rq = client.write_register(2002, 1, unit=my_unit)
		#rq = client.write_register(2003, 1, unit=my_unit)

		rq = client.write_registers(2002, [0]*5, unit=my_unit)

		#rq = client.write_register(self._dict.vLCDMessage.register - 1, 0, unit=my_unit)
		#rq = client.write_registers(self._dict.oFanEnable.register - 1, [1]*5, unit=my_unit)


		for key, value in my_dict.items():
			# run througn writable vars and sent to DGU
			if value.writable == "Yes":
				#print(value.writable, " is writable")
				#rq = client.write_register(value.register - 1, value.value, unit=my_unit)
				pass

		float_registers = client.read_input_registers(1000, 38, unit=my_unit) # Read 32bit float values
		float_registers = fn_decode_float2(float_registers.registers) # Decode 32bit float values

		rr = client.read_input_registers(2000, 41, unit=my_unit) # Read 16bit values.
		tt = client.read_input_registers(6566, 1, unit=my_unit) # Read TemplateID


	
	client.close()
	# UPDATE  THINK ABOUT DEFAULT VALUE FOR KEY IF SCAN RETURNS VALUES BUT SOME ARE MISSING
	# UPDATE  GUARD AGAINST FAILED SCANS
	# UPDATE GUARD AGAINST SCANS THAT RETURN NUMBER OF VALUES THAT DONT MATCH THE NUMBER OF KEYS
	# UPDATE INCLUDE TIME STAMP FOR HEARTBEAT
	count = 0
	for key, value in my_dict.items():
		if value["format"] == "Float32" and value["register"] <= 1038 and count <= len(float_registers):
			value["value"] = float_registers[count]
			count += 1
			pass

	count = 0
	# could limit this by len(rr.registers)
	for key, value in my_dict.items():
		if value["format"] == "Init16" and value["register"] <= 2041 and count <= len(rr.registers):
			value["value"] = rr.registers[count]
			count += 1
			pass
		elif value["format"] == "Init16" and value["register"] == 6567:
			value["value"] = tt.registers[0]

	count = 1
	for key, value in my_dict.items():
		#if value["format"] == "Init16":
		#if value["format"] == "Float32":
		#print(count, value["name"], value["value"])
		count += 1
		pass

#squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#print(squares[0:-1])


# build a list of decoded values and return to call
def fn_decode_float2(list):
	#use range() to build list to search by?
	values = []
	length=len(list)
	for i, val in enumerate(list): 
		if i * 2 < length:
			i=i*2
			y=i+1
			tmpReg=[list[i],list[y]]
			decoder = BinaryPayloadDecoder.fromRegisters(tmpReg,byteorder=Endian.Big,wordorder=Endian.Little)
			my_value=decoder.decode_32bit_float()
			values.append(my_value)
			#print(my_value)
			#print(decoder)
			#print(tmpReg)
	return values

def fn_decode_float(list):
	#use range() to build list to search by?
	length=len(list)
	for i, val in enumerate(list): 
		if i * 2 < length:
			i=i*2
			y=i+1
			tmpReg=[list[i],list[y]]
			decoder = BinaryPayloadDecoder.fromRegisters(tmpReg,byteorder=Endian.Big,wordorder=Endian.Little)
			my_value=decoder.decode_32bit_float()
			print(my_value)








#fn_read_VeoStat_1(dgu_var_dict,5)



#rtu_list = fn_rtu_scan(my_stop=30, my_timeout=0.1)

#for key in rtu_list:
	#print(key)



