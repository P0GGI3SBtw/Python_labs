def f_pow(arg0, arg1):
    result = pow(arg0, arg1)
    print(result)

user_input_1 = int(input('Enter first number: '))
user_input_2 = int(input('Enter second number: '))

list_arg = [user_input_1, user_input_2]

f_pow(*list_arg)