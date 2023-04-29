### Ejercicios
#------------------------------------------------------------------
#Alumno: Miguel De Jesús Calderón Hernández 
#Matricula 36174268
#Materia: Informatica Aplicada 
#------------------------------------------------------------------


'''
1. Declare an empty list
2. Declare a list with more than 5 items
3. Find the length of your list
4. Get the first item, the middle item and the last item of the list
5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, manzana, IBM, Oracle and Amazon.
7. Print the list using _print()_
8. Print the number of companies in the list
9. Print the first, middle and last company
10. Print the list after modifying one of the companies
11. Add an IT company to it_companies
12. Insert an IT company in the middle of the companies list
13. Change one of the it_companies names to uppercase (IBM excluded!)
14. Join the it_companies with a string '#;&nbsp; '
15. Check if a certain company exists in the it_companies list.
16. Sort the list using sort() method
17. Reverse the list in descending order using reverse() method
18. Slice out the first 3 companies from the list
19. Slice out the last 3 companies from the list
20. Slice out the middle IT company or companies from the list
21. Remove the first IT company from the list
22. Remove the middle IT company or companies from the list
23. Remove the last IT company from the list
24. Remove all IT companies from the list
25. Destroy the IT companies list
26. Join the following lists:

    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node','Express', 'MongoDB']
'''


print("1. Declare an empty list")
Milista=list()
Milista1=[]
print("Milista=list() \n Milista1=[]")

print("2. Declare a list with more than 5 items")
Milista=["esto","es","una","lista","de 5 elementos"]
print("Milista=",Milista)

print("3. Find the length of your list")
print("len(Milista)=",len(Milista))


print("4. Get the first item, the middle item and the last item of the list")
print("First item:",Milista[0])
print("Middle item:",Milista[int(len(Milista)/2)])
print("Last Item:",Milista[int(len(Milista)-1)])


print("5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)")
Soltero=True;
mixed_data_types=["Miguel Calderon",22,1.64,Soltero,"Calle Pino Camara, Col Francisco Garcia salinas #308"]
print(mixed_data_types)

print("6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, manzana, IBM, Oracle and Amazon.")
it_companies=["Facebook","Google","Microsoft","Manzana","IBM","Oracle","Amazon"]
print(it_companies)

print("7. Print the list using _print()_")
print("print(it_companies):",it_companies)

print("8. Print the number of companies in the list")
print("print(len(it_companies)):",len(it_companies))

print("9. Print the first, middle and last company")
print("First item:",it_companies[0])
print("Middle item:",it_companies[int(len(it_companies)/2)])
print("Last Item:",it_companies[int(len(it_companies)-1)])

print("10. Print the list after modifying one of the companies")
it_companies[0]="Meta"
print("it_companies=",it_companies)







