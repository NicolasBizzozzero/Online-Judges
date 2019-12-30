nothing = 16044
visits = {}
for i in range(400):
   text = urllib.request.urlopen("http: // www.pythonchallenge.com / pc / def / linkedli
st.php?nothing=" + str(nothing)).read().decode("utf8")
   visits[nothing] = text
   content = " ".join(text.split()[:-1])
   print(i, text)

   if content != "and the next nothing is":
       if content == "<font color = red > Your hands are getting tired < /font > and th
e next nothing is":
           pass
       if text == "Yes. Divide by two and keep going": 
           divide = True 
           nothing = nothing // 2 
           continue 
       else: 
           break 
   if nothing in visits.keys(): 
       print("Already visited") 
   nothing = text.split()[-1]
