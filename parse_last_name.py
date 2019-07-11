from emailList import email_list

f = open("directories.txt","w+")
for email in email_list:
    name = email.split("@")[1]
    last_name = name.split(".")[0]
    f.write("\""+last_name.capitalize()+"\":\""+email+"\""+",\n")

f.close()
