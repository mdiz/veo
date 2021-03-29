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
import re


def fn_module_def():
	#import re
	#OPENING FILES 595
	#REGULAR EXPERSSIONS line 1746
	try:
		with open("deviceconfig.txt") as file: # with statement will allways close the file, even on error 
			for line in file:
				#if not re.match(r"^#.*", line):
				setting=re.match(r"(^[a-zA-Z][\w]+)([\s]*=[\s]*)([\w\d]+).*$", line)
				if setting:
					i = setting.group(1)
					v = setting.group(3)
					print(i, v)
		file.close() 
	except:
		print("fn_module_def failed")


def fn_serial_port_list(): # Print current conected comports
	#my_port="/dev/ttyUSB0"
	try:
		import serial.tools.list_ports
		comport=[comport.device for comport in serial.tools.list_ports.comports()]
		if comport:
			my_port=comport[0]

	except:
		print("Error: fn_serial_port_list")
	
	return my_port


def fn_rtu_scan(my_start=1, my_stop=256, my_timeout=0.1,my_baudrate=9600):
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


def fn_tcp_scan(my_start=1, my_stop=256, my_port=502, my_timeout=0.05):
	list=[]
	for i in range(my_start,my_stop):
		#print("192.168.11." + str(i))
		client = ModbusTCPClient("192.168.11." + str(i), my_port, timeout=my_timeout)
		client.connect()

		if client.connect():
			list.append("192.168.11." + str(i))

		client.close()
	
	return list




print(fn_serial_port_list())