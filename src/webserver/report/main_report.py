from report.PDFReport import PDFReport



def main_report(name, street, loc, today, phone, mail, tco, clv, output_data):
    ########################################################################
    ############################## PDF-REPORT ##############################
    ########################################################################

    liste = output_data

    list1 = liste[0]
    list1 = list1.replace("[", "").replace("]", "").replace("'", "")
    entry_list = list1.split(',')
    methode1 = entry_list[1]
    methode1_datentyp = entry_list[0]
    methode1_verfahren = entry_list[2]
    methode1_lerntyp = entry_list[3]

    list2 = liste[1]
    list2 = list2.replace("[", "").replace("]", "").replace("'", "")
    entry_list = list2.split(',')
    methode2 = entry_list[1]

    beschreibung = ''

    kmeans = 'Die Verwendung des K-Means-Algorithmus erfordert eine konvexe Verteilung und ausgewogene Klassen in den Daten, um eine gute Performance zu gewährleisten. Jeder Cluster ist ungefähr ein kugelförmiger Globus im Hyperraum, die Globus sollen weit voneinander entfernt sein, und sie sollen alle ein ähnliches Volumen haben und sollen eine ähnliche Anzahl von Elementen enthalten (Domingos, 2015; Rodriguez u. a., 2019). Der K-Means-Algorithmus ist tendenziell effektiv beim Clustering großer Datensätze und hat niedrige Rechenkosten und hohe Skalierbarkeit, was ihn für Big-Data-Aufgaben geeignet macht. Er kann seine Leistung bei größeren Datenmengen erheblich steigern (Abbas, 2008; Domingos, 2015; Xu und Tian, 2015; Rodriguez u. a., 2019). Die Anzahl der Cluster muss im Voraus festgelegt werden. Die Verwendung ist auf eine bestimmte Datenkomplexität beschränkt. Sie kann generell mit komplexeren Datenverteilungen und mit un-ausgewogenen Daten nicht angemessen umgehen (Abbas, 2008; Domingos, 2015; Rodriguez u. a., 2019). Zusätzlich zu den geringen Rechenkosten kann der K-Means-Algorithmus in vielen praktischen Situationen und Big Data Aufgaben gute Ergebnisse liefern, z. B. bei der Erkennung von Anoma-lien und der Segmentierung von Daten (Abbas, 2008; Xu und Tian, 2015; Rodriguez u. a., 2019)'

    if 'K-Means' in str(methode1) :
        beschreibung = kmeans

    # Initialise new pdf_report object
    r1 = PDFReport()

    # Create new dictionary for input context to the report
    context_dict = {
        'name': name,
        'street': street,
        'loc': loc,
        'today': today,
        'phone': phone,
        'mail': mail,
        'tco': tco,
        'clv': clv,
        'methode1': methode1,
        'methode2': methode2,
        'methode1_datentyp': methode1_datentyp,
        'methode1_verfahren': methode1_verfahren,
        'methode1_lerntyp': methode1_lerntyp,
        'beschreibung': beschreibung
    }

    # Create report
    r1.create_report(context_dict)


if __name__ == "__main__":
    main_report()
