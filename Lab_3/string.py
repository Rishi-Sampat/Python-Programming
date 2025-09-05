st1="ICT Department"
print(st1)

st1='ICT Department'
print(st1)

st2='3EK1'
#print(st2[4])--IndexError
print(st2[1])

st3='ICT Department'
print(st3[-4])

#slicing
st4='ICT Department'
print(st4[1:4])
print(st4[:2])
print(st4[2:])

#strings are immutable
#mes='ict department'
#mes[0]='h'
#print(mes)--type error--does not support assignment

#multiline string
mess="""
ICT
Department
3ek1
"""
print(mess)