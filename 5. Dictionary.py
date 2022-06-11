# Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
  #forced change
thisdict["year"] = 2018

  #update
thisdict.update({"color": "red"})

  #pop-delete
thisdict.pop("model")

print(thisdict)
#{'brand': 'Ford', 'year': 2018, 'color': 'red'}

print(thisdict["brand"])
#Ford

print(len(thisdict))
#3