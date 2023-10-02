def main():
  
  #set this to any double
  doubleValue =25
  
  #set this to any int
  intValue = 5
  
  #print out addition, subtraction, multiplication, and division of these two values

  print(doubleValue + intValue)
  print(doubleValue - intValue)
  print(doubleValue / intValue)
  print(doubleValue * intValue)
  
  #populate this list
  myFriends = ["bob","conor","jimmy","tofa","sissy"]
  print(myFriends[2],[3])
  #print out your friends at index 2 and index 3
  
  
  #populate this list with five numbers
  fiveNumbers = [1,3,4,5,2]
  
  #do each of the four equations with different numbers each time.
  ans1 = fiveNumbers[0] + fiveNumbers[3]
  ans2 = fiveNumbers[1] - fiveNumbers[4]
  ans3 = fiveNumbers[3] / fiveNumbers[1]
  ans4 = fiveNumbers[4] * fiveNumbers[2]
  #now replace two of the numbers in the list with a different number (using name of list[x] = ?, not rewriting the fiveNumber list)
  fiveNumbers[1] = 5
  fiveNumbers[3] = 99
  #print out the list
  print(fiveNumbers)
  
  
main()
