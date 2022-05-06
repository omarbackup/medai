data = open("ai.sys")
dat = data.read()
print("Resent:" + dat)
print("Search Here")
se = input ("")
searches = []
searches.append(se+"*"+dat)
with open ("ai.sys", "w")as f:
  f.writelines(searches)
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
"""/*
 *
 *
 *
 *   Copyright (c) Tobey_Source
 *              5/6/2022 11:09 PM
 */"""
