file=open("Myfile.txt","w")
file.write("Hello")
file.close()
try:
    file=open("Myfile.txt","r")
    file.write("Hello....!!! This is Aishu")
    file.close()
    print("success")
except Exception as e:
    print(e)
finally:
    print("---END---")