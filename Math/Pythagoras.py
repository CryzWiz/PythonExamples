from math import sqrt

print('Pyhtagoras theorem kalkulator!')
print('Sidene er a, b og c hvor c er hypotenusen')
formula = input('Hvilken side (a, b, c) leter du etter? side> ')

if formula == 'c':
    side_a = int(input('Lengden av side a: '))
    side_b = int(input('Lengden av side b: '))
    side_c = sqrt(side_a * side_a + side_b * side_b)
    print('Lengden av side c er %.2f % side_c')

elif formula == 'a':
    side_b = int(input('Lengden av side b: '))
    side_c = int(input('Lengden av side c: '))
    side_a = sqrt((side_c * side_c) - (side_b * side_b))
    print('Lengden av side a er %.2f' % side_b)

elif formula == 'b':
    side_a = int(input('Lengden av side a: '))
    side_c = int(input('Lengden av side c: '))
    side_b = sqrt(side_c * side_c - side_a * side_a)
    print('Lengden av side b er %.2f' % side_b)

else:
    print('Vennligst velg mellom a, b eller c')
