---
name: thesis-chapter-review
description: >-
  Review rozdziałów pracy licencjackiej o formach normalnych zespolonych macierzy
  symetrycznych, antysymetrycznych i ortogonalnych (na podstawie Gantmachera, "Teoria
  macierzy"). Użyj tego skilla zawsze, gdy użytkownik prosi o sprawdzenie, zrecenzowanie,
  review, korektę lub ocenę rozdziału pracy (pliku .tex), niezależnie czy prosi wprost o
  "review" czy np. "sprawdź ten rozdział", "co jest nie tak w tym dowodzie", "czy to ma
  sens matematycznie", "popraw gramatykę w tym pliku". Skupia się na trzech rzeczach -
  po pierwsze poprawności matematycznej dowodów i twierdzeń, po drugie spójności
  terminologicznej i logicznej z resztą pracy (definicje muszą poprzedzać użycie,
  numeracja i oznaczenia muszą być konsekwentne), po trzecie poprawności językowej
  (gramatyka, styl akademicki po polsku). NIE edytuje plików pracy samodzielnie - tylko
  raportuje i proponuje poprawki do zatwierdzenia przez użytkownika.
---

# Review rozdziałów pracy licencjackiej

Skill do recenzowania rozdziałów pracy licencjackiej pt. **"Formy normalne zespolonych macierzy
symetrycznych, antysymetrycznych oraz ortogonalnych"**. Praca dowodzi/omawia twierdzenia 5, 6 i 9
z rozdziału XI podręcznika F.R. Gantmachera "Teoria macierzy", oparta na aparacie dzielników
elementarnych (VI(3)) i formy normalnej Jordana (VI(6)).

## Twarda zasada: TYLKO REVIEW, ŻADNYCH EDYCJI BEZ ZGODY

To jest zasada nadrzędna z CLAUDE.md tego projektu i obowiązuje zawsze:

- Nigdy nie modyfikuj, nie nadpisuj i nie twórz plików pracy (.tex, .docx, .md) w ramach tego skilla.
- Wynikiem pracy tego skilla jest **raport recenzyjny** (w czacie lub jako osobny plik notatek,
  nigdy jako podmiana oryginału).
- Jeśli chcesz zaproponować konkretną poprawkę (np. przeformułowanie zdania, brakującą definicję),
  pokaż ją jako propozycję "przed / po" i poczekaj na wyraźne potwierdzenie użytkownika, zanim
  cokolwiek zapiszesz do pliku.
- Dotyczy to też drobnych poprawek — literówek, interpunkcji, zmiany szyku zdania.

## Krok 0: Znajdź i wczytaj kontekst

1. Znajdź plik(i) .tex rozdziału do review — użytkownik zwykle wskaże ścieżkę lub nazwę rozdziału.
   Jeśli nie wskazał, zapytaj który rozdział / plik.
2. Jeśli to możliwe, wczytaj też sąsiednie/poprzednie rozdziały (albo main.tex / spis treści),
   żeby sprawdzić spójność terminologiczną — definicje i oznaczenia wprowadzone wcześniej muszą
   być używane konsekwentnie później.
3. Sprawdź, czy w rozmowie (lub w projekcie) są już wklejone fragmenty źródłowe z Gantmachera
   (dokładne sformułowania twierdzeń 5, 6, 9, definicji dzielników elementarnych, twierdzenia
   Jordana). **Nie zgaduj z pamięci treści tych twierdzeń** — różne wydania/tłumaczenia mogą się
   różnić. Jeśli potrzebnego fragmentu nie ma, zapytaj użytkownika o wklejenie/skan strony z
   książki, zamiast rekonstruować twierdzenie z pamięci.

## Krok 1: Poprawność matematyczna (priorytet #1)

Dla każdego dowodu / twierdzenia / definicji w rozdziale sprawdź:

- **Logiczna poprawność kroków dowodu** — czy każdy krok wynika z poprzedniego, czy nie ma luk
  (np. "z tego oczywiście wynika", które w rzeczywistości wymaga uzasadnienia).
- **Kwantyfikatory i założenia** — czy założenia twierdzenia są jawnie użyte w dowodzie, czy
  wniosek faktycznie odpowiada tezie (nie jest ani za mocny, ani za słaby).
- **Poprawność algebraiczna** — rachunki na macierzach, wyznacznikach, wartościach/wektorach
  własnych, transponowaniu/sprzężeniu — przelicz krytyczne kroki samodzielnie, jeśli to możliwe.
- **Rozróżnienie rzeczywiste vs. zespolone** — praca opiera się na kontraście: twierdzenie
  spektralne działa nad R, ale nie nad C w tej samej formie (kontrprzykład: nilpotentne macierze
  symetryczne). Sprawdź, czy rozdział nigdzie po cichu nie zakłada własności prawdziwych tylko
  nad R (np. dodatniej określoności, istnienia bazy ortonormalnej z rzeczywistych wartości
  własnych) tam, gdzie mowa o C.
- **Zgodność z podanym źródłem (Gantmacher)** — jeśli użytkownik dostarczył dokładne
  sformułowanie twierdzenia/definicji, porównaj punkt po punkcie ze sformułowaniem w rozdziale:
  czy założenia, teza i oznaczenia się zgadzają. Jeśli sformułowania nie dostarczono, oznacz to
  wprost jako "nie zweryfikowane ze źródłem — brak dostarczonego fragmentu" zamiast milczeć lub
  zgadywać.

## Krok 2: Spójność i konsekwencja całości pracy

- **Kolejność wprowadzania pojęć** — żaden termin, oznaczenie czy wynik nie może być użyty, zanim
  zostanie zdefiniowany/udowodniony wcześniej w pracy (lub jawnie zacytowany ze źródła). Zrób listę
  terminów użytych w rozdziale i sprawdź każdy pod tym kątem.
- **Spójność oznaczeń** — te same obiekty matematyczne powinny być oznaczane tak samo w całej
  pracy (np. jeśli macierz antysymetryczna to wcześniej `A`, a w tym rozdziale nagle `S`, to
  zgłoś to jako niespójność).
- **Spójność numeracji** — numery twierdzeń/definicji/wzorów powinny być zgodne z resztą pracy
  i (tam gdzie to istotne) z numeracją źródła (np. "Twierdzenie 5" faktycznie odpowiada
  Twierdzeniu 5 z rozdz. XI Gantmachera, a nie innemu numerowi).
- **Kontrola cross-referencji** (`\ref`, `\label`, `\cite` w LaTeX) — sprawdź, czy każde odwołanie
  ma odpowiadającą etykietę i czy nie ma "wiszących" odwołań.

## Krok 3: Poprawność językowa (polski, styl akademicki)

- Gramatyka, składnia, interpunkcja (w tym poprawne stosowanie polskiej notacji matematycznej,
  np. przecinek jako separator dziesiętny, spójna terminologia polska/obcojęzyczna).
- Styl akademicki: unikanie potocznego języka, spójny czas i tryb (zwykle czas teraźniejszy dla
  faktów matematycznych), konsekwentne stosowanie 1. os. l.mn. ("pokażemy, że...") lub formy
  bezosobowej — sprawdź, co dominuje w reszcie pracy, i zgłoś odstępstwa.
- Nie poprawiaj tekstu w pliku — tylko wypisz znalezione miejsca z sugerowaną poprawką do
  akceptacji.

## Krok 4: Format raportu

Zwróć recenzję w czacie (nie jako plik, chyba że użytkownik prosi o plik) w formie:

1. **Streszczenie** (2-3 zdania): ogólna ocena rozdziału.
2. **Błędy krytyczne** — luki logiczne, błędy matematyczne, niezdefiniowane pojęcia. Dla każdego:
   lokalizacja (numer strony/linii/twierdzenia w .tex), opis problemu, sugerowana poprawka.
3. **Niespójności** — terminologia, oznaczenia, numeracja.
4. **Uwagi językowe** — zebrane w krótszej formie (lista, nie osobny akapit na każdą literówkę).
5. **Pytania do użytkownika** — miejsca, gdzie potrzebny jest fragment źródła z Gantmachera, żeby
   dokończyć weryfikację.

Nie używaj emoji (✓, ✅, 🚀, ⚠️ itd.) — zgodnie z zasadami projektu, także w raporcie.

## Kiedy pytać użytkownika zamiast zgadywać

- Brak dostarczonego dokładnego sformułowania twierdzenia/definicji ze źródła → zapytaj, nie
  rekonstruuj z pamięci.
- Niejasne, czy dana niespójność oznaczeń jest zamierzona (np. różne konwencje w różnych
  rozdziałach) → zapytaj zamiast automatycznie flagować jako błąd.
- Każda sugerowana zmiana treści pracy → zawsze czeka na wyraźne "tak, zmień" od użytkownika,
  zanim cokolwiek zostanie zapisane do pliku.