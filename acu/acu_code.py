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







