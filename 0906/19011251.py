#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:

# Nombre: Omar Israel Navarro Oliva
# No. Control: 19011251
# Calificación: XXX

# Operadores a nivel e bits (bitwise)

x = 22

print ("x = {: >6b}". format ( x ) )
print ("x & 4 = {: >3d} = {: >6b}". format ( x & 4 , x & 4) )
print ("x | 1 = {: >3d} = {: >6b}". format ( x | 1 , x | 1) )
print ("x ^ 4 = {: >3d} = {: >6b}". format ( x ^ 4 , x ^ 4) )
print ("~x = {: >3d} = {: >6b}". format (~ x , ~ x ) )
print ("x << 1 = {: >3d} = {: >6b}". format ( x << 1 , x << 1) )
print ("x >> 2 = {: >3d} = {: >6b}". format ( x >> 2 , x >> 2) )