import json 


LEDEN_BESTAND = "leden.json" 


def laad_leden():
    try:
        
        with open(LEDEN_BESTAND, "r") as f:
            return json.load(f) 
    except FileNotFoundError:
        return []  


def bewaar_leden(leden):
    with open(LEDEN_BESTAND, "w") as f:
        json.dump(leden, f, indent=4)

def nieuw_lid():
    naam = input("Naam: ")
    geboortedatum = input("Geboortedatum (YYYY-MM-DD): ")
    telefoon = input("Telefoonnummer: ")
    adres = input("Adres: ")
    
    
    lidmaatschapsnummer = int(input("Lidmaatschapsnummer: "))

    leden = laad_leden()

    
    for lid in leden:
        if lid['lidmaatschapsnummer'] == lidmaatschapsnummer:
            print("Dit lidmaatschapsnummer bestaat al, probeer een ander nummer.")
            return

    leden.append({
        "naam": naam,
        "geboortedatum": geboortedatum,
        "telefoon": telefoon,
        "adres": adres,
        "lidmaatschapsnummer": lidmaatschapsnummer
    })

    bewaar_leden(leden)
    print(f"Lid toegevoegd met lidmaatschapsnummer {lidmaatschapsnummer}!")


def bewerk_lid():
    leden = laad_leden()
    lidmaatschapsnummer = int(input("Lidmaatschapsnummer van het te bewerken lid: "))

    for lid in leden:
        if lid["lidmaatschapsnummer"] == lidmaatschapsnummer:
            print(f"Huidige gegevens van {lid['naam']}: Geboortedatum: {lid['geboortedatum']}, Telefoon: {lid['telefoon']}, Adres: {lid['adres']}")
            
            nieuwe_geboortedatum = input(f"Nieuwe geboortedatum (leeg laten voor geen wijziging): ")
            if nieuwe_geboortedatum:
                lid["geboortedatum"] = nieuwe_geboortedatum

            nieuwe_telefoon = input(f"Nieuwe telefoon (leeg laten voor geen wijziging): ")
            if nieuwe_telefoon:
                lid["telefoon"] = nieuwe_telefoon

            nieuwe_adres = input(f"Nieuw adres (leeg laten voor geen wijziging): ")
            if nieuwe_adres:
                lid["adres"] = nieuwe_adres

            bewaar_leden(leden)
            print(f"Gegevens van {lid['naam']} zijn bijgewerkt!")
            return

    print("Lid niet gevonden.")


def verwijder_lid():
    leden = laad_leden()
    lidmaatschapsnummer = int(input("Lidmaatschapsnummer van het te verwijderen lid: "))

    for lid in leden:
        if lid["lidmaatschapsnummer"] == lidmaatschapsnummer:
            bevestiging = input(f"Weet je zeker dat je {lid['naam']} wilt verwijderen? (ja/nee): ")
            if bevestiging.lower() == "ja":
                leden.remove(lid)
                bewaar_leden(leden)
                print(f"Lid {lid['naam']} is verwijderd!")
            return

    print("Lid niet gevonden.")


def zoek_lid():
    leden = laad_leden()
    zoekterm = input("Zoek op naam of lidmaatschapsnummer: ")

    for lid in leden:
        if zoekterm.lower() in lid["naam"].lower() or str(lid["lidmaatschapsnummer"]) == zoekterm:
            print(f"Lid gevonden: {lid['naam']}, Geboortedatum: {lid['geboortedatum']}, Telefoon: {lid['telefoon']}, Adres: {lid['adres']}, Lidmaatschapsnummer: {lid['lidmaatschapsnummer']}")
            return

    print("Lid niet gevonden.")


def toon_leden():
    leden = laad_leden()
    for lid in leden:
        print(f"{lid['lidmaatschapsnummer']}: {lid['naam']}")


def menu():
    while True:
        print("\n1. Nieuw lid toevoegen")
        print("2. Bestaand lid bewerken")
        print("3. Lid verwijderen")
        print("4. Lid zoeken")
        print("5. Alle leden tonen")
        print("6. Afsluiten")
        keuze = input("Kies een optie: ")

        if keuze == "1":
            nieuw_lid()
        elif keuze == "2":
            bewerk_lid()
        elif keuze == "3":
            verwijder_lid()
        elif keuze == "4":
            zoek_lid()
        elif keuze == "5":
            toon_leden()
        elif keuze == "6":
            break
        else:
            print("Ongeldige keuze, probeer opnieuw.")

if __name__ == "__main__":
    menu()

  



