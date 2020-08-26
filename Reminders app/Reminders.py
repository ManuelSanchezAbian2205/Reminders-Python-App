def Espanol ():
    def writeremind ():
        newreminder = input ("Nuevo recordatorio: ")
        f = open ("reminders.txt", "a")
        newreminder1 = ("-" + newreminder + "\n")
        print ("Recordatorio creado con éxito!!\n")
        f.write (newreminder1)
        f.close()
    def seeremind ():
        f = open ("reminders.txt")
        remindersapp = f.read()
        print (remindersapp)
        f.close()
    def deleteremind ():
        confirm = input ("Estas seguro? Se eliminarán TODOS los recordatorios [s/n] : ")
        if confirm == "s":
            print ("Recordatorios borrado con éxito!!")
            f = open ("reminders.txt","w")
            f.write ("\n")
            f.close
        else:
            input ("Pulsa cualquier tecla para ir al menú")
    def menu ():
        i=0
        while i == 0:
            print ("1. Escribir un recordatorio\n2.Ver los recordatorios\n3. Borrar TODO\n4.Salir")
            opc = int(input("Opcion a seleccionar: "))
            if opc == 1 :
                writeremind()
            elif opc == 2 :
                seeremind()
            elif opc == 3 :
                deleteremind()
            elif opc == 4 :
                i=1
    menu()

def English ():
    def writeremind ():
        newreminder = input ("New reminder: ")
        f = open ("reminders.txt", "a")
        newreminder1 = ("-" + newreminder + "\n")
        print ("Reminder created succesfully!!!\n")
        f.write (newreminder1)
        f.close()
    def seeremind ():
        f = open ("reminders.txt")
        remindersapp = f.read()
        print (remindersapp)
        f.close()
    def deleteremind ():
        confirm = input ("Are you sure? All data and all reminders will be erased [y/n] : ")
        if confirm == "y":
            print ("Reminders deleted succesfully!!")
            f = open ("reminders.txt","w")
            f.write ("\n")
            f.close
        else:
            input ("Tap ENTER to go home")
    def menu ():
        i=0
        while i == 0:
            print ("1. Write a reminder\n2. See all reminders\n3. Erase everything\n4. Exit")
            opc = int(input("Select an option: "))
            if opc == 1 :
                writeremind()
            elif opc == 2 :
                seeremind()
            elif opc == 3 :
                deleteremind()
            elif opc == 4 :
                i=1
    menu()

abc = 0
while abc == 0:

    print("Select a language")
    print ("""    1. Español
    2. English
    3. Français (non disponible)""")
    selopc = input ("Select: ")
    if selopc  == "1":
        abc = 1
        Espanol()
    elif selopc == "2":
        abc = 1
        English()
    elif selopc == "3":
        abc = 1
    elif selopc == "help":
        input ("Copyright Manuel Sanchez")
        input ("Ver. 1.0")
        input ("Thanks for using Reminders App")
        input ("Coded with python")
