if __name__ == "__main___":
    t = 0.5
    v0 = 2
    a = 0.2
    strekning = v0*t + 0.5*a*t**2
    print(strekning)
    #gammel måte å skrive format
    print("Etter {:.2f} sekunder, vil objektet ha flyttet seg {:.3f} meter".format(t,strekning))

    #ny format code oppsett
    print(f"Etter {t:.2f} sek, vil objektet ha flyttet seg {strekning:.2f} m")
    print(f"{strekning:.2f}")
    # Her ser man at den printer ikke runde tall, men float. Hvis du vil runde opp eller ned bruker vi func round():

    print("#"*40)
    print(round(0.5)) 
    print(round(1.5))
    print(round(2.5))
    print(round(3.5))
    # Kalkulator for Volum, m/radius målt i cm
    from math import pi
    R = 22 
    v = (4/3)*pi*R**3
    print(f"Volum: {v:.2f}")

    #Finn ut typen til variabelen
    a = 1
    print(type(a))

# ALT utenfor if __name__=="__main__" exc not hvis ikke det kalles på

""" Mutable vs Immutable: 
Immutable: bool, int, float, str, tuple
Mutable: list, dict, set. 
Dvs noen variabler kan endres på og andre kan ikke, immutable kan endres. Mutable kan vi bare f.eks legge til se eks:
"""
a1 = 9
b1 = a1 
a1 += 9
print(b1)

a2 = [1]
b2 = a2
a2.append(2)
print(b2)





