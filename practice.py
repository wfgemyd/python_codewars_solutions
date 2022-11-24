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
#______________________________________
#______________________________________
#______________________________________
#______________________________________
#______________________________________
#______________________________________
#______________________________________
#______________________________________
#______________________________________
#______________________________________
