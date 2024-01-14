#email extractor
import re


print("Enter your data whic h do you want to extract email from it.")
str = input()
email= re.findall(r"[a-zA-Z0-9._-]+@{1,1}+[a-z0-9._-]+.{1}", str)
for item in email:
    print(item,end="\n")




    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut in leo ut justo tincidunt aliquet nec a tellus. Proin euismod, dui et nisl. Nullam aliquam, metus sit amet convallis tristique, mauris dolor vehicula lacus, sit amet fermentum erat augue at turpis. Maecenas rhoncus elit at lorem feugiat, at fermentum sapien viverra. Aliquam erat volutpat. If you have any questions, feel free to contact us at dummy.email1@example.com, dummy.email2@example.com, dummy.email3@example.com, dummy.email4@example.com, dummy.email5@example.com, esque fringilla, velit elit hendrerit ipsum, et varius mauris neque sit amet felis. Vestibulum auctor semper massa, ac cursus ipsum vehicula vel. Nunc ornare, justo eu pretium volutpat, libero ligula tempor libero, at dummy.email6@example.com, dummy.email7@example.com, dummy.email8@example.com,ligula id ullamcorper aliquam, mauris dui dapibus ipsum, vel egestas lacus lacus a arcu. Sed vel ligula ac dui luctus sollicitudin. Nulla facilisi. Suspendisse potenti. Praesent aliquam, mauris sit amet pellentposuere velit  dummy.email9@example.com, dummy.email10@example.com, dummy.email11@example.com, dummy.email12@example.com, dummy.email13@example.com, esque fringilla, velit elit hendrerit ipsum, et varius mauris neque sit amet felis. Vestibulum auctor semper massa, ac cursus ipsum vehicula vel. Nunc ornare, justo eu pretium volutpat, libero ligula tempor libero, at dummy.email14@example.com, dummy.email15@example.com, dummy.email16@example.com,esque fringilla, velit elit hendrerit ipsum, et varius mauris neque sit amet felis. Vestibulum auctor semper massa, ac cursus ipsum vehicula vel. Nunc ornare, justo eu pretium volutpat, libero ligula tempor libero, at  dummy.email17@example.com, dummy.email18@example.com, dummy.email19@example.com, or dummy.email20@example.com.