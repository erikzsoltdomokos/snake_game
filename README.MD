# Snake Game (Python + pygame)

Ez a projekt a "Szoftverfejlesztés MI támogatással" tárgy házi feladataként készült. Egy klasszikus Snake játék modern megvalósítása, amely szigorúan elválasztja a játéklogikát (backend) a megjelenítéstől (frontend).

## Tartalomjegyzék
1. [Telepítés és Futtatás](#telepítés-és-futtatás)
2. [Használati Útmutató](#használati-útmutató)
3. [Rendszerarchitektúra](#rendszerarchitektúra)
4. [MI Használat Dokumentációja](#mi-használat-dokumentációja)

---

## Telepítés és Futtatás

### Előfeltételek
- Python 3.10 vagy újabb verzió
- `pip` csomagkezelő

### Telepítés
1. Klónozd le a repót vagy töltsd le a forráskódot.
2. Telepítsd a szükséges függőségeket (pygame):

```bash
python -m pip install pygame
```

### Futtatás
A játék indításához futtasd a `main.py` fájlt a projekt gyökérkönyvtárából:

```bash
python main.py
```

---

## Használati Útmutató

### Menü Kezelés
A játék indításakor a főmenü fogad.
- **Fel/Le** vagy **W/S**: Nehézségi szint kiválasztása (Easy, Normal, Hard).
- **Enter** vagy **Space**: Játék indítása a kiválasztott szinten.
- **R**: "Wrap" (átjárható falak) mód be/kikapcsolása.
- **F**: Teljes képernyő (Fullscreen) mód váltása.
- **H** vagy **F1**: Top 10 dicsőséglista (Highscores) megjelenítése/elrejtése.
- **Esc** vagy **Q**: Kilépés.

### Játék Közben
- **Nyilak** vagy **WASD**: A kígyó irányítása.
- **P**: Szünet (Pause) be/kikapcsolása.
- **T**: Téma váltása (Sár/Vibráló).
- **Esc**: Kilépés a menübe.

### Játék Célja
Irányítsd a kígyót, hogy megegye a piros almákat. Minden alma növeli a pontszámot és a kígyó hosszát.
- **Normál mód:** Ha a falnak vagy a saját farkadnak ütközöl, a játéknak vége.
- **Wrap mód:** A falakon át lehet menni (a túloldalon jössz ki), de a saját farkadnak ütközés továbbra is végzetes.
- **Bónusz étel:** Időnként megjelenik egy arany színű bónusz étel, amely extra pontot ér, de csak rövid ideig elérhető.

### Dicsőséglista
Ha a pontszámod bekerül a legjobb 10 közé, a játék a végén megkérdezi a nevedet, és elmenti az eredményedet.

---

## Rendszerarchitektúra

A projekt szigorúan követi a **Backend-Frontend szétválasztás** elvét.

### Backend (`backend/` mappa)
A backend felelős a játék teljes logikájáért. **Nem tartalmaz semmilyen grafikus (pygame) hívást.**
- **`state.py`**: A központi `GameState` osztályt tartalmazza. Ez tárolja a pályát, a kígyót, az ételeket és a pontszámot. Az `update()` metódus végzi a léptetést.
- **`snake.py`**: A kígyó modellje. Kezeli a testrészek koordinátáit, a növekedést és az irányváltást (megakadályozva a 180 fokos visszafordulást).
- **`collision.py`**: Ütközésdetektáló logika (falak, önmagába harapás).
- **`food.py`**: Ételgenerálás logikája, biztosítva, hogy ne kerüljön étel a kígyó testére.
- **`difficulty.py`**: Nehézségi szintek definíciója (sebesség, növekedési ráta).

### Frontend (`frontend/` mappa)
A frontend felelős a megjelenítésért és a felhasználói interakcióért.
- **`menu.py`**: A főmenü rendszer (`Menu` osztály). Kezeli a nehézségi szint választást, beállításokat (wrap, fullscreen), és a highscore listát.
- **`screens.py`**: Overlay képernyők (game over, név prompt, top 10 ellenőrzés).
- **`renderer.py`**: A `GameState` alapján kirajzolja a játékot pygame felületekre. Támogatja a témákat, skálázást, és a szünet overlay-t.
- **`input_handler.py`**: A billentyűzet eseményeket (pygame events) fordítja le játékparancsokra (irányváltás, szünet).
- **`game_loop.py`**: A játék fő ciklusa. Ez hívja meg a backend `update()`-jét és a frontend `render()`-ét minden képkockában.
- **`sound_manager.py`**: Szintetizált hangeffektek kezelése (evés, ütközés, menü navigáció). Tisztán kódból generált hangok, nincs szükség külső fájlokra.
- **`scoreboard.py`**: A pontszámok betöltése és mentése JSON fájlba.

### Főprogram (`main.py`)
Minimális belépési pont (92 sor). Orchestrálja a menüt, játékindítást, score mentést és a game over flow-t. Nem tartalmaz üzleti logikát vagy UI kódot.

---

## MI Használat Dokumentációja

A projekt fejlesztése során a **GitHub Copilot** (GPT-5, Gemini 3 Pro, Claude Sonnet 4.5 modellekkel) volt a fő fejlesztőpartner. Az alábbiakban részletezem az MI használatát a különböző fázisokban.

### 1. Specifikáció
- **Eszköz:** GitHub Copilot
- **Feladat:** A projekt követelményeinek és struktúrájának tisztázása.
- **Prompt példa:** *"Generálj egy teljes, működőképes projektvázat Python és pygame használatával, szigorú backend-frontend szétválasztással."*
- **Eredmény:** A mappastruktúra és a modulok feladatainak meghatározása (lásd `SPECIFICATION.md`).

### 2. Backend Fejlesztés
- **Eszköz:** GitHub Copilot
- **Feladat:** A játéklogika implementálása grafikus függőségek nélkül.
- **Prompt példa:** *"Implementáld a Snake mozgását és növekedését a backendben. A backend nem importálhat pygame-et."*
- **Prompt példa:** *"Adj hozzá egy 'wrap' módot, ahol a kígyó átmegy a falakon."*
- **Eredmény:** Tiszta Python kód, amely egységtesztelhető és független a megjelenítéstől.

### 3. Frontend Fejlesztés
- **Eszköz:** GitHub Copilot
- **Feladat:** A backend állapotának vizualizációja és input kezelés.
- **Prompt példa:** *"Készíts egy renderert, ami kirajzolja a rácsot, a kígyót lekerekített sarkokkal, és az almát."*
- **Prompt példa:** *"Implementálj fullscreen módot, ami skálázza a játékteret a képernyő méretére."*
- **Eredmény:** Reszponzív, skálázható grafikus felület, témaváltóval és HUD-dal.

### 4. Dokumentáció
- **Eszköz:** GitHub Copilot
- **Feladat:** A README.md és a kódkommentek generálása.
- **Prompt példa:** *"Írj egy részletes README-t, ami tartalmazza a telepítést, a billentyűkiosztást és az architektúra leírását."*
- **Eredmény:** Ez a dokumentum.

### Összegzés
Az MI asszisztens a kódírás mintegy 90%-át végezte, beleértve a refaktorálást, a hibajavítást (pl. import hibák, fullscreen villogás) és az új funkciók (highscores, bónusz étel) hozzáadását. A fejlesztő szerepe a specifikálás, a kód átnézése és a tesztelés volt.
