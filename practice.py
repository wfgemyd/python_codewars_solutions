def find_even_index(arr):
  for i in range(len(arr)):
    if sum(arr[:i])==sum(arr[i+1:]):
      print(arr.index(i))
      return arr.index(i)
  return -1
find_even_index([1,2,3,4,3,2,1])
#______________________________________
def narcissistic( value ):
  lst = list(str(value))
  res = 0
  for i in lst:
    res+=int(i)**len(lst)
  return res==value
#_____________________________________
def unique_in_order(iterable):
  lst = list(iterable)
  res = []
  for i in range(len(lst)):
    if i == 0:
      res.append(lst[i])
    elif lst[i] != lst[i-1]:
      res.append(lst[i])
  return res
unique_in_order('AAAABBBCCDAABBB')
#______________________________________
def pyramid(n):
  for i in range(1,n+1):
    print(' '*(n-i)+'*'*i+'*'*(i-1))
  return None
#______________________________________
import string
def to_camel_case(text):
  alph = string.ascii_letters
  lst = list(text)
  if text=='':
    return ''
  for i in lst:
    if i not in alph:
      lst[lst.index(i)+1]=lst[lst.index(i)+1].upper()
      del(lst[lst.index(i)])
  
  print(''.join(lst))  
  return ''.join(lst)
  
to_camel_case("A-B-C")
#______________________________________
def order(sentence):
  res=''
  lst = sentence.split()
  num_lst=[None]*len(lst)
  for word in lst:
    for letter in word:
      try:
        num_lst[int(letter)-1] = word
      except:
        pass
       
  return ' '.join(num_lst)    


order("4of Fo1r pe6ople g3ood th5e the2")
#______________________________________
def persistence(n):
  num = n
  counter = 0
  lst=[]
  lens = len(str(n))
  if lens ==1:
    return counter
  while len(str(num))!=1:
    lst=list(str(num))
    num = 1
    for i in lst:
      num*=int(i)
    counter+=1
  print(counter)
  return counter

persistence(39)
#______________________________________
import string
def alphabet_position(text):
  text = text.lower()
  alph = string.ascii_lowercase
  res = ''
  for i in text:
    if i in alph:
      res = res + str(alph.index(i)+1) + " "
  print(res)
  return res[0:-1]  
  
alphabet_position("The sunset sets at twelve o' clock.")
#______________________________________
def anagrams(word, words):
  anagram = []
  copy_word = list(word)
  for i in words:
    for letter in list(i):
      if letter in copy_word:
        copy_word.remove(letter)
      else:
        break
      if len(copy_word)==0:
        anagram.append(i)
    copy_word = list(word)
  print(anagram)
  return anagram
anagrams('abba', ['abbab', 'abbaa', 'babaa'])
#______________________________________

def next_bigger(n):
  if len(str(n))>1:
    original_num = n
    lst = sorted(list(str(n)))
    temp = ''
    for i in range(1,len(str(n))):
      #new_num = int(str(n)[:-i-1]+str(n)[-i]+str(n)[-i-1])
      lst[-i],lst[-i-1] = lst[-i-1],lst[-i] 
      for x in lst:
        temp+=x
      if  original_num<int(temp):
        print(temp)
        return temp
      temp = ''
    return -1
  return -1

next_bigger(76453144957786)
#______________________________________


def duplicate_encode(word):
    lst = list(word.lower())
    encoded = ''
    for i in lst:
      if lst.count(i) > 1:
        encoded += ")"
      else:
        encoded += "("
    print(encoded)
    return encoded


duplicate_encode("recede")
#______________________________________


def increment_string(strng):
  lst = list(strng)
  num_str, num_str_p_1, the_word, zeros = '','','',''
  indx = 0
  f = True
  for num in lst[::-1]:
    if ord(num) > 48 and ord(num) < 58 and f:
      num_str+=num
    elif ord(num) == 48 and f:
      zeros+=num
    else:
      f = False
      the_word += num

  the_word = the_word[::-1]
  num_str = num_str[::-1]
  if num_str != '':
    num_str_p_1 = str(int(num_str)+1)

  if len(num_str_p_1) > len(num_str):
    zeros = zeros[0:len(zeros)-1]
    print(zeros)

  if num_str == '':
    if zeros == '':
      print(the_word+num_str+'1')
      return the_word+zeros+num_str+'1'
    else:
      print(the_word+zeros[:len(zeros)-1]+num_str+'1')
      return the_word+zeros[:len(zeros)-1]+num_str+'1'
  else:
    print(the_word+zeros+num_str_p_1)
    return the_word+zeros+num_str_p_1


increment_string("foobar00")
#______________________________________
import math
from statistics import mean
def solution(array_a, array_b):
    lst,sum = [],0
    for i in range(len(array_a)):
        i = abs(i)
        if array_a[i] == array_b[i]:
            lst.append(0)
        else:
            lst.append(abs((array_a[i])-(array_b[i]))**2)
            print(lst)
    print(mean(lst))
    return mean(lst)


a1 = [1,2,3]
a2 = [4,5,6]
solution(a1, a2)
#______________________________________
def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1
    
find_even_index([20,10,30,10,10,15,35])
#______________________________________
import random
def guess():
    a = 5
    b = int(input("Enter a number: "))
    while a != b:
        if b < a:
            print("too low")
            b = int(input("try again: "))
        elif b > a:
            print("too high")
            b = int(input("try again: "))
        else:
            break
    print("you won")
    replay = input("Do you want to play again: (yes,Yes,y/no,No,n): ")
    if replay == "yes" or replay == "Yes" or replay == "y":
        result == 0
    else:
        print("bye bye")
        result = result+1
          
guess()
#______________________________________
def rect_with_hole(rows,cols,symb):
    lst=[]
    belly = []
    lst.append(f"{symb}"*rows)
    lst.append(" "*rows)
    belly = symb+lst[1][1:-1]+symb
   
    for row in range(1,2):
        #print("# "*cols)
        for col in range(1,cols+1):
            if col == row or col == cols:
                print(lst[0])
            else:
                print(belly)
        
rect_with_hole(8, 3,"#") 
#______________________________________
def pira(n):
    n=n+1
    for y in range(n,0,-1):
        print(" "*(y-1)+"# "*(n-y)) 

pira(7)
#______________________________________
def find_t(lst_of_t):
    bigger = [0,'']
    for i in lst_of_t:
        if bigger[0] < (i[1]*i[2])/2:
            bigger[0] = (i[1]*i[2])/2
            bigger[1] = i[0]
    print(bigger[1])
    return bigger[1]
            
rectangles = [('red', 23400, 12484), ('green', 1567, 873), ('blue', 928, 876)]   
find_t(rectangles)
#______________________________________
def bigger(num):
    lst = num.split(' ')
    if int(lst[0])>int(lst[1]):
        print(lst[0])
        return lst[0]
    print(lst[1])
    return lst[1]

bigger('177 32') 
#______________________________________
def snail(array):
    results = []
    while len(array) > 0:
        # go right
        results += array[0]
        del array[0]

        if len(array) > 0:
            # go down
            for i in array:
                results += [i[-1]]
                del i[-1]

            # go left
            if array[-1]:
                results += array[-1][::-1]
                del array[-1]

            # go top
            for i in reversed(array):
                results += [i[0]]
                del i[0]

    return results

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array)
#______________________________________
def rot13(message):
    encrypt = ''
    for i in list(message):
        if 123>ord(i)>96:
            if ord(i)+13 > 122:
                encrypt = encrypt + chr((ord(i)+13) - 26)
            else:
                encrypt = encrypt + chr((ord(i)+13))
        elif 91>ord(i)>64:
            if ord(i)+13 > 90:
                encrypt = encrypt + chr((ord(i)+13) - 26) 
            else:
                encrypt = encrypt + chr((ord(i)+13))
        else:
            encrypt = encrypt + i
    print(encrypt)        
    return encrypt
        
rot13('aA bB zZ 1234 *!?%')
#______________________________________
def zeros(n):
    fac = 1
    counter = 0
    biggest = 0
    while n != 0:
        fac = n * fac
        n-=1

    for i in str(fac):
        if int(i) == 0:
            counter +=1
        else:
            if counter >= biggest:
                biggest = counter
                counter = 0
            else:
                counter = 0 

    if counter > biggest:
        biggest = counter
        counter = 0

    print (biggest)
    return biggest

zeros(1000)
#______________________________________
def make_readable(seconds):
    if seconds > 359999 or seconds < 0:
        return False
    else:
        hours = seconds // 3600 % 24
        minutes = seconds // 60 % 60
        seconds = seconds % 60
        time = [str(hours), str(minutes), str(seconds)]

        for i in time:
            if iftwodigit(i) == 1:
                time[time.index(i)] = '0' + time[time.index(i)]

        return f'{time[0]}:{time[1]}:{time[2]}'

 
def iftwodigit(num):
    print (len(str(num)))
    return len(str(num))

make_readable(3542)
#______________________________________
def valid_parentheses(string):
    lst_ = list(string)
    lst_temp = []
    if ('(' in lst_ and ')' in lst_) or string == '':
        if string =='':
            return True
        elif lst_.index(')') < lst_.index('('):
            print('false!!!!')
            return False

        for item in string:
            try:
                if item == '(':
                    lst_temp.append(item)
            
                elif item ==')':
                    lst_temp.pop()
            except IndexError:
                return False
        if '(' not in lst_temp:
            return True
        else:
            return False
    else:
        return False           

valid_parentheses("s(h()r)k(")
#______________________________________
def rgb(r, g, b):
    rgb_lst = [r,g,b]
    hex_ = ''
    ecumulator = 0
    for num in rgb_lst:
        if num > 255:
            rgb_lst[rgb_lst.index(num)] = 255
        elif num < 0:
            rgb_lst[rgb_lst.index(num)] = 0
    


    for num in rgb_lst:
        num = num / 16
        ecumulator = list(math.modf(num))[0] * 16

        hex_ = hex_ + str(dectohex(int(num)))
        hex_ = hex_ + str(dectohex(int(ecumulator)))
    print(hex_)
    return hex_

rgb(255,-255,255)
#______________________________________
class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.bal = balance

    def owner(self):
        return self.owner

    def balance(self):
        return self.bal

    def deposit(self, add_money):
        print("Deposit Accepted")
        self.bal = self.bal + add_money

    def withdraw(self, sub_money):
        withdraw_temp = self.bal - sub_money
        if not withdraw_temp < 0:
            self.bal = withdraw_temp
            print("Withdrawal Accepted")
            return withdraw_temp
        else:
            print("Funds Unavailable!")
    
    def __str__(self):
        return "Account owner:{}\nAccount balance:{} ".format(self.owner,self.bal)

acct1 = Account('Jose',100)
print(acct1.withdraw(101))
#______________________________________
class Line:
    
    def __init__(self,coor1,coor2):
        print("New coor is assianed")
        self.x1= coor1[0]
        self.x2= coor2[0]
        self.y1= coor1[1]
        self.y2= coor2[1]

        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        return math.dist(self.coor1,self.coor2)
    
    def slope(self):
        return (self.y2-self.y1)/(self.x2-self.x1)

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print(li.distance())
print(li.slope())
#______________________________________
#______________________________________
#______________________________________


