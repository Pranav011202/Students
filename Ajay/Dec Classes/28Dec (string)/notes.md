# Strings in Java

## Introduction
* In Java , String is a class that represents a sequence of characters 
* Strings in Java are immutable , means their value cannot be changed once it is created 


## Two ways to create Strings in JAVA 

### USING STRING LITERAL (NORMAL WAY)
### USING THE NEW KEYWORD


### 1) Using String Literal 

           String s1 = "hello";
    
* When we create a string like this it is created in a string constant pool 
* String Constant pool is a special area in the memory where java stores string literals to avoid redundancy 
* If a string with the same content exist already in SCP , the variable will point to the already existing object rather than creating a new one 


### 2) Using new Keyword 

            String s2 = new String("hello")


* This explicitly creates a new object in the heap memory 
* In addition , if the string value doesn't exist in the SCP , another object is created in the SCP 


### What is the difference between Heap memory and SCP ?

1) HEAP MEMORY 
=> Heap memory is where all java objects are created using new keyword 

2) String Constant Pool 
=> It is the special Part of the heap memory 
=> It is designed to store unique string literals 
