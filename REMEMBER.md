# PODSTAWY ALGEBRY LINIOWEJ: NOTATKA DO PRACY O FORMACH NORMALNYCH

## 1. Operacje na Macierzach Zespolonych

* **Transpozycja ($A^T$):** Zamiana wierszy z kolumnami. 
  Macierz symetryczna: $A = A^T$.
  Macierz antysymetryczna: $A = -A^T$.
* **Sprzężenie Hermitowskie ($A^*$ lub $A^H$):** Transpozycja połączona ze sprzężeniem zespolonym każdego elementu ($\bar{a}_{ji}$).
  *UWAGA:* W Twoim temacie kluczowa jest transpozycja ($A^T$), nie sprzężenie.

## 2. Wartości Własne i Wielomian Charakterystyczny

* **Równanie charakterystyczne:** $w(\lambda) = \det(A - \lambda I) = 0$.
* Pierwiastki tego równania to wartości własne $\lambda_1, \lambda_2, \dots, \lambda_n$.
* **Krotność algebraiczna:** Ile razy dana wartość własna pojawia się jako pierwiastek $w(\lambda)$.
* **Krotność geometryczna:** Liczba liniowo niezależnych wektorów własnych dla danej $\lambda$.

## 3. Relacje między Macierzami

* **Podobieństwo:** $B = P^{-1}AP$. Macierze podobne mają te same wartości własne i dzielniki elementarne.
* **Kongruencja:** $B = P^T AP$. To relacja kluczowa dla form kwadratowych i macierzy symetrycznych.
* **Podobieństwo Ortogonalne:** $B = P^T AP$, gdzie $P^T P = I$ (czyli $P^T = P^{-1}$). 
  Łączy cechy podobieństwa i kongruencji.

## 4. Problem Diagonalizacji

* **Macierz Diagonalizowalna:** Taka, która jest podobna do macierzy diagonalnej.
* **Twierdzenie Spektralne (Rzeczywiste):** Każda macierz $A \in \mathbb{R}^{n \times n}$, która jest symetryczna ($A = A^T$), JEST diagonalizowalna.
* **Przypadek Zespolony:** Macierz $A \in \mathbb{C}^{n \times n}$, która jest symetryczna ($A = A^T$), NIE MUSI być diagonalizowalna. 
  *Przykład:* $A = \begin{pmatrix} 1 & i \\ i & -1 \end{pmatrix}$ ma $\lambda = 0$ (krotność 2), ale tylko jeden wektor własny. Jest nilpotentna.

## 5. Postać Jordana (Druga Forma Normalna)

Jeśli macierz nie jest diagonalizowalna, sprowadzamy ją do postaci blokowej:
* **Klatka Jordana $J_k(\lambda)$:** Macierz $k \times k$ z $\lambda$ na przekątnej i 1-kami bezpośrednio nad nią.
* Każda macierz zespolona jest podobna do macierzy Jordana (zbiór klatek na głównej przekątnej).

## 6. Wielomian Minimalny i Dzielniki Elementarne

* **Wielomian minimalny $m(\lambda)$:** Wielomian najniższego stopnia taki, że $m(A) = 0$.
* **Dzielniki elementarne:** 1. Wyznaczamy macierz charakterystyczną $A - \lambda I$.
  2. Obliczamy największe wspólne dzielniki $D_k(\lambda)$ wszystkich podwyznaczników stopnia $k$.
  3. Wielomiany niezmiennicze to $E_k(\lambda) = D_k(\lambda) / D_{k-1}(\lambda)$.
  4. **Dzielniki elementarne** to czynniki nierozkładalne wielomianów $E_k(\lambda)$ nad ciałem $\mathbb{C}$, czyli potęgi $(\lambda - \lambda_i)^{p_{ij}}$.
  *ZNACZENIE:* Potęgi $p_{ij}$ to rozmiary klatek Jordana dla wartości własnej $\lambda_i$.

## 7. Macierz Ortogonalna ($A^T A = I$)

* Macierz, której kolumny tworzą układ ortonormalny w sensie symetrycznym.
* Wartości własne macierzy ortogonalnej występują w parach: jeśli $\lambda$ jest wartością własną, to $1/\lambda$ również (z tą samą krotnością).