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


def fn_serial_port_list():
	#error=1
	my_port="/dev/ttyUSB0"
	try:
		import serial.tools.list_ports
		comport=[comport.device for comport in serial.tools.list_ports.comports()]
		if comport:
			my_port=comport[0]
	
	except:
		print("Error: fn_serial_port_list")
	
	return my_port


print(fn_serial_port_list())