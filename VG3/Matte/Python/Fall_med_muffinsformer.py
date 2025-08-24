    #%%
    # -*- coding: utf-8 -*-
    """
    Created on Tue Sep  3 11:35:06 2024
    
    @author: ansoa037
    """
    
    # Program for å beregne fallhastigheten til muffinskopper
    
    # Gitte konstanter
    g = 9.81    # m/s^2
    
    #Inputs
    m = 0.00035 #Vekten for 1 muffinsform
    h = 4.8 #Fall høyden
    
    # Resulterende tyngde
    G1 = m*g        # Tyngden til én muffinsform
    
    
    def a1(v1, k):          # Akselerasjonen er en funksjon av farten
        R1 = k*v1**2    # Luftmotand for en gitt fart
        F1 = G1 - R1    # Kraftsum nedover for én muffinsform
        aks1 = F1/m     # Akselerasjonen til én muffinsform
        return aks1
    
    # Lager tilsvarende funksjoner for to, tre, fire og fem muffinsformer
    
    # Startverdier
    s1 = 0
    v1 = 0
    t1 = 0
    
    
    # Simuleringsteknisk
    dt = 0.1   # Simuleringssteg i sekunder
    
    s1_verdier = [s1]
    v1_verdier = [v1]
    t1_verdier = [t1]
    
    k = 0 #Start verdi på ingen luftmotstand

    k_endring = 0.0001 #Hvor mye skall luftmotstandtallet endres hver gang


    '''
    Modifisert Anders sin while løke for å kalkulere tiden det tar
    for flere verdier for k (luftmotstandstall). Koden vil gå gjennom et
    område av k-verdier fra 0 til 0.007 med en endring på 0.0001 for hver
    gang. Programmet vil skrive ut k-verdiene som resulterer i en sluttid
    i nærheten av gjennomsnitts resultatet som ble målt. Programmet vil skrive
    ut for en, to og tre muffinsformer.

    Bare første while løke kommer til å være kommentert på grunn av liten
    forskjell
    '''

    print()
    print("For en form:")
    print()

    while k < 0.007:
        #Må tilbake stille verdier og lister som tidligere har blitt brukt
        s1 = 0
        v1 = 0
        t1 = 0
        s1_verdier.clear()
        v1_verdier.clear()
        s1_verdier.clear()

        #While løkke fra Anders
        while s1 < h:
            v1 = v1 + a1(v1, k)*dt #Kalkuler den nye farten til objektet
            s1 = s1 + v1*dt #Kalkuler strekningen legemet har falt
            t1 = t1 + dt #Kalkuler tidsforløpet
    
            s1_verdier.append(t1)
            v1_verdier.append(v1)
            s1_verdier.append(s1)
        if 3.4 < t1 < 3.8: #Skriv ut hvis det er et resultat som er i nærheten av den gjennomsnitt målingen
            print("Sluttid én form: " , round(t1, 4) , "s, når k = ", round(k, 5))
        k += k_endring

    print()
    print("For to former:")
    print()
    m = 0.0007

    k = 0
    
    while k < 0.007:
        s1 = 0
        v1 = 0
        t1 = 0
        s1_verdier.clear()
        v1_verdier.clear()
        s1_verdier.clear()

        while s1 < h:
            v1 = v1 + a1(v1, k)*dt
            s1 = s1 + v1*dt
            t1 = t1 + dt
    
            s1_verdier.append(t1)
            v1_verdier.append(v1)
            s1_verdier.append(s1)
        if 2.2 < t1 < 2.5:
            print("Sluttid to former: " , round(t1, 4) , "s, når k = ", round(k, 5))
        k += k_endring

    print()
    print("For tre former:")
    print()
    m = 0.001

    k = 0
    
    while k < 0.007:
        s1 = 0
        v1 = 0
        t1 = 0
        s1_verdier.clear()
        v1_verdier.clear()
        s1_verdier.clear()

        while s1 < h:
            v1 = v1 + a1(v1, k)*dt
            s1 = s1 + v1*dt
            t1 = t1 + dt
    
            s1_verdier.append(t1)
            v1_verdier.append(v1)
            s1_verdier.append(s1)
        if 1.7 < t1 < 2.4:
            print("Sluttid tre former: " , round(t1, 4) , "s, når k = ", round(k, 5))
        k += k_endring
    # %%
