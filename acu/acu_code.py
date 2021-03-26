class AcuCodeClass():
	def acu_fan(self):
		if self.vDisableUnitControl.value == 0:
			lvFanCall = 0
			lvSafetyTripped = 0
			if self.vUnitFanDeltatControlEnable.value == 1 and self.vScheduleStateLocal.value != 0:
				lvFanCall = 1
				print("Fan call active. Fan set to run continuously during occupied periods")

def acu_fan_def(self,print_it):
	print(f"Printing {print_it} to the screen for {self._app}{self._ref}")
	if self.vDisableUnitControl == 0:
		lvFanCall = 0
		lvSafetyTripped = 0
		if self.vUnitFanDeltatControlEnable == 1 and self.vScheduleStateLocal != 0:
			lvFanCall = 1
			print("Fan call active. Fan set to run continuously during occupied periods")
		if lvFanCall == 1:
			print(f"lvFanCall is now set to {lvFanCall}")
			self.vScheduleStateLocal = lvFanCall



def acu_fan_def2(self,print_it):
	print(f"Printing {print_it} to the screen for {self.app}{self.ref}")
	if self.iReturnTemp.value == 9999:
		lvFanCall = 0
		lvSafetyTripped = 9999
		if self.iSupplyTemp.value == 9999 and self.iSpaceTemp.value == 9999:
			lvFanCall = 1
			print("Fan call active. Fan set to run continuously during occupied periods")
		if lvFanCall == 1:
			print(f"lvFanCall is now set to {lvFanCall}")
			self.oFanEnable.value = lvFanCall



def acu_fan_def3(self,print_it):
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