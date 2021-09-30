name= input ('Hogy hívnak? ')
age= int (input('Hány éves vagy? '))
kg= int (input('Hány kg vagy? '))
cm= int (input('Hány cm vagy? '))
print('Szia '+name+', aki ',age,' éves', kg , 'kg',cm, 'cm magas ')
if(kg > 90):
    print ('Akkor dagadt vagy')
else:
    print ('Nem vagy Dagadt') 

if(cm < 150):
    print ('Törpe vagy')
else:
    print ('Magas vagy')       