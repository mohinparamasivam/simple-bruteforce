
#!/usr/bin/python3

from termcolor import colored

import time 


print("                                                                       ")
print("                                                                       ")
print ("            #################################################" )       
print ("            #                                               #" )        
print ("            #         Simple Password Bruteforce Tool       #" )        
print ("            #                                               #" )        
print ("            #                  Version 1.0                  #" )        
print ("            #                                               #" )       
print ("            #           Author : Mohin Paramasivam          #" )       
print ("            #                                               #" )
print("            #   Link : https://github.com/mohinparamasivam  #" )
print ("            #                                               #" )       
print ("            #################################################" )       

print("                                                                   ")


print("                                           ")






print("     ")

##Secret Password

word = input("Please enter your super super secret password : ")

print("  ")

#check length of word

word_length = len(word)


##Keep track of character in the password

bruteforce_counter = 0

#Completion Percentage

percentage_counter =  0

completion = ((percentage_counter/word_length)*100)


while(percentage_counter!=word_length+1):
  completion=round(((percentage_counter/word_length)*100),1)
  
  
  print("Password Cracking : " + str(completion) + " %")
  print("    ")
  percentage_counter = percentage_counter+1
  time.sleep(2)

  ##Output when cracking completed

if(percentage_counter==word_length+1):
  print("Password Cracking : " + colored('COMPLETED','green' ))
  print("  ")
  print("Password seems very easy to crack !!") 
  print("   ")


while(bruteforce_counter!=word_length) :
  

  ##Set value for all 24 alphabets

  A='A'
  B='B'
  C='C'
  D='D'
  E='E'
  F='F'
  G='G'
  H='H'
  I='I'
  J='J'
  K='K'
  L='L'
  M='M'
  N='N'
  O='O'
  P='P'
  Q='Q'
  R='R'
  S='S'
  T='T'
  U='U'
  V='V'
  W='W'
  X='X'
  Y='Y'
  Z='Z'
  a='a'
  b='b'
  c='c'
  d='d'
  e='e'
  f='f'
  g='g'
  h='h'
  i='i'
  j='j'
  k='k'
  l='l'
  m='m'
  n='n'
  o='o'
  p='p'
  q='q'
  r='r'
  s='s'
  t='t'
  u='u'
  v='v'
  w='w'
  x='x'
  y='y'
  z='z'



  ##Check for specific character in the password 

  if(word[bruteforce_counter])==A:
    print(A,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==B:
    print(B,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==C:
    print(C,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==D:
    print(D,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==E:
    print(E,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==F:
    print(F,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==G:
    print(G,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==H:
    print(H,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==I:
    print(I,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==J:
    print(J,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==K:
    print(K,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==L:
    print(L,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==M:
    print(M,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==N:
    print(N,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==O:
    print(O,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==P:
    print(P,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==Q:
    print(Q,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==R:
    print(R,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==S:
    print(S,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==T:
    print(T,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)


  elif(word[bruteforce_counter])==U:
    print(U,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)
  
  elif(word[bruteforce_counter])==V:
    print(V,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)
    
  elif(word[bruteforce_counter])==W:
    print(W,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==X:
    print(X,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)  

  elif(word[bruteforce_counter])==Y:
    print(Y,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)  

  elif(word[bruteforce_counter])==Z:
    print(Z,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)  

  elif(word[bruteforce_counter])==a:
    print(a,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)  

  elif(word[bruteforce_counter])==b:
    print(b,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)  

  elif(word[bruteforce_counter])==c:
    print(c,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==d:
    print(d,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==e:
    print(e,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==f:
    print(f,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==g:
    print(g,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==h:
    print(h,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==i:
    print(i,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==j:
    print(j,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==k:
    print(k,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==l:
    print(l,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==m:
    print(m,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==n:
    print(n,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==o:
    print(o,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==p:
    print(p,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==q:
    print(q,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==r:
    print(r,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==s:
    print(s,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==t:
    print(t,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==u:
    print(u,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==v:
    print(v,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==w:
    print(w,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==x:
    print(x,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==y:
    print(y,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

  elif(word[bruteforce_counter])==z:
    print(z,end="")
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)
  


## Prints space if there is space in password provided
  else:
    print(" ",end='')
    bruteforce_counter=bruteforce_counter+1
    time.sleep(0.2)

print("")
print("")
