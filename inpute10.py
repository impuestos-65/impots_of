# ==================================================
# SIMULATION DE PHISHING - EXEMPLE PEDAGOGIQUE
# CONTENU FICTIF - AUCUN SYSTEME REEL
# ==================================================

def afficher_entete():
    print("=" * 60)
    print(" SIMULATION NON REELLE - A DES FINS PEDAGOGIQUES")
    print(" USURPATION D'IDENTITE : ADMINISTRATION FISCALE")
    print("")
    print(" [LOGO FICTIF - DIRECTION GENERALE DES FINANCES]")
    print(" Republique Francaise (REPRESENTATION TEXTUELLE)")
    print("=" * 60)
    print()


def message_fictif():
    # Message volontairement realiste dans la forme
    return (
        "DGFiP - Avis de regularisation\n"
        "Un solde reste du concernant votre dossier fiscal.\n"
        "Merci de proceder a la mise en conformite avant majoration.\n"
        "Acces securise : https://impots-gouv.example"
    )


def analyser_indicateurs(sms):
    indicateurs = []

    if "regularisation" in sms.lower() or "majoration" in sms.lower():
        indicateurs.append("Pression administrative")

    if "dgfip" in sms.lower() or "fiscal" in sms.lower():
        indicateurs.append("Usurpation d une autorite publique")

    if "https://" in sms.lower():
        indicateurs.append("Lien HTTPS rassurant")

    return indicateurs


# -------------- EXECUTION ----------------
afficher_entete()

sms = message_fictif()
print("SMS SIMULE (FICTIF) :\n")
print(sms)

print("\nINDICATEURS DE PHISHING IDENTIFIES :")
for i in analyser_indicateurs(sms):
    print("-", i)
