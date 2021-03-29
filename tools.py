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



