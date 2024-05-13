def exponent(base, exp):
    x = int(base**exp)
    return x


b = int(input('Enter the base: '))
e = int(input('Enter the exponent: '))
print(b, 'raises to the power of', e, ':', exponent(b, e))
