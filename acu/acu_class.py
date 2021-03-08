
"""dot notation
procedural programming
dunder methods 
inheritance vs composition
inheritance is an "is a" relationship
composition is an "has a" relationship
__init__ is a constructor
The Object Super Class
dir() returns a list of all the members in the specified object
isinstance() to determin if instance is part of a class.  isinstance(AV1, VeoAppVar) returns true or false
You can access the parent class from inside a method of a child class by using super()
#print(locals()) to print all the local objects in memory
"""


"""
some research i need to do:

how to setup composition between App and Var classes

https://realpython.com/inheritance-composition-python/
"""

class App():
	def __init__(self, app_name, id, dictionary):
		self.app_name = app_name
		self.id = id
		for key, value in dictionary.items():
			#setattr(self, key, Var(value["var_name"], value["value"], value["id"]))
			setattr(self, key, Var(name=value["name"], value=value["value"], id=value["id"]))

		# DO WE WANT ATTRIBUTES IN COMPISITION CLASS OR PART OF APP CLASS
		# DO WE STORE VAR VALUE ONLY IN CLASS OR ALL ATTRIBUTES
		# WILL NEED VALUE, TIME FOR STABLE, ON/OFF TIME IN CONTROL CODE
		# COULD HAVE TWO VAR CLASSES WITH ONE OF THEM VALUE ONLY SO ACU1.SpaceTemp WORKS OR CREATE LOOKUP FOR VAR NAME
		# COULD USE ALAIS

		# need method for saving attributes to file every hour
		# need to work out how to run the control code

		# BUILD SYSTEM ON ACU TO TEST LOADING VARS, RUNNING CONTROL CODE, SAVING VALUES ...
		# THIS WILL ALLOW FOR PERFORMANCE MEASURING AND CONSEPT TESTING
		# CHECK OUT HOW TO STRUCTURE AN APPLICATION AS PART OF THIS
	def save_app(self):
		# Saves attribute values to file
		print(self.app_name)
		print(acu1.__dict__) # trying to use this to save to dict
		return acu1.__dict__



class Var():
	def __init__(self, name, value, id):
		self.name = name
		self.value = value
		self.id = id


acu_var_dict = {
"space_temp":{"id":"1", "name":"spaceTemp", "value":"74"},
"return_temp":{"id":"2", "name":"returnTemp", "value":"55"},
}

acu1 = App("acu1", 1, acu_var_dict)
#ACU2 = App("ACU2", 1, acu_var_dict)

print(acu1.space_temp.name, acu1.space_temp.value, acu1.space_temp.id)
print(acu1.return_temp.name, acu1.return_temp.value, acu1.return_temp.id)
test = acu1.save_app()
print(test)
for key, value in test.items():
	print(key, value)


print(acu1.space_temp.__dict__)
print(acu1.space_temp.__dict__["value"])
SpaceTemp=acu1.space_temp.__dict__["value"]
print(SpaceTemp)

# this shows we need var name as class.  need class generator for App class to generate var component class bassed on dict
# ACU1.SpaceTemp.value
# this can't be a inheritance with a  child class.  It's composition with a component
# ME.AV1_Object_Name.value
# ME.AV1_Description.value
# ME.AV1_Present_Value.value
# ME.AV1_Units.value
# ME.AV1_Input_Type.value
# ME.AV1_Configuration.value
# ME.AV1

# ACU1.AV1_Object_Name.value
# ACU1.AV1_Description.value
# ACU1.AV1_Present_Value.value
# ACU1.AV1_Units.value
# ACU1.AV1_Input_Type.value
# ACU1.AV1_Configuration.value
# ACU1.AV1