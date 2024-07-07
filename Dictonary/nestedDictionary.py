stud = {
    "name" : "nikhil",
    "marks" : {
        "phy" : 21,
        "chem" : 23
    }

}

print(stud["marks"]["phy"])

new_dict = {"name":"Mukku","area":"muz"} #here name is already present in stud and we have name in new_dict also and as we are updating new_dict in stud so name will be overrite in stud
stud.update(new_dict)
print(stud)