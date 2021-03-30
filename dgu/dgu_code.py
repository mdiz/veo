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

from dgu_dict import dgu_var_dict

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


def fn_serial_port_list(): # Print current conected comports
	#my_port="/dev/ttyUSB0"
	#try:
	import serial.tools.list_ports
	comport=[comport.device for comport in serial.tools.list_ports.comports()]
	if comport:
		my_port=comport[0]

	#except:
		#print("Error: fn_serial_port_list")
	
	return my_port


def fn_read_VeoStat_1(my_unit, my_port=fn_serial_port_list(), my_timeout=1, my_baudrate=9600):
	client = ModbusClient(method='rtu', port=my_port, timeout=my_timeout, baudrate=my_baudrate)
	client.connect()
	
	if client.connect():

		#print("\nReading 32bit Registers " + "-" * 60)
		#rr = client.read_input_registers(1000, 38, unit=my_unit) # Read 32bit float values.
		#fn_decode_float(rr.registers)

		#print("\nReading 16bit Registers " + "-" * 60)
		rr = client.read_input_registers(2000, 41, unit=my_unit) # Read 16bit values.

	
	client.close()

	for i in rr.registers:
		print(i)

	

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





fn_read_VeoStat_1(5)



#rtu_list = fn_rtu_scan(my_stop=30, my_timeout=0.1)

#for key in rtu_list:
	#print(key)



