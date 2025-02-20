
from utils.Bac import Bac
from utils.Object import Object
from algo.Dim_1 import Dim_1

bac = Bac(10)
list_obj = []
obj1 = Object(1, 2)
obj2 = Object(2, 5)
obj3 = Object(3, 4)
obj4 = Object(4, 7)
obj5 = Object(5, 1)
obj6 = Object(6, 3)
obj7 = Object(7, 8)
list_obj.append(obj1)
list_obj.append(obj2)
list_obj.append(obj3)
list_obj.append(obj4)
list_obj.append(obj5)
list_obj.append(obj6)
list_obj.append(obj7)

# # FF 
# bac = Bac(10)
# list_obj = []
# obj1 = Object(1, 9)
# obj2 = Object(2, 5)
# obj3 = Object(3, 5)
# obj4 = Object(4, 5)
# obj5 = Object(5, 5)
# list_obj.append(obj1)
# list_obj.append(obj2)
# list_obj.append(obj3)
# list_obj.append(obj4)
# list_obj.append(obj5)

# # BF
# bac = Bac(10)
# list_obj = []
# obj1 = Object(1, 6)
# obj2 = Object(2, 5)
# obj3 = Object(3, 4)
# obj4 = Object(4, 4)
# list_obj.append(obj1)
# list_obj.append(obj2)
# list_obj.append(obj3)
# list_obj.append(obj4)

# # WF
# bac = Bac(10)
# list_obj = []
# obj1 = Object(1, 8)
# obj2 = Object(2, 2)
# obj3 = Object(3, 2)
# obj4 = Object(4, 2)
# obj5 = Object(5, 2)
# list_obj.append(obj1)
# list_obj.append(obj2)
# list_obj.append(obj3)
# list_obj.append(obj4)
# list_obj.append(obj5)

dim_1 = Dim_1()
n = len(list_obj)


# nbr_bacs = dim_1.first_fit (list_obj, n, bac)
# nbr_bacs = dim_1.best_fit (list_obj, n, bac)
nbr_bacs = dim_1.worst_fit (list_obj, n, bac)
# nbr_bacs = dim_1.brute_force (list_obj, bac)

print ("nbr bacs :", nbr_bacs) 
dim_1.display_res()



