class AcuCode():
	def acu_fan(self):
		if self.vDisableUnitControl.value == 0:
			lvFanCall = 0
			lvSafetyTripped = 0
			if self.vUnitFanDeltatControlEnable.value == 1 and self.vScheduleStateLocal.value != 0:
				lvFanCall = 1
				print("Fan call active. Fan set to run continuously during occupied periods")

def acu_fan_def(self):
		if self.vDisableUnitControl.value == 0:
			lvFanCall = 0
			lvSafetyTripped = 0
			if self.vUnitFanDeltatControlEnable.value == 1 and self.vScheduleStateLocal.value != 0:
				lvFanCall = 1
				print("Fan call active. Fan set to run continuously during occupied periods")