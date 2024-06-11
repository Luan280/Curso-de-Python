from math import cos, tan, sin, radians
ang = float(input("Qual o ângulo: "))
cos = cos(radians(ang))
tan = tan(radians(ang))
sin = sin(radians(ang))
print("O Ângulo de {} tem o SENO:{:.2f}".format(ang, sin))
print("O Âgulo de {} tem o COSSENO:{:.2f}".format(ang, cos))
print("O Âgulo de {} tem a TANGENTE:{:.2f}".format(ang, tan))