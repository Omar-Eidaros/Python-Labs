
Text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry." \
       " Lorem Ipsum has been the industry's standard dummy text ever since the 1500s," \
       " when an unknown printer took a galley of type and scrambled it to make a type specimen book." \
       " It has survived not only five centuries, but also the leap into electronic typesetting," \
       " remaining essentially unchanged. It was popularised in the 1960s with the release of" \
       " Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software" \
       " like Aldus PageMaker including versions of Lorem Ipsum."
a = Text.count("a")
e = Text.count("e")
i = Text.count("i")
o = Text.count("o")
u = Text.count("u")

listnames = ["Count A","Count E","Count I","Count O","Count U"]
listvalues = [a,e,i,o,u]

for i in range(len(listnames)):
      print(f"{listnames[i]} ={listvalues[i]}")


