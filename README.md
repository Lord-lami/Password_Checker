# Password_Checker
# This is a command line program that uses pwned API to check if a password has been leaked
# It is insecure since you have to pass the password as an argument
# If someone has access to your command history, the passwords you checked will be leaked
# You pass the password(s) you want to chek as arguments. Like so
# python password_check.py CheckThisPassword AndThisPassword
# It will print the password and the amount of leaks the password has according to pwned API
