from math import radians, sin, cos, tan
print('------------------------------------------')
a = float(input('Digite um ângulo: '))
sen = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))
print('------------------------------------------')
print('O ângulo de {} tem o SENO de {:.2f}'.format(a, sen))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(a, cos))
print('O ângulo de {} tem a TANGENTE  de {:.2f}'.format(a, tan))
print('------------------------------------------')
