#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Carlos Ivan Gomez Gonzalez
# No. Control: 19012228
# Calificación: XXX
x = 22

print("x    =   {:>6b}".format(x))
print("x  &  4  =  {:>3b} = {:>6b}".format(x & 4, x &  4))
print("x  |  1  =  {:>3b} = {:>6b}".format(x | 1, x  | 1))
print("x  ^  4   =  {:>3b} = {:>6b}".format(x ^ 4, x ^ 4))
print("~x       =  {:>3b} = {:>6b}".format(~x , ~x))
print("x  <<  1  =  {:>3b} = {:>6b}".format(x << 1, x <<  1))
print("x  >>  2  =  {:>3b} = {:>6b}".format(x >> 2, x >>  2))
