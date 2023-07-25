import sqlite3

# Vytvoření databáze
conn = sqlite3.connect("databaze.db")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS databaze (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        jmeno TEXT,
        prijmeni TEXT,
        telefon INTEGER,
        vek INTEGER
)''')

# Funkce programu
def pridat_pojistence(jmeno, prijmeni, telefon, vek):
    c.execute("INSERT INTO databaze (jmeno, prijmeni, telefon, vek) VALUES (?,?,?,?)", (jmeno, prijmeni, telefon, vek))
    conn.commit()

def vypsat_pojistence():
    c.execute("SELECT * FROM databaze")
    pojistenci = c.fetchall()
    if len(pojistenci) == 0:
        print("V databázi nejsou žádní pojištěnci. Musíte přidat nějakého uživatele.")
        pridat_pojistence(jmeno, prijmeni, telefon, vek)
    else:
        print("--------------------\n"
               "Seznam pojištěnců:\n"
               "--------------------")
        for pojistenec in pojistenci:
            id, jmeno, prijmeni, telefon, vek = pojistenec
            print(f"ID: {id}\n"
                  f"Jméno: {jmeno}\n"
                  f"Příjmení: {prijmeni}\n"
                  f"Telefonní číslo: {telefon}\n"
                  f"Věk: {vek}\n")
            print("-" * 10)
        print(f"Celkový počet pojištěnců: {len(pojistenci)}")

def vyhledat_pojistence():
    jmeno = input("Zadejte jméno pojištěnce: ")
    prijmeni = input("Zadejte příjmení pojištěnce: ")
    c.execute("SELECT * FROM databaze WHERE jmeno = ? AND prijmeni = ?", (jmeno, prijmeni))
    nalezeni = c.fetchall()
    if len(nalezeni) == 0:
        print("Pojištěnec nenalezen.")
    else:
        print("Nalezení pojištěnci:\n")
        for pojistenec in nalezeni:
            id, jmeno, prijmeni, telefon, vek = pojistenec
            print(f"ID: {id}\n"
                  f"Jméno: {jmeno}\n"
                  f"Příjmení: {prijmeni}\n"
                  f"Telefonní číslo: {telefon}\n"
                  f"Věk: {vek}\n")
            print("-" * 10)
    return

# Hlavní program
print("--------------------\n"
      "Evidence pojištěnců\n"
      "--------------------")

print("1 - Přidat nového pojištěnce\n"
      "2 - Vypsat všechny pojištěnce\n"
      "3 - Vyhledat pojištence\n"
      "4 - Konec\n")

vyber = ""
while vyber not in ("1", "2", "3", "4"):
    vyber = input("Vyberte si akci (1-4): ")
    if vyber == "1":
        while True:
            print("Přidání pojištěnce:\n")
            jmeno = input("Zadejte jméno pojištěnce: ")
            prijmeni = input("Zadejte příjmení: ")
            telefon = input("Zadejte telefonní číslo (bez mezer): ")
            while len(telefon) != 9 or not telefon.isdigit():
                print("Neplatné telefonní číslo. Zadejte devítimístné číslo bez mezer a znaků.")
                telefon = input("Zadejte telefonní číslo (bez mezer): ")
            vek = input("Zadejte věk: ")
            while not vek.isdigit() or int(vek) < 0 or int(vek) > 99:
                print("Neplatný věk. Zadejte číselnou hodnotu 0 až 99.")
                vek = input("Zadejte věk: ")
            telefon = int(telefon)
            vek = int(vek)
            pridat_pojistence(jmeno, prijmeni, telefon, vek)
            volba = input("Přejete si přidat dalšího pojištěnce? (ano/ne): ")
            if volba.lower() != "ano":
                break
    elif vyber == "2":
        vypsat_pojistence()
    elif vyber == "3":
        vyhledat_pojistence()    
    elif vyber == "4":
        print("Program skončil.")
        break
    else:
        print("Neplatná volba. Zadejte číslo možnosti (1-4): ")
