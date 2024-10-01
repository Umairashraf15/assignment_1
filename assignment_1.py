#1. Age Assignments Based on the Riddle

anton_age : int = 21
beth_age : int = anton_age + 6
chen_age : int = beth_age + 20
drew_age : int = chen_age + anton_age
ehtan_age : int = chen_age

print("Ages of Anton,Beth,Chen,Drew and Ethan:")
print(f"Anton is {anton_age} years old.")
print(f"Beth is {beth_age} years old.")
print(f"Chen is {chen_age} years old.")
print(f"Drew is {drew_age} years old.")
print(f"Ethan is {ehtan_age} years old.")


#2. Formatted String Interpolation

name : str = "Alice"
age : int = 30
city : str = "New York"

print(f"{name} is {age} years old and lives in {city}")


#3. String Manipulation

s:str = "hElLo WoRlD"

        # Capitalize the first letter
capitalized_string = s.capitalize()
print(capitalized_string)

        # Convert to uppercase
uppercase_string = s.upper()
print(uppercase_string)

        # Convert to lowercase
lowercase_string = s.lower()
print(lowercase_string)


#4. Substring Search

        # index of the substring "fox"
s_fox : str = "the quick brown fox jumps over the lazy dog"

fox_index = s_fox.find("fox")
print(f"Index of 'fox': {fox_index} ")
        # Occurence of "the"

the_occured = s_fox.count("the")
print(f"Number of occurences of 'the': {the_occured}")


#5. String Replacement

s_replace:str ="I love programming in Python"
print(s_replace)

replaced = s_replace.replace("Python", "Java")
print(replaced)


#6. String Splitting and Joining


s_fruits:str ="apple,banana,cherry,dates"

        # Splitting into a list
split_string = s_fruits.split(",")
print(split_string)

        # Joining string
Joined_string = " ".join(split_string)
print(Joined_string)


#7. String Stripping and Justifying
s_string:str ="   Python is fun!   "

        # Remove leading/trailing spaces
trimmed_string = s_string.strip()
print(trimmed_string)

        # Left justify with '*'
left_justified = trimmed_string.ljust(20, '*')
print(left_justified)

        # Left justify with '*'
right_justified = trimmed_string.rjust(20, '*')
print(right_justified)


#8. Convert an integer to its binary representation
num : int = 45

binary_representation = bin(num)
print(f"Binary representation : {binary_representation}")


#9. Calculate Powers of Numbers
base:int = 3
exponent:int = 4

Power_result = base ** exponent
print(f"Power result: {Power_result}")


#10. Round floating-point numbers
value:float = 12.34567

        #Round to the nearest integer
rounded_integer = round(value)
print(rounded_integer)

        #Round to two decimal places
rounded_two_decimals = round(value, 2)
print(rounded_two_decimals)