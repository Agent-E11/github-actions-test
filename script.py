while True:
    print('----------------')
    num1 = input('First number: ')
    num2 = input('Second number: ')
    
    if num1 == 'q' or num2 == 'q':
        quit(0)
    
    try:
        num1, num2 = int(num1.strip()), int(num2.strip())
    except ValueError:
        quit(1)

    print('--------')
    print(f'Add: {num1 +  num2}')
    print(f'Sub: {num1 -  num2}')
    print(f'Mul: {num1 *  num2}')
    print(f'Pow: {num1 ** num2}')
