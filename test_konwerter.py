import konwerter

kilometry = 6
mile = 3

wynik_1 = konwerter.km_na_mile(kilometry)
wynik_2 = konwerter.mile_na_km(mile)

print(f"{kilometry} km to {wynik_1:.2f} mil")
print(f"{mile} mil to {wynik_2:.2f} km")

import konwerter2

cm= 1
m= 1

wynik_3= konwerter2.cm_na_m(cm)

print(f"{cm}cm to {wynik_3}m")

wynik_4= konwerter2.m_na_cm(m)
print(f"{m}m to {wynik_4}cm")