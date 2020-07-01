# Python naming convention.
# 1- Modules (filenames) all-lowercase names, contains underscores "_"
# 2- Packages ( directories) all-lowercase without underscore.
# More info in: https://stackoverflow.com/questions/48721582/how-to-choose-proper-variable-names-for-long-names-in-python/48721872#48721872

# Python variables.

name_one = "Mario"

print(name_one)  # console.log(javascript) or puts(Ruby on Rails)

# Python variables exercises. 

# Create two variables, var1 and var2, both with the same value.


var1 = 5
var2 = 10

#template string ${} in JS or #{name} in RUBY
#The Old way of doing it: %s (s is equal to string) format specifier here to tell Python where to substitute the value of name, represented as a string.
print("This is var1 value: %s and this is var2 value: %s" % (var1, var2))

# Newer way, works on python 3 and python 2.7
var1 = 20
var2 = 40
print('This is var1 is now: {a} and var2 also changed!: {b}'.format(a=var1, b=var2))

# Create two variables, num1 and num2, which multiply together to give 16.

num1 = 8
num2 = 2
print(num1 * num2)
