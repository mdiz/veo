# There will be a dict (profile) for each DGU 

dgu_var_dict = {
"iSpaceTemp":{"name":"iSpaceTemp","description":"Space Temperature","type":"Input","ref":1,"units":"F","value":9999,"register":1002,"format":"Float32","writable":"No","last_change":9999,"local_log":9999},
"iReturnTemp":{"name":"iReturnTemp","description":"Return Temperature","type":"Input","ref":2,"units":"F","value":9999,"register":1004,"format":"Float32","writable":"No","last_change":9999,"local_log":9999},
"iSupplyTemp":{"name":"iSupplyTemp","description":"Supply Temperature","type":"Input","ref":3,"units":"F","value":9999,"register":1006,"format":"Float32","writable":"No","last_change":9999,"local_log":9999},
"iSpaceTempRemote":{"name":"iSpaceTempRemote","description":"Remote Space Temperature","type":"Input","ref":4,"units":"F","value":9999,"register":1008,"format":"Float32","writable":"No","last_change":9999,"local_log":9999},
"iAI5":{"name":"iAI5","description":"Analog Input 5","type":"Input","ref":6,"units":"F","value":9999,"register":1010,"format":"Float32","writable":"No","last_change":9999,"local_log":9999},
"iAI6":{"name":"iAI6","description":"Analog Input 6","type":"Input","ref":7,"units":"F","value":9999,"register":1012,"format":"Float32","writable":"No","last_change":9999,"local_log":9999},
"iAI7":{"name":"iAI7","description":"Analog Input 7","type":"Input","ref":8,"units":"F","value":9999,"register":1014,"format":"Float32","writable":"No","last_change":9999,"local_log":9999},
"iAI8":{"name":"iAI8","description":"Analog Input 8","type":"Input","ref":9,"units":"F","value":9999,"register":1016,"format":"Float32","writable":"No","last_change":9999,"local_log":9999},
"iLightLevel":{"name":"iLightLevel","description":"Indoor Light Level","type":"Input","ref":10,"units":"%","value":9999,"register":1018,"format":"Float32","writable":"No","last_change":9999,"local_log":9999},
"oAO1":{"name":"oAO1","description":"Analog Output 1","type":"Output","ref":12,"units":"V","value":0,"register":1020,"format":"Float32","writable":"Yes","last_change":9999,"local_log":9999},
"oAO2":{"name":"oAO2","description":"Analog Output 2","type":"Output","ref":13,"units":"V","value":0,"register":1022,"format":"Float32","writable":"Yes","last_change":9999,"local_log":9999},
"oAO3":{"name":"oAO3","description":"Analog Output 3","type":"Output","ref":14,"units":"V","value":0,"register":1024,"format":"Float32","writable":"Yes","last_change":9999,"local_log":9999},
"oAO4":{"name":"oAO4","description":"Analog Output 4","type":"Output","ref":15,"units":"V","value":0,"register":1026,"format":"Float32","writable":"Yes","last_change":9999,"local_log":9999},
"vCalculatedSpaceTemp":{"name":"vCalculatedSpaceTemp","description":"Calculated Space Temperature","type":"Var","ref":21,"units":"F","value":9999,"register":1028,"format":"Float32","writable":"No","last_change":9999,"local_log":9999},
"vSpaceTempOffset":{"name":"vSpaceTempOffset","description":"Space Temperature Offset","type":"Var","ref":22,"units":"F","value":0,"register":1030,"format":"Float32","writable":"Yes","last_change":9999,"local_log":9999},
"vBackupCoolingSetpoint":{"name":"vBackupCoolingSetpoint","description":"Backup Cooling Setpoint","type":"Var","ref":31,"units":"F","value":80,"register":1032,"format":"Float32","writable":"Yes","last_change":9999,"local_log":9999},
"vBackupHeatingSetpoint":{"name":"vBackupHeatingSetpoint","description":"Backup Heating Setpoint","type":"Var","ref":32,"units":"F","value":60,"register":1034,"format":"Float32","writable":"Yes","last_change":9999,"local_log":9999},
"vBackupMaxHeatingSetpoint":{"name":"vBackupMaxHeatingSetpoint","description":"Backup Max Heating Setpoint","type":"Var","ref":33,"units":"F","value":69,"register":1036,"format":"Float32","writable":"Yes","last_change":9999,"local_log":9999},
"vBackupMinCoolingSetpoint":{"name":"vBackupMinCoolingSetpoint","description":"Backup Min Cooling Setpoint","type":"Var","ref":34,"units":"F","value":73,"register":1038,"format":"Float32","writable":"Yes","last_change":9999,"local_log":9999},
"iFanStatus":{"name":"iFanStatus","description":"Fan Status","type":"Input","ref":5,"units":"On/Off","value":9999,"register":2001,"format":"Init16","writable":"No","last_change":9999,"local_log":9999},
"iPushButton":{"name":"iPushButton","description":"Push Button","type":"Input","ref":11,"units":"On/Off","value":9999,"register":2002,"format":"Init16","writable":"No","last_change":9999,"local_log":9999},
"oFanEnable":{"name":"oFanEnable","description":"Fan Enable","type":"Output","ref":16,"units":"none","value":0,"register":2003,"format":"Init16","writable":"Yes","last_change":9999,"local_log":9999},
"oCompressor1Enable":{"name":"oCompressor1Enable","description":"Compressor 1 Enable","type":"Output","ref":17,"units":"none","value":0,"register":2004,"format":"Init16","writable":"Yes","last_change":9999,"local_log":9999},
"oCompressor2Enable":{"name":"oCompressor2Enable","description":"Compressor 2 Enable","type":"Output","ref":18,"units":"none","value":0,"register":2005,"format":"Init16","writable":"Yes","last_change":9999,"local_log":9999},
"oHeat1Enable":{"name":"oHeat1Enable","description":"Heat 1 Enable","type":"Output","ref":19,"units":"none","value":9999,"register":2006,"format":"Init16","writable":"Yes","last_change":0,"local_log":9999},
"oHeat2Enable":{"name":"oHeat2Enable","description":"Heat 2 Enable","type":"Output","ref":20,"units":"none","value":9999,"register":2007,"format":"Init16","writable":"Yes","last_change":0,"local_log":9999},
"vUnitStagesCooling":{"name":"vUnitStagesCooling","description":"Number of Cooling Stages","type":"Var","ref":23,"units":"none","value":9999,"register":2008,"format":"Init16","writable":"No","last_change":9999,"local_log":9999},
"vUnitStagesHeating":{"name":"vUnitStagesHeating","description":"Number of Heating Stages. Includes compressors as stage 1 and electric heat as stage 2 when unit is heat pump. ","type":"Var","ref":24,"units":"none","value":9999,"register":2009,"format":"Init16","writable":"No","last_change":9999,"local_log":9999},
"vUnitIsHeatPump":{"name":"vUnitIsHeatPump","description":"Unit is a Heat Pump - Only used by XVS and unit alarms to indicate that unit is a heat pump.  This var does not enable the heat pump sequence.  It only allows XVS to select the proper graphic and unit alarms. ","type":"Var","ref":25,"units":"none","value":9999,"register":2010,"format":"Init16","writable":"No","last_change":9999,"local_log":9999},
"vEnableHeatPumpControl":{"name":"vEnableHeatPumpControl","description":"Enable Heat Pump Control Sequence - Used with vUnitReversingValveHeatingOff to enable heat pump control sequence.  Only enable if reversing valve is controlled directly by EMS.","type":"Var","ref":26,"units":"none","value":9999,"register":2011,"format":"Init16","writable":"Yes","last_change":9999,"local_log":9999},
"vUnitGasHeat":{"name":"vUnitGasHeat","description":"Gas Heat Unit - Unit has gas heat","type":"Var","ref":27,"units":"none","value":9999,"register":2012,"format":"Init16","writable":"No","last_change":9999,"local_log":9999},
"vUnitEconomizer":{"name":"vUnitEconomizer","description":"Unit Has Econimizer - 1=Has Economizer, 0=Does Not Have Economizer","type":"Var","ref":28,"units":"none","value":9999,"register":2013,"format":"Init16","writable":"No","last_change":9999,"local_log":9999},
"vUnitDehumidification":{"name":"vUnitDehumidification","description":"Unit is equipped with dehumidification control - Only used to allow XVS to select the proper graphic and unit alarms. ","type":"Var","ref":29,"units":"none","value":9999,"register":2014,"format":"Init16","writable":"No","last_change":9999,"local_log":9999},
"vEnableRemoteSpaceTemp":{"name":"vEnableRemoteSpaceTemp","description":"Remote Space Temp Used","type":"Var","ref":30,"units":"none","value":0,"register":2015,"format":"Init16","writable":"Yes","last_change":9999,"local_log":9999},
"vEnableBackupControl":{"name":"vEnableBackupControl","description":"Enable Backup Control","type":"Var","ref":35,"units":"none","value":1,"register":2016,"format":"Init16","writable":"Yes","last_change":9999,"local_log":9999},
"vForceBackupControl":{"name":"vForceBackupControl","description":"Force Backup Control","type":"Var","ref":36,"units":"none","value":0,"register":2017,"format":"Init16","writable":"Yes","last_change":9999,"local_log":9999},
"vBackupControlActive":{"name":"vBackupControlActive","description":"Backup Control Active","type":"Var","ref":37,"units":"none","value":9999,"register":2018,"format":"Init16","writable":"No","last_change":9999,"local_log":9999},
"vUnitNumber":{"name":"vUnitNumber","description":"Unit Number","type":"Var","ref":38,"units":"none","value":9999,"register":2019,"format":"Init16","writable":"No","last_change":9999,"local_log":9999},
"vUnitType":{"name":"vUnitType","description":"Unit Type","type":"Var","ref":39,"units":"none","value":9999,"register":2020,"format":"Init16","writable":"No","last_change":9999,"local_log":9999},
"vAlarmActive":{"name":"vAlarmActive","description":"Used to set alarm active message on DGU","type":"Var","ref":40,"units":"none","value":0,"register":2021,"format":"Init16","writable":"Yes","last_change":9999,"local_log":9999},
"vTicketActive":{"name":"vTicketActive","description":"Used to set ticket active message on DGU","type":"Var","ref":41,"units":"none","value":0,"register":2022,"format":"Init16","writable":"Yes","last_change":9999,"local_log":9999},
"vSensorFail":{"name":"vSensorFail","description":"Used to set sensor fail active message on DGU","type":"Var","ref":42,"units":"none","value":0,"register":2023,"format":"Init16","writable":"Yes","last_change":9999,"local_log":9999},
"vCoolFail":{"name":"vCoolFail","description":"Used to set cool fail active message on DGU","type":"Var","ref":43,"units":"none","value":0,"register":2024,"format":"Init16","writable":"Yes","last_change":9999,"local_log":9999},
"vHeatFail":{"name":"vHeatFail","description":"Used to set heat fail active message on DGU","type":"Var","ref":44,"units":"none","value":0,"register":2025,"format":"Init16","writable":"Yes","last_change":9999,"local_log":9999},
"vDisableKeypad":{"name":"vDisableKeypad","description":"Disable Keypad","type":"Var","ref":45,"units":"none","value":0,"register":2026,"format":"Init16","writable":"Yes","last_change":9999,"local_log":9999},
"vEnableKeypadAdmin":{"name":"vEnableKeypadAdmin","description":"Enable Keypad Admin Menu","type":"Var","ref":46,"units":"none","value":1,"register":2027,"format":"Init16","writable":"Yes","last_change":9999,"local_log":9999},
"vALSC":{"name":"ALSC","description":"Keypad PIN","type":"Var","ref":47,"units":"none","value":0,"register":2028,"format":"Init16","writable":"Yes","last_change":9999,"local_log":9999},
"vCPUALSC":{"name":"CPUALSC","description":"System Assigned PIN","type":"Var","ref":48,"units":"none","value":0,"register":2029,"format":"Init16","writable":"Yes","last_change":9999,"local_log":9999},
"vLCDMessage":{"name":"vLCDMessage","description":"LCD Message","type":"Var","ref":49,"units":"none","value":0,"register":2030,"format":"Init16","writable":"Yes","last_change":9999,"local_log":9999},
"vDegUnits":{"name":"vDegUnits","description":"Temp Units, Off=Deg C, On=Deg F","type":"Var","ref":50,"units":"none","value":1,"register":2031,"format":"Init16","writable":"Yes","last_change":9999,"local_log":9999},
"vSiteID":{"name":"vSiteID","description":"Site ID","type":"Var","ref":51,"units":"none","value":1,"register":2032,"format":"Init16","writable":"Yes","last_change":9999,"local_log":9999},
"vModbusAddress":{"name":"vModbusAddress","description":"Modbus Address","type":"Var","ref":52,"units":"none","value":6,"register":2033,"format":"Init16","writable":"Yes","last_change":9999,"local_log":9999},
"vSerialNumber":{"name":"vSerialNumber","description":"Serial Number","type":"Var","ref":53,"units":"none","value":9999,"register":2034,"format":"Init16","writable":"No","last_change":9999,"local_log":9999},
"vModbusCommFail":{"name":"vModbusCommFail","description":"Modbus Communication Fail","type":"Var","ref":54,"units":"none","value":9999,"register":2035,"format":"Init16","writable":"No","last_change":9999,"local_log":9999},
"vDeviceResets":{"name":"vDeviceResets","description":"Device Resets","type":"Var","ref":55,"units":"none","value":9999,"register":2036,"format":"Init16","writable":"No","last_change":9999,"local_log":9999},
"vModbusPacketError":{"name":"vModbusPacketError","description":"Modbus Packet Error","type":"Var","ref":56,"units":"none","value":9999,"register":2037,"format":"Init16","writable":"No","last_change":9999,"local_log":9999},
"vModbusCRCError":{"name":"vModbusCRCError","description":"Modbus CRC Error","type":"Var","ref":57,"units":"none","value":9999,"register":2038,"format":"Init16","writable":"No","last_change":9999,"local_log":9999},
"vModbusLastComm":{"name":"vModbusLastComm","description":"Modbus Last Communication in Seconds","type":"Var","ref":58,"units":"none","value":9999,"register":2039,"format":"Init16","writable":"No","last_change":9999,"local_log":9999},
"vAverageCPULoopTime":{"name":"vAverageCPULoopTime","description":"Average CPU Loop Time","type":"Var","ref":59,"units":"none","value":9999,"register":2040,"format":"Init16","writable":"No","last_change":9999,"local_log":9999},
"vMaxCPULoopTime":{"name":"vMaxCPULoopTime","description":"Max CPU Loop Time","type":"Var","ref":60,"units":"none","value":9999,"register":2041,"format":"Init16","writable":"No","last_change":9999,"local_log":9999},
"vTemplateID":{"name":"vTemplateID","description":"Template ID","type":"Var","ref":61,"units":"none","value":10001,"register":6567,"format":"Init16","writable":"No","last_change":9999,"local_log":9999},
}


