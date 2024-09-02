#
# car = CarBlueprint()
from turtle import Turtle, Screen
from prettytable import PrettyTable
jacky = Turtle()
print(jacky)
jacky.shape("turtle")
jacky.color("aquamarine")
jacky.forward(100)

my_screen  = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = 'l'
print(table)