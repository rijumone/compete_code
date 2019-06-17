# world_of_numbers.sh
#!/bin/bash

echo "Enter first integer: "
read x
echo -n "Enter second integer: "
read y

# if [[$x= ~ ^[0-9]+$ & $y= ~ ^[0-9]+$ ]];then

echo $x
echo $(x+y)
echo "x-y"
echo "x*y"
echo "x/y"

# fi