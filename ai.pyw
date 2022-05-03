print("Search Here")
se = input ("")
searches = []
searches.append(se+"*")
import webbrowser
opt = input ("Search with the web browser?Y/N")
if opt == "N":
  op = input("Run Command?Y/N")
  if op == "Y":
    import os
    os.system(se)
  else:
    import os
    os.startfile(se)
else:
  webbrowser.se()
