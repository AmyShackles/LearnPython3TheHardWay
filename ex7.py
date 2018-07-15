# prints the string 'Mary had a little lamb'
print("Mary had a little lamb.")
# prints 'Its fleece was white as snow', the {} indicated replacement and 'snow' was the replacement text
print("Its fleece was white as {}.".format('snow'))
# prints 'And everywhere that Mary went'
print("And everywhere that Mary went.")
# prints 10 periods
print("." * 10)  # what'd that do?

# assigns letter 'C' to variable end1
end1 = "C"
# assigns letter 'h' to variable end2
end2 = "h"
# assigns letter 'e' to variable end3
end3 = "e"
# assigns letter 'e' to variable end4
end4 = "e"
# assigns letter 's' to variable end5
end5 = "s"
# assigns letter 'e' to variable end6
end6 = "e"
# assigns letter 'B' to variable end7
end7 = "B"
# assigns letter 'u' to variable end8
end8 = "u"
# assigns letter 'r' to variable end9
end9 = "r"
# assigns letter 'g' to variable end10
end10 = "g"
# assigns letter 'e' to variable end11
end11 = "e"
# assigns letter 'r' to variable end12
end12 = "r"

# prints end1 plus end2 plus end3 plus end4 plus end5 plus end6
# with end=' ' at the end, it prints 'Cheese Burger' to screen
# without end=' ' at the end, it prints 'Cheese\nBurger' to screen
# end is an argument of print and by default equals new line
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
# prints end7 plus end8 plus end9 plus end10 plus end11 plus end12
print(end7 + end8 + end9 + end10 + end11 + end12)
