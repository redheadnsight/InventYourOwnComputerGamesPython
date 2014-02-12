def TrueFizz(message):
    print(message)
    return True

def FalseFizz(message):
    print(message)
    return False

if FalseFizz('Cats') or TrueFizz('Dogs'):
    print('Step1')

if TrueFizz('Hello') or TrueFizz('Goodbye'):
    print('Step 2')

if TrueFizz('Spam')and TrueFizz('Cheese'):
    print('Step3')

if FalseFizz('Red') and TrueFizz('Blue'):
    print('Step4')
    
