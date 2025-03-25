thistuple=("apple","banana","cherry")
y=list(thistuple)
y[2]="mango"
thistuple=tuple(y)
print(thistuple)