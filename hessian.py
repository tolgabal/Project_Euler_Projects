from sympy import symbols, diff, Eq, solve, hessian, Matrix, pprint

# Değişkenleri tanımla
x1, x2 = symbols('x1 x2')

# Fonksiyonu tanımla
f = (x1 - 1)**2 + (x2 - 1)**2 - x1 * x2

print("           ***** ADIM 1 *****")
print("1. Gradient (birinci türevleri) al ve durağan nokta bul")

# Gradient: kısmi türevler
df_dx1 = diff(f, x1)
df_dx2 = diff(f, x2)

print("\nKısmi türevler:")
print("∂f/∂x1 =", df_dx1)
print("∂f/∂x2 =", df_dx2) #asdasdasdasd

# Gradient = 0 → denklemleri kur
eq1 = Eq(df_dx1, 0)
eq2 = Eq(df_dx2, 0)

# Denklemi çöz → durağan nokta
duragan_noktalar = solve((eq1, eq2), (x1, x2))
print("\nDurağan Nokta(lar):", duragan_noktalar)

# ADIM 2: Hessian matrisi
print("\n           ***** ADIM 2 *****")
print("2. Hessian matrisini hesapla")

variables = [x1, x2]
H = hessian(f, variables)
print("\nHessian Matrisi:")
pprint(H)

# Durağan noktada Hessian’ı değerlendir
H_point = H.subs(duragan_noktalar)
print("\nHessian Matrisi (durağan noktada):")
pprint(H_point)

# ADIM 3: Özdeğerleri hesapla ve tipi yorumla
print("\n           ***** ADIM 3 *****")
print("3. Özdeğerleri hesapla ve durağan noktanın tipini belirle")

eigenvals = H_point.eigenvals()
eigenval_list = list(eigenvals.keys())
print("\nÖzdeğerler:", eigenval_list)

# Tip yorumlama
if all(ev > 0 for ev in eigenval_list):
    print("→ Durağan nokta kesin yerel minimumdur ✅")
elif all(ev < 0 for ev in eigenval_list):
    print("→ Durağan nokta kesin yerel maksimumdur 🔻")
else:
    print("→ Durağan nokta semer noktasıdır ⚠️")