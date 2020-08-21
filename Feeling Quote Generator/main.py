import random
import Quotes

def feeling(feeling_type,emoji):
    print(f' {feeling_type} {emoji}')

print(' ')
print('Want a quote to match how you are feeling or how you want to feel?')
print('Pick a feeling from the list and type how you are feeling or how you want to feel next to the prompt that says "Type to get some inspiration".')
print(' ')

print ('______________')
print(' ')
feeling('Happy', '😀')
feeling('Sad', '😭')
feeling('Angry', '🤬')
feeling('Loving', '😘')
feeling('Crazy', '🤪')
feeling('Confused', '🤔')
feeling('Unloved', '😞')
feeling('Mischeveous', '😈')
feeling('Successful', '🤩')
print ('______________')
print(' ')
response = input('Type to get some inspiration: ')

if str.casefold(response) == 'happy':
    print(' ')
    print(random.choice(Quotes.Happy_list))
    print(' ')
elif str.casefold(response) == 'sad':
    print(' ')
    print(random.choice(Quotes.Sad_list))
    print(' ')
elif str.casefold(response) == 'angry':
    print(' ')
    print(random.choice(Quotes.Angry_list))
    print(' ')
elif str.casefold(response) == 'loving':
    print(' ')
    print(random.choice(Quotes.Loving_list))
    print(' ')
elif str.casefold(response) == 'crazy':
    print(' ')
    print(random.choice(Quotes.Crazy_list))
    print(' ')
elif str.casefold(response) == 'confused':
    print(' ')
    print(random.choice(Quotes.Confused_list))
    print(' ')
elif str.casefold(response) == 'unloved':
    print(' ')
    print(random.choice(Quotes.Unloved_list))
    print(' ')
elif str.casefold(response) == 'mischeveous':
    print(' ')
    print(random.choice(Quotes.Mischeveous_list))
    print(' ')
elif str.casefold(response) == 'successful':
    print(' ')
    print(random.choice(Quotes.Successful_list))
    print(' ')
else:
    print(' ')
    print(f'"{response}" is not a valid response. Type just one word from the list, e.g. "happy".')
    print(' ')