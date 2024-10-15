immutable_var = (1,2, "apple",0)
print(immutable_var)
#immutable_var[3] = 500 #Traceback (most recent call last):
  #File "C:\projest\pythonProject9\module1_5.py", line 3, in <module>
    #immutable_var[3] = 500
   # ~~~~~~~~~~~~~^^^
#TypeError: 'tuple' object does not support item assignment
#Вывод: immuTable_var является неизменяемым кортежем, то есть невозможно изменить элементы внутри кортежа
mutable_list = 1, 2, "x", "Анастасия"
print(mutable_list)
immutable_var =(mutable_list, "София")
print(immutable_var)