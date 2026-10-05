
# print a to z alphabets 

# 1)       
#             *              
#          *     *           
#       *  *  *  *  *        
#    *                 *     
# *                       *  


for i in range(1,6,1):
    for j in range(1,10,1):
        if(i==1 and(j==5)or (i==2 and(j==4 or j==6)) or (i==3 and (j==3 or j==4 or j==5 or j==6 or j==7)) or (i==4 and (j==2 or j==8)) or (i==5 and (j==1 or j==9))):
            print("*"," ",end="")
        else:
            print(" "," ",end="")
    print()


# optimized

# for i in range(1,6,1):
#     for j in range(1,10,1):
#         if(i+j==6 or j-i==4 or (i==3 and (j==3 or j==4 or j==5 or j==6 or j==7))):
#             print("*"," ",end="")
#         else:
#             print(" "," ",end="")
#     print()

#==========================================================

# 2)
#   *  *  *     
#   *        *  
#   *  *  *     
#   *        *  
#   *  *  *    

for i in range (1,6,1):
    for j in range(1,7,1):
        if(j==3 or (i==1 and(j>=3 and j<=5)) or (i==2 and j==6) or (i==3 and(j>=3 and j<=5)) or (i==4 and j==6) or (i==5 and(j>=3 and j<=5)) ):
            print("*", " ",end="")
        else:
            print(" "," ",end="")
    print()


# =======================================================================
print("                                                                                 ")


# 3)
#       *  *  *        
#    *                 
# *                    
# *                    
# *                    
#    *                 
#       *  *  *        

for i in range(1, 8):
    for j in range(1, 8):
        if ((i == 1 and j >= 3 and j <= 5) or (i == 2 and j == 2) or (i == 3 and j == 1) or (i == 4 and j == 1) or (i == 5 and j == 1) or (i == 6 and j == 2) or (i == 7 and j >= 3 and j <= 5)):
            print("*", end="  ")
        else:
            print(" ", end="  ")
    print()

# ==========================================================================
print("                                                                                 ")

# 4)
#    *  *  *           
#    *        *        
#    *           *     
#    *           *     
#    *           *     
#    *        *        
#    *  *  *  

for i in range (1,8,1):
    for j in range(1,8,1):
        if(j==2 or (i==1 and (j>=3 and j<=4))or (i==7 and (j>=3 and j<=4)) or (i==2 and (j==5)) or (i==6 and (j==5)) or (i==3 and (j==6))or (i==4 and (j==6)) or (i==5 and (j==6))):
            print("*"," ",end="")
        else:
            print(" "," ",end="")
    print()

# ============================================================================
print("                                                                                 ")

# 5)
# *  *  *  *  *  
# *              
# *              
# *  *  *  *  *  
# *              
# *              
# # *  *  *  *  *  

for i in range(1,8,1):
    for j in range(1,6,1):
        if(j==1 or i==1 or i==4 or i==7):
            print("*"," ",end="")
        else:
            print(" "," ",end="")
    print()

# ===================================================================================
print("                                                                                 ")

# 6)

# *  *  *  *  *  
# *              
# *              
# *  *  *  *  *  
# *              
# *              
# *    

for i in range(1,8,1):
    for j in range(1,6,1):
        if(j==1 or i==1 or i==4 ):
            print("*"," ",end="")
        else:
            print(" "," ",end="")
    print()

# ==============================================================
print("                                                ")
# # 7)
#       *  *  *        
#    *                 
# *                    
# *     *  *  *  *  *  
# *           *     *  
#    *        *     *  
#       *  *        *  

for i in range(1, 8):
    for j in range(1, 8):
        if ((i == 1 and j >= 3 and j <= 5) or (i == 2 and j == 2) or (i == 3 and (j == 1 )) or (i == 4 and (j == 1 or j>=3)) or (i == 5 and (j == 1 or j==5)) or (i == 6 and (j == 2 or j==5)) or (i == 7 and j >= 3 and j <= 4) or (j==7 and (i>=4))):
            print("*", end="  ")
        else:
            print(" ", end="  ")
    print()


# ====================================================================================
# 8)
                                                    
#    *        *     
#    *        *     
#    *  *  *  *     
#    *        *     
#    *        *    


for i in range(1,6,1):
    for j in range(1,7,1):
        if(j==2 or j==5 or i==3 and (j>=2 and j<=5)):
            print("*"," ",end="")
        else:
            print(" "," ",end="")
    print()

# =======================================================================================
print("                                                   ")
# 9)

# *  *  *  *  *  
#       *        
#       *        
#       *        
# *  *  *  *  *  

for i in range(1,6,1):
    for j in range(1,6,1):
        if(i==1 or i==5 or j==3):
            print("*"," ",end="")
        else:
            print(" "," ",end="")
    print()

# =======================================================================================
print("                                                   ")
# 10)  
#                                          
# *  *  *  *  *  
#       *        
#       *        
#       *        
#    *  *        
#    *  * 

for i in range(1,8,1):
    for j in range(1,6,1):
        if(i==1 or (j==3 and (i<=5)) or  (i==6 and (j>=2 and j<=3)) or (i==5 and  j==2)):
            print("*"," ",end="")
        else:
            print(" "," ",end="")
    print()

# =======================================================================================
print("                                                   ")
# 11)
#
# *           *           
# *        *              
# *     *                 
# *  *                    
# *                       
# *  *                    
# *     *                 
# *        *              
# *           *           

for i in range(1,10,1):
    for j in range(1,9,1):
        if(j==1 or (i <= 5 and i + j == 6)  or (i >= 5 and i - j == 4)):
            print("*"," ",end="")
        else:
            print(" "," ",end="")
    print()

# =======================================================================================
print("                                                   ")

# 12)
# *              
# *              
# *              
# *              
# *              
# *  *  *  *  *  

for i in range (1,7,1):
    for j in range(1,6,1):
        if(j==1 or i==6):
            print("*"," ",end="")
        else:
            print(" "," ",end="")
    print()    

# =======================================================================================
print("                                                   ")

# 13)

# *                 *  
# *  *           *  *  
# *     *     *     *  
# *        *        *  
# *                 *  
# *                 *  
# *                 *  

for i in range(1,8,1):
    for j in range(1,8,1):
        if(j==1 or j==7 or (j<=4 and  i==j ) or (j>=4 and i+j==8)):
            print("*"," ",end="")
        else:
            print(" "," ",end="")
    print()

# =======================================================================================
print("                              ")

# 14)

# *                 *  
# *  *              *  
# *     *           *  
# *        *        *  
# *           *     *  
# *              *  *  
# *                 *  

for i in range(1,8,1):
    for j in range(1,8,1):
        if(j==1 or j==7 or (j<=7 and  i==j )  ):
            print("*"," ",end="")
        else:
            print(" "," ",end="")
    print()

# =======================================================================================
print("                              ")

# 15)

#       *  *  *  *  *        
#    *                 *     
#    *                 *     
#    *                 *     
#    *                 *     
#       *  *  *  *  *     

for i in range(1, 8):
    for j in range(1, 10):
        if ((i == 1 and (j >= 3 and j <= 7)) or(i == 2 and (j == 2 or j == 8)) or(i == 3 and (j == 2 or j == 8)) or(i == 4 and (j == 2 or j == 8)) or(i == 5 and (j == 2 or j == 8))   or(i == 6 and (j >= 3 and j <= 7))):
                print("*"," ", end="")
        else:
            print(" "," ", end="")
    print()

# =======================================================================================
print("                              ")

# 16)

# *  *  *  *           
# *           *        
# *           *        
# *  *  *  *           
# *                    
# *                    
# *         

for i in range(1,8,1):
    for j in range(1,8,1):
        if(j==1 or (i==1 and (j<=4)) or (i==2 and j==5) or (i==3 and j==5) or (i==4 and (j<=4))  ):
            print("*"," ",end="")
        else:
            print(" "," ",end="")
    print()


# =======================================================================================
print("                              ")

# 17)

#       *  *  *  *  *     
#    *                 *  
#    *                 *  
#    *        *        *  
#    *           *     *  
#       *  *  *  *  *     
#                      *  

for i in range(1, 9):
    for j in range(1, 9):
        if ((i == 1 and (j >= 3 and j <= 7)) or(i == 2 and (j == 2 or j == 8)) or(i == 3 and (j == 2 or j == 8)) or(i == 4 and (j == 2 or j == 8)) or(i == 5 and (j == 2 or j == 8))   or(i == 6 and (j >= 3 and j <= 7)) or (i>=4 and j-i==1 )):
                print("*"," ", end="")
        else:
            print(" "," ", end="")
    print()

# =======================================================================================
print("                              ")

# 18)
# *  *  *  *           
# *           *        
# *           *        
# *  *  *  *           
# *  *                 
# *     *              
# *        *     

for i in range(1,8,1):
    for j in range(1,8,1):
        if(j==1 or (i==1 and (j<=4)) or (i==2 and j==5) or (i==3 and j==5) or (i==4 and (j<=4))   or (i-j==3)):
            print("*"," ",end="")
        else:
            print(" "," ",end="")
    print()

# =======================================================================================
print("                              ")

# # 19)
#       *  *  *        
#    *           *     
#    *                 
#       *  *  *        
#                *     
#    *           *     
#       *  *  *      

for i in range(1,8,1):
    for j in range(1,8,1):
        if((i==1 and (j>=3 and j<=5)) or (i==2 and (j==2 or j==6)) or (i==3 and (j==2)) or (i==4 and(j>=3 and j<=5)) or (i==5 and (j==6) or (i==6 and (j==2 or j==6))) or (i==7 and (j>=3 and j<=5)) ):
            print("s"," ",end="")
        else:
            print(" "," ",end="")    
    print()

# =======================================================================================
print("                              ")

# 20)
# *  *  *  *  *  
#       *        
#       *        
#       *        
#       *  

for i in range(1,6,1):
    for j in range(1,6,1):
        if(i==1 or j==3):
            print("*"," ",end="")
        else:
            print(" "," ",end="")
    print()

# =======================================================================================
print("                              ")

# 21)

# *           *  
# *           *  
# *           *  
# *           *  
# *           *  
#    *  *  *     

for i in range (1,8,1):
    for j in range(1,6,1):
        if((j==1 and i<=5) or (j==5 and i<=5) or (i==6 and(j==2 or j==3 or j==4)) ):
            print("*"," ",end="")
        else:
            print(" "," ",end="")
    print()

# =======================================================================================
print("                              ")

# 22)

# *       *
# *       *
# *       *
#   *   *
#     *     

for i in range(1,6,1):
    for j in range(1,6,1):
        if j==5 and i<=3 or j==1 and i<=3 or i==4 and j>3 and j<5 or i-j==2:
            print("*",end=" ")
        else:
            print(" ",end=" ")    
    print()

# =======================================================================================
print("                              ")

# 23)
# =======================================================================================

# *       * 
# *       * 
# *   *   * 
# * *   * * 
# *       * 

for i in range(1,6,1):
    for j in range(1,6,1):
        if j==1 or j==5 or i==j and i>=3 or i+j==6 and i>=3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() 


# =======================================================================================
print("                              ")

# 24)
# *       * 
#   *   *   
#     *     
#   *   *   
# *       * 

for i in range(1,6,1):
    for j in range(1,6,1):
        if i==j or j==6-i:
            print("*",end=" ")
        else:
            print(" ",end=" ")    
    print()

# =======================================================================================
print("                              ")

# 25)
# *           *
#   *       *
#     *   *
#       *
#       *
#       *
#       *       


for i in range(1,8,1):
    for j in range(1,8,1):
        if i==j and j<=4 or j==8-i and j>=4 or j==4 and i>=4:   
            print("*",end=" ")
        else:
            print(" ",end=" ")    
    print()



# =======================================================================================
print("                              ")

# 26)
# * * * * * 
#       *   
#     *     
#   *       
# * * * * * 

for i in range(1,6,1):
    for j in range(1,6,1):
        if i==1 or i==5 or j==6-i:
            print("*",end=" ")
        else:
            print(" ",end=" ")    
    print()