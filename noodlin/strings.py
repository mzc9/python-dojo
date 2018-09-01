#string formatting
''' String formatting lets you chain items  into a string without commas or concatenation'''
#example

prez = "Obama"
years = 2016

#print(prez + ' was the President till the year ' + years +' this is concatenation')

#print(f'{prez} was the President till  {years} this is string formatting but requires python3.6')

print('Floating point numbers: %5.2f' %(13.144))

print('This is a string with an {}'.format('insert'))
