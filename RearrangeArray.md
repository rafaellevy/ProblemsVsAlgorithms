I used merge sort because it has a time complexity of O(nlogn).  After the array is
sorted, the program runs through the array backwards and adds every other number to
the string variable largerNumber.  The program runs through the array backwards and skips every other element again, but this time starting at the second to last number to add each digit to the string variable smallerNumber.  This is a reliable pattern for finding the two numbers that add up the most.  

In terms of space complexity it's O(n) because you need to allocate memory for each 
element during sorting.

