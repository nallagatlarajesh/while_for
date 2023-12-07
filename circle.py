#write the program for compute the area and circumference of a circle using a function
def circle(r):
    area=3.14*r*r
    circumference=2*3.14*r
    return (area,circumference)
#end of fumction
radius=int(input("enter radius of circle:"))
area,circumference =circle(radius)
print("area of circle is :",area)
print("circumference of circle is :",circumference)
