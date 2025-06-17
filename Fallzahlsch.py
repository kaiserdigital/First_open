import scipy.stats as stats
import math

def fallzahl_schaetzung():
    print("=== Fallzahlkalkulation für eine Vergleichsstudie ===")
    print("Dieses Programm berechnet die erforderliche Fallzahl basierend auf:")
    print("- Signifikanzniveau (α)")
    print("- Power (1-β)")
    print("- Effektgröße (Differenz in Proportionen, z.B. 0,1 für 10%)")
    print("- Erwartete Erfolgsrate in der Kontrollgruppe (p1)")
    print("- Testart: einseitig oder zweiseitig")
    print("- Prävalenz der interessierenden Bedingung in der Gesamtpopulation (optional)")

    # Eingabeparameter mit Erklärungen
    alpha = float(input("\nGeben Sie das Signifikanzniveau α ein (z.B. 0.05): "))
    power = float(input("Geben Sie die gewünschte Power 1-β ein (z.B. 0.8 für 80%): "))
    p1 = float(input("Erwartete Erfolgsrate (Detektionsrate) in der Kontrollgruppe (z.B. 0.2 für 20%): "))
    diff = float(input("Minimal relevante Differenz in der Erfolgsrate (z.B. 0.1 für 10% Unterschied): "))

    # Abfrage der Testart
    testart = input("Soll der Test einseitig oder zweiseitig sein? (e/z): ").lower()
    if testart not in ["e", "z"]:
        print("Ungültige Eingabe. Standardmäßig wird zweiseitig verwendet.")
        testart = "z"

    # Optional: Prävalenzabfrage
    praev_input = input("Geben Sie die Prävalenz der interessierenden Bedingung in der Population an (z.B. 0.01 für 1%) oder drücken Sie Enter, um zu überspringen: ")
    if praev_input:
        praevalenz = float(praev_input)
    else:
        praevalenz = None

    # Berechnung der Fallzahl
    p2 = p1 + diff
    pooled_p = (p1 + p2) / 2
    q1 = 1 - p1
    q2 = 1 - p2
    q_pooled = 1 - pooled_p

    if testart == "z":
        z_alpha = stats.norm.ppf(1 - alpha / 2)
    else:
        z_alpha = stats.norm.ppf(1 - alpha)
    z_beta = stats.norm.ppf(power)

    n = ((z_alpha * math.sqrt(2 * pooled_p * q_pooled) + z_beta * math.sqrt(p1 * q1 + p2 * q2)) ** 2) / (diff ** 2)

    # Ausgabe
    print("\n--- Ergebnisse ---")
    print(f"Testart: {'zweiseitig' if testart == 'z' else 'einseitig'}")
    print(f"Benötigte Fallzahl pro Gruppe: {math.ceil(n)}")
    print(f"Gesamtzahl der Teilnehmer (für 2 Gruppen): {math.ceil(n * 2)}")
    print(f"Berechnungsgrundlage: Signifikanzniveau={alpha}, Power={power}, p1={p1}, Unterschied={diff}")

    # Prävalenz berücksichtigen
    if praevalenz:
        total_screened = math.ceil((n * 2) / praevalenz)
        print(f"Da die Prävalenz der interessierenden Bedingung {praevalenz*100:.2f}% beträgt,")
        print(f"müssen insgesamt ca. {total_screened} Patienten gescreent werden, um die Fallzahl zu erreichen.")

    print("------------------")

if __name__ == "__main__":
    fallzahl_schaetzung()
0.05
