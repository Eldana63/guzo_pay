STATION=[{"name":["Addisu","Asela"],"city":"Adama","Region":"Oromia"},
 {"name":["kaliti","lamberet","Awtobis tera"],"city":"Addis Ababa","Region":"Addis Ababa"},
{"name":["Bishoftu"],"city":"Bishoftu","Region":"Oromia"},
{"name":["Bahrdar"],"city":"Bahrdar","Region":"Amhara"},
{"name":["Mekele"],"city":"Mekele","Region":"Tigray"},
{"name":["Gondar"],"city":"Gondar","Region":"Amhara"},
{"name":["Jijiga"],"city":"Jijiga","Region":"Somali"},
{"name":["Harar"],"city":"Harar","Region":"Harari"},
{"name":["Dire Dawa"],"city":"Dire Dawa","Region":"Dire Dawa"},
{"name":["Awash"],"city":"Awash","Region":"Afar"},
{"name":["Dessie","Woldiya"],"city":"Dessie","Region":"Amhara"},
{"name":["Jimma","Agaro"],"city":"Jimma","Region":"Oromia"},
{"name":["Shashemene","Arsi Negele"],"city":"Shashemene","Region":"Oromia"},
{"name":["Hawassa","Wondo Genet"],"city":"Hawassa","Region":"SNNPR"}
]

print("Welcome to Ethiopin bus Terminal" )
def search_by_city(city):
   found=False
   for station in STATION:
      if city=="All":
         print(" ".join(station["name"]), station["city"],station["Region"])
         found=True
      elif city==station["city"].lower():
         print(" ".join(station["name"]))
         found=True
   if not found:
      print("nothing is found")
user=input("which city do you want? ").strip().lower()
search_by_city(user)