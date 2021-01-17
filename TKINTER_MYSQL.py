from tkinter import *
import tkinter.messagebox as Message
import mysql.connector as mysql


Ecran = Tk()
Ecran.geometry("1100x500")
Ecran["bg"]="silver"
Label(Ecran,text="BIENVENUE \n MERCI DE REMPLIR LES CHAMPS SUIVANT SI NECESSAIRE",bg="sky blue",font=("ALGERIAN",20),width=70).pack()
#can.pack()


Ecran.title("ACCUEIL")
Host=Label(Ecran,text="Host",font=("Algerian",11))
Host.place(x=5,y=200)
Por=Label(Ecran,text="Port",font=("Algerian",11))
Por.place(x=950,y=200)
po=Entry(width=15)
po.place(x=1000,y=200)
H=Entry()
H.place(x=75,y=200)
User=Label(Ecran,text="Username",font=("Algerian",11))
User.place(x=230,y=200)
U=Entry()
U.place(x=320,y=200)
Password=Label(Ecran,text="Password",font=("Algerian",11))
Password.place(x=470,y=200)
Pwd=Entry()
Pwd.place(x=570,y=200)
Dbd=Label(Ecran,text="Database",font=("Algerian",11))
Dbd1=Entry()
Dbd1.place(x=810,y=200)
Dbd.place(x=710,y=200)
ser=H.get()
userna=U.get()
Pass=Pwd.get()
data=Dbd1.get()

def Menu():
    ser = H.get()
    userna = U.get()
    Pass = Pwd.get()
    data = Dbd1.get()
    P1=po.get()
    if ser=="" or userna=="" or data=="":
        Message.showwarning("Connection STATUS","Host, User , Databse sont indispensable\n les autres si nécéssaires",parent=Ecran)
    else:
        con1=mysql.connect(host="" + ser + "", user="" + userna + "", password="" + Pass + "",port=""+P1+"")
        mycursor = con1.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS  " + data + "")
    con = mysql.connect(host="" + ser + "", user="" + userna + "", password="" + Pass + "", database="" + data + "",port=""+P1+"")
    if con.connect():
        Message.showinfo("Connexion Status","CONNEXION AVEC SUCCES AU DATABASE")
    my=con.cursor()
    dbd = "CREATE TABLE  IF NOT EXISTS Filiere(idFiliere INT NOT NULL,NomFiliere VARCHAR(100) NOT NULL, PRIMARY KEY(idFiliere)) "
    dbd1 = "CREATE TABLE  IF NOT EXISTS Etudiant(idEtudiant INT NOT NULL,idFiliere INT NOT NULL,Nom VARCHAR(100) NOT NULL,Prenom VARCHAR(100) NOT NULL,Age INT,PRIMARY KEY(idEtudiant),FOREIGN KEY(idFiliere) REFERENCES Filiere(idFiliere))"
    my.execute(dbd)
    my.execute(dbd1)

    def inserer_e():
        idEtudiant = id_e.get()
        idFiliere = id_f.get()
        Nom = Nom_e.get()
        Prenom = Prenom_e.get()
        Age = Age_e.get()
        if idEtudiant == "" or idFiliere == "" or Nom == "" or Prenom == "" or Age == "":
            Message.showwarning("INSERT STATUS", "Tout les champs doit être fournis sauf NomFiliere",parent=root)
        else:
            my.execute("insert into etudiant(idEtudiant, idFiliere, Nom, Prenom, Age) values('" + idEtudiant + "','" + idFiliere + "','" + Nom + "','" + Prenom + "','" + Age + "')")
            my.execute("commit")
        clear_eb()
        Message.showinfo("INSERT STATUS", "INSERTION DE L'ETUDIANT  AVEC SUCCES", parent=root)

    def inserer_f():
        idFiliere = id_f.get()
        NomFiliere = Nom_f.get()
        if idFiliere == "" or NomFiliere == "":
            Message.showwarning("INSERT STATUS","idFiliere et NomFiliere doivent être fournis",parent=root)
        else:
            my.execute("insert into filiere(idFiliere, NomFiliere) values('" + idFiliere + "','" + NomFiliere + "')")
            my.execute("commit")
        clear_fb()
        Message.showinfo("INSERT STATUS", "INSERTION DE FILIERE EST AVEC SUCCES", parent=root)

    def supprimer_e():
        idEtudiant = id_e.get()
        if idEtudiant == "":
            Message.showwarning("DELETE STATUS","ID ETUDIANT EST RECOMMANDE",parent=root)
        else:
            my.execute("DELETE  FROM etudiant WHERE idEtudiant='" + idEtudiant + "'")
            my.execute("commit")
        clear_eb()
        Message.showinfo("DELETE STATUS", "LA SUPPRESSION DE L'ETUDIANT EST EFEECTUEE AVEC SUCCES", parent=root)

    def supprimer_f():
        idFiliere = id_f.get()
        if idFiliere =="":
            Message.showwarning("DELETE STATUS", "ID FILIERE EST RECOMMANDEE",parent=root)
        else:
            my.execute("DELETE  FROM filiere WHERE idFiliere='" + idFiliere + "'")
            my.execute("commit")
        clear_fb()
        Message.showinfo("DELETE STATUS", "LA SUPPRESSION DE FILIERE EST EFEECTUEE AVEC SUCCES", parent=root)

    def miseajour_e():
        idEtudiant = id_e.get()
        idFiliere = id_f.get()
        Nom = Nom_e.get()
        Prenom = Prenom_e.get()
        Age = Age_e.get()
        if idEtudiant == "" or idFiliere == "" or Nom == "" or Prenom == "" or Age == "":
            Message.showwarning("UPDATE STATUS", "TOUT LES PARAMETRE SONT RECOMMANDES SAUF NOMFILIERE",parent=root)
        else:
            my.execute("UPDATE etudiant e set e.Nom='" + Nom + "', e.idFiliere='" + idFiliere + "', e.Prenom='" + Prenom + "', e.Age='" + Age + "' WHERE e.idEtudiant='" + idEtudiant + "'")
            my.execute("commit")
        clear_eb()
        Message.showinfo("UPDATE STATUS", "LA MISE A JOUR DES ETUDIANTS EST EFEECTUEE AVEC SUCCES", parent=root)

    def miseajour_f():
        idFiliere = id_f.get()
        NomFiliere = Nom_f.get()
        if idFiliere == "" or NomFiliere == "" :
            Message.showwarning("UPDATE STATUS","idFiliere et NomFiliere sont RECOMANDEES",parent=root)
        else:
            my.execute("UPDATE filiere f set f.NomFiliere='" + NomFiliere + "' WHERE f.idFiliere='" + idFiliere + "'")
            my.execute("commit")
        clear_fb()
        Message.showinfo("UPDATE STATUS", "LA MISE A JOUR DE FILIERE EST EFEECTUEE AVEC SUCCES", parent=root)

    def Afficher_e():
        my.execute("select * from etudiant")
        d = my.fetchall()
        e = []
        j = 0
        k = 0
        while j < len(d):
            c = ["", "","","",""]
            c[0] = d[j][0]
            c[1] = d[j][1]
            c[2] = d[j][2]
            c[3] = d[j][3]
            c[4] = d[j][4]
            e.append(c)
            j = j + 1
        for item in e:
            Lb.insert(END, row_format1.format(*item, sp=" " * 2))
        my.execute("commit")


    def Afficher_f():
        my.execute("select * from filiere")
        d = my.fetchall()
        e = []
        j = 0
        k = 0
        while j < len(d):
            c = ["", ""]
            c[0] = d[j][0]
            c[1] = d[j][1]
            e.append(c)
            j = j + 1
        for item in e:
            Lb2.insert(END, row_format.format(*item, sp=" " * 2))
        my.execute("commit")

    def clear_e():
        Lb.delete(0, END)
        Afficher_e()

    def clear_f():
        Lb2.delete(0, END)
        Afficher_f()

    def clear_eb():
        Lb.delete(0, END)
        Afficher_e()

    def clear_fb():
        Lb2.delete(0, END)
        Afficher_f()
    root = Toplevel()
    root.geometry("1300x700")
    root.title("GESTION DONNEES ETUDIANTS")
    root["bg"] = "turquoise"
    Frame1 = Frame(root, height=20, width=40, bg="orange", borderwidth=2, relief=GROOVE)
    Frame1.pack(side=LEFT, padx=0, pady=0, ipadx=0, ipady=0)
    Lb = Listbox(Frame1, height=25, width=40, activestyle='dotbox', font="Helvetica", fg="yellow", bg="teal")
    label = Label(Frame1, text="LISTE DES ETUDIANTS", bg="orange")
    label.pack(padx=0, pady=0)
    Lb.pack(ipadx=0, pady=0)
    p1=["idEtudiant","idFiliere","Nom","Prenom","Age"]
    row_format1 = "{:2} {:>8} {:>15} {:>10} {:>5}"
    Lb.insert(0, row_format1.format(*p1, sp="  " * 2))
    Frame2 = Frame(root, height=40, width=100, bg="orange", borderwidth=2, relief=GROOVE)
    Frame2.pack(side=RIGHT, padx=0, pady=0, ipadx=0, ipady=0)
    Lb2 = Listbox(Frame2, height=25, width=40, activestyle='dotbox', font="Helvetica", fg="yellow", bg="teal")
    label2 = Label(Frame2, text="LISTE DES FILIERES", bg="orange")
    label2.pack(padx=0, pady=0)
    Lb2.pack(ipadx=0, pady=0)
    p = ["idFiliere", "NomFiliere"]
    row_format = "{:<8}  {:>8} "
    Lb2.insert(0, row_format.format(*p, sp=" " * 2))
    Frame4 = Frame(root, bg="powder blue", height=20, borderwidth=2, relief=GROOVE)
    Frame4.pack(side=TOP, padx=0, pady=0, ipady=10, ipadx=0)
    Lb4 = Listbox(Frame4, height=5, width=100, bg="cadet blue", fg="white", font=("Algerian", 12))
    Lb4.insert(1, "BIENVENUE \n DANS LA REPERTOIRE DE GESTION DES DONNEES DES ETUDIANTS")
    Lb4.pack(padx=0, pady=0)
    Frame3 = Frame(root, bg="red", height=70, borderwidth=2, relief=GROOVE)
    Frame3.pack(side=BOTTOM, padx=0, pady=0, ipady=10, ipadx=0)
    # Canvas(Frame3, bg="red", height=30, width=30).pack()
    # label3 = Label(Frame3, text="Avis", font=("Algerian", 12), width=30)
    Lb3 = Listbox(Frame3, height=10, width=100, bg="grey", fg="white", font=("bold", 12))
    Lb3.insert(0, "---Vueillez cliquez sur les butons pour remplir les champs nécéssaires")
    Lb3.insert(1, "---id est seulement nécéssaire pour la suppression ")
    Lb3.insert(1, "---Notez bien que la suppréssion d'une filiere doit être supprimer dans etudiant au préalable")
    Lb3.pack(padx=0, pady=0)
    idEtudiant = Label(root, text="ENTER idEtudiant", font=("Algerian", 13))
    idEtudiant.place(x=410, y=130)
    idFiliere = Label(root, text="ENTER idFiliere", font=("Algerian", 13), height=0)
    idFiliere.place(x=410, y=180)
    NomFiliere = Label(root, text="ENTER NomFiliere", font=("Algerian", 13))
    NomFiliere.place(x=410, y=230)
    Nom = Label(root, text="ENTER Nom", font=("Algerian", 13))
    Nom.place(x=410, y=280)
    Prenom = Label(root, text="ENTER Prenom", font=("Algerian", 13))
    Prenom.place(x=410, y=330)
    Age = Label(root, text="ENTER Age", font=("Algerian", 13))
    Age.place(x=410, y=380)
    id_e = Entry(root)
    id_e.place(x=600, y=130)
    id_f = Entry(root)
    id_f.place(x=600, y=180)
    Nom_f = Entry(root)
    Nom_f.place(x=600, y=230)
    Nom_e = Entry(root)
    Nom_e.place(x=600, y=280)
    Prenom_e = Entry(root)
    Prenom_e.place(x=600, y=330)
    Age_e = Entry(root)
    Age_e.place(x=600, y=380)
    Insert = Button(root, width=20, text="INSERT ETUDIANT", font=("Algerian", 10), bg="green", command=inserer_e)
    Insert.place(x=750, y=125)
    Insert = Button(root, width=20, text="INSERT FILIERE", font=("Algerian", 10), bg="green", command=inserer_f)
    Insert.place(x=750, y=175)
    DELETE_e = Button(root, text="DELETE ETUDIANT", width=20, font=("Algerian", 10), bg="red", command=supprimer_e)
    DELETE_e.place(x=750, y=235)
    DELETE_f = Button(root, text="DELETE FILIERE", width=20, font=("Algerian", 10), bg="red", command=supprimer_f)
    DELETE_f.place(x=750, y=285)
    UPDATE_e = Button(root, text="UPDATE ETUDIANT", width=20, font=("Algerian", 10), bg="yellow", command=miseajour_e)
    UPDATE_e.place(x=750, y=330)
    UPDATE_f = Button(root, text="UPDATE FILIERE", width=20, font=("Algerian", 10), bg="yellow", command=miseajour_f)
    UPDATE_f.place(x=750, y=380)
    Afficher1 = Button(root, text="AFFICHER LA LISTE DES ETUDIANTS", width=30, font=("Algerian", 10), bg="sky blue",command=clear_e)
    Afficher1.place(x=50, y=620)
    Afficher = Button(root, text="AFFICHER LA LISTE DES FILIERES", width=30, font=("Algerian", 10), bg="sky blue",command=clear_f)
    Afficher.place(x=1000, y=620)
    root.mainloop()

Conn=Button(Ecran,width=20,text=" Se Connecter",font=("Algerian",12),height=1,command=Menu)
Conn.pack(pady=200,padx=50)
Ecran.mainloop()