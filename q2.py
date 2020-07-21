class Person(object):
	def __init__(self, first_name, last_name, father):
		self.first_name = first_name
		self.last_name = last_name
		self.father = father



def print_depth(d, start=0):
    for key, value in d.items():
        print(key, start + 1)
        if isinstance(value, dict):
            print_depth(value, start=start+1)


a = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4
        }
    }
}

print_depth(a)



person_a = Person("Arif", "Badhon", "Fayek")
person_b = Person("User", "2", person_a)


list1 = person_a.__dict__
for key in list1:
	print("{} : {}".format(key, list1[key]))

list2 = person_b.__dict__
for key in list2:
	print("{} : {}".format(key, list2[key]))