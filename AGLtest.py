import requests
res=requests.get("http://agl-developer-test.azurewebsites.net/people.json")

respJ=res.json()

maleOwners = []
femaleOwners = []

for item in respJ:
    sex=item['gender']
    if item['pets']:
       for pet in item['pets']:
           if pet['type']=="Cat":
               if sex=="Male":
                  maleOwners.append(pet['name'])
               else:
                   femaleOwners.append(pet['name'])

maleOwners.sort()
femaleOwners.sort()

with open("Rajneesh_AGL_test_Output.html", "w") as my_file:
  my_file.write("<html><body><table>")
  my_file.write("<tr><td><b>Male</td></tr>")
  for mc in maleOwners:my_file.write("<tr><td>%s</td></tr>" % mc)
  my_file.write("<tr><td></td></tr>")
  my_file.write("<tr><td><b>Female</td></tr>")
  for fc in femaleOwners: my_file.write("<tr><td>%s</td></tr>" % fc)
  my_file.write("</table></body></html>")