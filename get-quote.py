#!/usr/bin/env python3
import random
def main():
  interested = input("Are you interested to add a Quote Y /N : ")
  print(interested)
  while interested in {'Y','y'}:
    quote_text = input("Enter the Quote: ")
    filename = "quotes.txt"
    interested = 'n'
    with open (filename, 'a') as f:
      f.write(quote_text)
      f.write("\n")
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes)
  rnd = random.randint(0,last-1)
  if rnd == 0:
     nrnd = random.randint(0,last+1)
  else:
     nrnd = random.randint(0,last-1)

  print("Here is the Quote for today")
  print(quotes[rnd])
  print(quotes[nrnd])

  print("Rnd", rnd, "NRnd", nrnd)	

if __name__== "__main__":
  main()
