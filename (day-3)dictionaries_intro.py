student={
   "name":"riya",
   "age":"23",
   "hobby":"singing"
}
print(student["name"]) #accessing values

information=dict(name="rohan", age="25") #using keyword dict
print(information)

#adding a val
student["age"]=26
student["grade"]=78
print(student["age"])

#removing
a=student.pop("hobby")
print(a)

print(student.keys())
print(information.values())
print(student.items()) #tuple format of key:val
print(student.update(information)) #merging 2 diff dics

