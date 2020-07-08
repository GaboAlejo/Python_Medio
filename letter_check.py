def split(word): 
        return [char for char in word] 
    
def letter_check(lista):
    lista2= list(dict.fromkeys(split(lista[1])))
    estado = True
    
    
    for i in lista2:
        
        if i.upper() in lista[0].upper():
            print("La letra está en la lista 1 ")
            
          
        else:
            estado = False
            break
            
        
    return estado
            
        
    
estado=letter_check(["hola","hsdfdf"])
print(estado)


 
 
