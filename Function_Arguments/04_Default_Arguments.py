# These are the Default arguments are the arguments that are passed to a function
# when the caller does not provide a value for that argument. 
# The default value is specified in the function definition.
def School(School_name, number=3):
    print(School_name ,"is the Top", number, "in Barnala" ) 

School(School_name="KIPS", number=1)
School(number=2, School_name="DAWN")
School(School_name="Read")