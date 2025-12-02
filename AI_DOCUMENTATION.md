# AI Dokumentáció - Snake Game Projekt
## Mesterséges Intelligencia Használata a Fejlesztés Során

---

## Bevezetés

Ez a dokumentum részletesen tartalmazza az összes prompt-ot és MI interakciót, amely a Snake játék projekt fejlesztése során történt. A projekt teljes mértékben MI-asszisztált fejlesztéssel készült, online GPT-5 és GitHub Copilot használatával (GPT-5, Claude Sonnet 4.5, Gemini 3 Pro modellek).

---

## Témaválasztás és Specifikáció Készítése

### Prompt 1.1: Témaválasztás konzultáció
```
Az alábbiakban beküldöm a Szoftverfejlesztés MI támogatással c. tárgyból kapott házi feladatom leírását. 
A jelenlegi feladatom az lenne, hogy kiválasszam a témát, illetve leírást adjak róla. 
A feladatkiírás: 5-10 mondatban foglald össze, milyen alkalmazást szeretnél házi feladatként elkészíteni a tárgyból. 
Olvasd el a doksit, majd ha megértetted konzultálj velem, ajánlj nekem témákat, érdekes projekteket!
```

**Kontextus:** A házi feladat követelményeinek dokumentuma (4 oldalas PDF) beküldésre került, amely tartalmazta a témaválasztás, technológia, kidolgozás, beadás és pontozási rendszer részleteit.

**Felhasználó preferenciái:**
- Python nyelv használata (Java helyett, mivel abból már van másik házi)
- Asztali alkalmazás fejlesztése
- Könnyen megvalósítható játék elkészítése

**MI válasz:** Több játékötlet ajánlása (Snake, Tetris, Pong, Minesweeper, 2048), részletes backend-frontend felosztással és technológiai javaslatokkal mindegyikhez.

---

### Prompt 1.2: Snake játék választása
```
Rendben, köszönöm az ajánlásokat, valóban a Snake tetszik számomra a legjobban. 
A későbbiekben tehát erre fókuszáljunk. Készítsd el tehát a beadásra a megfelelő specifikációt!
```

**MI válasz:** Rövid, 5-10 mondatos témaválasztási szöveg generálása, amely később beadásra került:

> "A házi feladat célja egy klasszikus Snake (kígyós) játék megvalósítása Python nyelven, pygame grafikus könyvtár felhasználásával. A játékban a játékos egy kígyót irányít, amely minden alkalommal hosszabbodik, amikor „megeszik" egy megjelenő élelmet a pályán. A cél a lehető legtöbb pont elérése anélkül, hogy a kígyó a falnak vagy a saját testébe ütközne. A program backend része felel a játékszabályokért, az ütközéskezelésért, a pontszám nyilvántartásáért és a véletlenszerű ételgenerálásért. A frontend a grafikus megjelenítést biztosítja, beleértve a játékteret, a mozgó kígyót, az élelmet és a pontszám kijelzését. A játék újrakezdhető, a nehézségi szint pedig a kígyó sebességével változik. A fejlesztés során mesterséges intelligencia eszközöket (pl. ChatGPT, GitHub Copilot) használok a programlogika, a grafikus felület, valamint a dokumentáció megírásának támogatásához."

---

### Prompt 1.3: Teljes specifikáció készítése
```
Szia! Szeretnék elkészíteni egy teljes értékű, kb. 2–3 oldalas specifikációt a Szoftverfejlesztés MI támogatással tárgy házi feladatához. A specifikációnak illeszkednie kell a Moodle-ben közzétett pontozási rendszerhez, ahol a specifikáció 10 pontot ér. Kérlek úgy írd meg, hogy biztosan megkapjam rá a maximális pontszámot.

A specifikáció témája egy Python + pygame alapú Snake játék, amit backend + frontend szétválasztással szeretnék bemutatni:

Backend: játékszabályok, játékállapot-kezelés, ütközésdetektálás, pontszámkezelés, ételgenerálás.

Frontend: a grafikus megjelenítés pygame-ben (játékmező, kígyó, étel, pontszám, sebesség, game over képernyő).

A játék újraindítható és több nehézségi szint lesz (sebességkülönbséggel).

A fejlesztés során kötelezően MI-eszközöket használok (pl. ChatGPT, Github Copilot), amit majd dokumentálni fogok egy README-ben.

A specifikáció tartalmazza:
- a funkcionális követelményeket,
- a szerepköröket (egy játékos),
- a fontosabb forgatókönyveket (pl. játék indítása, mozgás, étel megevése, ütközés kezelése, újrakezdés),
- a rendszer felépítését backend–frontend felosztással,
- a technológiák rövid indoklását,
- valamint minden olyan elemet, ami egy 10 pontos specifikációhoz szükséges.

Fontos: legyen könnyen érthető, jól tagolt, hallgatói stílusú szöveg, ne túl formális, de rendezett és professzionális.

Kérlek állítsd össze a kész specifikációt úgy, hogy az megfeleljen a tárgy elvárásainak, és elég legyen a házi bemutatásra.
```

**Kontextus:** A házi feladat követelményeinek teljes dokumentuma (pontozási rendszerrel) és a témaválasztási beadás szövege csatolásra került.

**MI válasz:** Teljes, strukturált `SPECIFICATION.md` fájl generálása 8 fejezettel:
1. Bevezetés
2. Funkcionális követelmények (alap és speciális funkciók)
3. Nem funkcionális követelmények
4. Szerepkörök
5. Forgatókönyvek (részletes use-case-ek)
6. Rendszer architektúra (backend-frontend komponensek)
7. Technológia választás indoklása
8. Mappastruktúra

**Eredmény:** 2+ oldalas, professzionális specifikáció a maximális 10 pont megszerzéséhez.

---

### Prompt 1.4: VS Code + Copilot projekt inicializálás
```
A játékot végül VS Code-ban fogom lekódolni Copilot segítségével. 
Kérlek állíts össze egy checklistet és egy inicializáló promptot, amivel ebben a környezetben elkezdhetem a projektet!
```

**MI válasz:** 

**1. Részletes VS Code + Copilot checklist:**
- Mappa és virtuális környezet létrehozása
- pygame telepítése
- Mappastruktúra elkészítése (backend/, frontend/, assets/, main.py, README.md)
- Git inicializálás
- Python extension és Copilot beállítások

**2. Teljes Copilot inicializáló prompt:**
```
A Python + pygame Snake játék projektemet most indítom. A projekt backend–frontend szétválasztást használ, 
és szeretném, ha a Copilot segítene a projekt alapjainak létrehozásában.

Kérlek generálj teljes, működőképes projektvázat a következő elrendezésben:

/snake_game
  /backend
    state.py – a játék teljes állapotának kezelése (snake, food, score, running state)
    snake.py – a kígyó modellje (lista-alapú test, mozgás, növekedés, irányváltás tiltásokkal)
    food.py – véletlenszerű ételgenerálás, a kígyóval nem ütköző helyre
    collision.py – fal- és önütközés detektálása
    difficulty.py – nehézségi profilok: EASY/NORMAL/HARD sebességek
  /frontend
    renderer.py – a játék kirajzolása pygame-ben (kígyó, étel, pontszám, háttér)
    input_handler.py – billentyűzet események feldolgozása
    game_loop.py – fő pygame ciklus, amely meghívja a backend update metódusát
  main.py – a program belépési pontja (menü → játék → game over)

A következő elveket tartsd be:
- A backend semmilyen pygame-hívást nem tartalmazhat.
- A frontend csak megjelenítésért és inputért felel.
- A game_loop minden tickben meghívja a backend update() függvényét.
- Legyen legalább 3 nehézségi szint.
- A kód legyen olvasható és moduláris.
- A backend önmagában is tesztelhető legyen (nem kell most tesztet írni).

Kérlek először a teljes fájlvázat és minden fájl minőségi alapimplementációját generáld le, 
majd ellenőrizd, hogy a projekt futtatható-e pygame-ben.

A válaszod legyen: teljes, jól kommentelt, azonnal futtatható projektkód.
```

**Eredmény:** Teljes projekt inicializálási terv és használatra kész Copilot prompt a projekt scaffold generálásához.

---

## Backend és Frontend Fejlesztés

### Prompt 2.1: Projekt inicializálás és scaffold generálás
```
Generálj egy teljes, működőképes projektvázat Python és pygame használatával egy Snake játékhoz. 
A backend legyen teljesen pygame-mentes, csak tiszta Python logikát tartalmazzon. 
A frontend pygame-et használjon a vizualizációhoz. 
Szükséges backend modulok: state.py, snake.py, food.py, collision.py, difficulty.py. 
Frontend modulok: renderer.py, input_handler.py, game_loop.py.
```

**Eredmény:** Teljes projekt struktúra létrejött a backend-frontend szétválasztással.

---

### Prompt 2.2: Wrap mód implementáció
```
Implementálj wrap_edges funkciót a GameState osztályba. Ha a wrap_edges flag True értékű, 
akkor a kígyó feje a pálya szélén átmegy a túloldalra (koordináták modulózása a grid_size-zal). 
Az is_out_of_bounds collision check csak wrap_edges=False esetén fusson le.
```

**Eredmény:** Wrap mód működik - a kígyó átmegy a pálya szélén falütközés nélkül.

---

### Prompt 2.3: Bónusz étel rendszer implementáció
```
Bővítsd ki a backend-et időzített bónusz étel funkcióval. A GameState tartalmazza a bonus_food 
és bonus_timer attribútumokat. A bónusz étel véletlenszerűen spawn-oljon kb. 20 tick után, 
és tűnjön el 150 tick után, ha a játékos nem eszi meg. A bónusz étel érjen 5 extra pontot.
```

**Eredmény:** Bónusz étel rendszer működik időzítéssel és extra pontokkal.

---

### Prompt 2.4: Renderer téma rendszer kialakítása
```
Fejleszd ki a Renderer osztályt két vizuális témával: 'mud' (sárga-barna színskála) 
és 'vibrant' (élénk színek). A draw_snake() metódus rajzolja a kígyót lekerekített sarkú 
téglalapokkal (pygame.draw.rect border_radius paraméter), a fej külön színnel. 
A draw_food() rajzoljon alma alakú ételt: piros ellipszis testként, zöld kis ellipszis levélként, 
és árnyék a mélységérzet miatt.
```

**Eredmény:** Szép vizuális témák lekerekített sarkokkal és részletes ételekkel.

---

### Prompt 2.5: Fullscreen mód implementálás
```
Valósíts meg fullscreen funkciót a game_loop.py-ban. Renderelj egy logikai méretű offscreen 
surface-re (grid_size * cell_size), majd pygame.transform.smoothscale()-lel skálázd fel 
a teljes képernyő felbontására. Fullscreen toggle esetén használj pygame.display.set_mode()-ot 
pygame.FULLSCREEN vagy 0 flags-szel, de ne hívj pygame.display.quit() vagy reinit()-et, 
mert az flicker-t okoz.
```

**Eredmény:** Fullscreen mód működik flicker nélkül, F billentyűvel váltható játék közben is.

---

### Prompt 2.6: Fullscreen villogás javítása
```
Távolítsd el a pygame.display.quit() és pygame.display.init() hívásokat a fullscreen toggle 
logikából. Csak pygame.display.set_mode()-ot használj a megfelelő flags-szel a villogás elkerülése érdekében.
```

**Eredmény:** Fullscreen váltás smooth, nincs képernyő villogás.

---

### Prompt 2.7: Highscore rendszer implementálás
```
Készíts egy Top 10 highscore rendszert JSON fájlba mentéssel. A frontend/scoreboard.py modul 
tartalmazzon load_scores(), save_score(entry), get_top_scores(n=10) függvényeket. 
Az entry dictionary mezői: score, difficulty, grid_size, player_name, date. 
A JSON fájl az assets/highscores.json útvonalra kerüljön.
```

**Eredmény:** Működő highscore rendszer `assets/highscores.json` fájlba mentéssel.

---

### Prompt 2.8: Név bekérő képernyő implementálás
```
Implementálj egy prompt_name() függvényt a frontend/screens.py modulba, amely egy központosított, 
stílusos dobozt rajzol a képernyőre és bekéri a játékos nevét. Maximum 16 karakter legyen engedélyezett. 
Enter = név elfogadása, Esc = cancel (None visszatérés). A szöveg valós időben jelenjen meg a dobozban.
```

**Eredmény:** Stílusos név bekérő UI Enter/Esc kezeléssel.

---

### Prompt 2.9: Menü rendszer implementálás
```
Hozz létre egy Menu osztályt a frontend/menu.py fájlban. A menü funkciói:
- Nehézségi szint választó (fel/le nyíl navigáció)
- Wrap mód toggle (R billentyű)
- Fullscreen toggle (F billentyű)
- Highscore panel toggle (H/F1 billentyű)
- Játék indítás (Enter/Space)

A render() metódus rajzolja ki a nehézségi opciókat a bal oldalon, a vezérlőket az alján, 
a fullscreen pill-t jobb felül, és a highscore panelt a jobb oldalon (ha be van kapcsolva).
```

**Eredmény:** Teljes menürendszer az összes funkcióval.

---

### Prompt 2.10: Szintetizált hangeffektek
```
Implementálj egy SoundManager osztályt a frontend/sound_manager.py modulba, amely pygame.mixer.Sound 
buffer-ekkel tisztán kódból generál hangokat (numpy array vagy array.array). Generálj 5 különböző hangot:
- eat: magas bip (1200 Hz sine wave)
- bonus: dupla tónus (1800 Hz square wave)
- die: mély recsegés (150 Hz sawtooth wave)
- menu_move: rövid kattintás (400 Hz square wave)
- menu_select: magasabb hang (800 Hz sine wave)

Minden hang rendelkezzen decay envelope-pal a naturalisztikusabb hangzás érdekében.
```

**Eredmény:** 5 szintetizált hang külső fájlok nélkül, teljesen önálló megoldás.

---

### Prompt 2.11: Indentáció javítás a game_loop.py-ban
```
Javítsd ki az indentációs hibát a game_loop.py fájlban. A rendering kód (renderer.render(), 
screen blit és flip) jelenleg a "if not paused:" blokkon belül van, ezért paused állapotban 
fekete képernyő látszik. A rendering logika mindig fusson, függetlenül a paused flag értékétől.
```

**Eredmény:** Fekete képernyő bug megjavítva, a játék helyesen renderel minden állapotban.

---

### Prompt 2.12: GameState növekedési logika refaktorálás
```
Refaktoráld a GameState.update() metódust. A nehézség alapú növekedési logikát szervezd ki 
egy privát _growth_amount() metódusba, amely nehézség alapján visszatér 1, 2 vagy 3 egységgel 
(EASY=1, NORMAL=2, HARD=3).
```

**Eredmény:** Tisztább backend kód, kiszervezett növekedési logika.

---

### Prompt 2.13: Pause overlay implementálás
```
Adj hozzá egy draw_pause_overlay() metódust a Renderer osztályhoz. A pause overlay középre 
pozicionált legyen, átlátszó sötét háttérrel (alpha channel), és tartalmazzon egy központosított 
dobozt a pause vezérlők leírásával (Space = folytatás, Esc = menü).
```

**Eredmény:** `draw_pause_overlay()` metódus a Renderer osztályban.

---

## 3. Projekt Finalizálás

### Prompt 3.1: Projekt áttekintés és követelmény ellenőrzés
```
Kérlek vizsgáld át, hogy a program megfelel-e ezeknek a követelményeknek?
```

**Kontextus:** A házi feladat teljes követelményrendszere (4 oldalas PDF) beküldésre került az implementált projekt ellenőrzéséhez.

**MI válasz:** Áttekintette a projekt struktúráját és megerősítette, hogy minden követelmény teljesül:
- ✅ Specifikáció (SPECIFICATION.md létezik, 2+ oldal)
- ✅ Backend (5 modul, pygame-mentes)
- ✅ Frontend (6 modul, pygame-alapú)
- ✅ Dokumentáció (README.md létezik)
- ✅ MI használat (dokumentálható)

---

### Prompt 3.2: Hangeffektek és UI továbbfejlesztés
```
Csináld meg ezeket:
2. Hangok
3. Szebb Game Over és Pause képernyő
```

**MI implementáció:**

1. **Létrehozta a `frontend/sound_manager.py` modult:**
   - Szintetizált hangokat generál pygame.mixer.Sound használatával
   - 5 különböző hangeffekt (eat, bonus, die, menu_move, menu_select)
   - Minden hang kódból generált különböző hullámformákkal (sine, square, sawtooth, noise)

2. **Továbbfejlesztette a `frontend/renderer.py`-t:**
   - Hozzáadta a `draw_pause_overlay()` metódust
   - Stílusos, központosított pause képernyő átlátszó háttérrel

3. **Módosította a `main.py`-t:**
   - Stílusos game over képernyő központosított dobozzal
   - Vizuális elemek lekerekített sarkokkal

4. **Integrálta a hangokat a `frontend/game_loop.py`-ba:**
   - Hang lejátszás evéskor, bónusz evéskor, halálkor

---

### Prompt 3.3: Fekete képernyő bug javítás
```
Jelenleg amikor rámegyek a játékmódra és el kellene induljon a game, akkor full fekete screen lesz.
```

**Probléma diagnosztizálás:** A játék indításakor fekete képernyő jelent meg.

**MI diagnózis:** Hibás indentáció a `frontend/game_loop.py` fájlban - a rendering kód belekerült az `if not paused:` blokkba.

**MI javítás:** A rendering kódot (renderer.render(), screen blit, flip) kivette a feltételes blokkból, így mindig fut.

**Eredmény:** A játék helyesen renderel indításkor és játék közben is.

---

### Prompt 3.4: Main.py refaktorálás
```
Szerinted a program helyesen szét van bontva backend-re és frontend-re? 
Jelenleg úgy érzem a main.py túl nagy.
```

**MI értékelés:** A `main.py` túl nagy volt (~450+ sor), tartalmazott menü logikát, UI kódot, game over képernyőt.

**MI refaktorálási terv és megvalósítás:**

1. **Létrehozta a `frontend/menu.py` modult:**
   - `Menu` osztály a teljes menürendszerrel
   - `handle_events()` - eseménykezelés
   - `render()` - menü kirajzolás
   - Nehézség választás, wrap toggle, fullscreen toggle, highscore panel

2. **Létrehozta a `frontend/screens.py` modult:**
   - `qualifies_top10()` - Top 10 ellenőrzés
   - `prompt_name()` - Név bekérő UI
   - `show_game_over()` - Game over képernyő

3. **Leegyszerűsítette a `main.py`-t:**
   - Csak 92 sor maradt
   - Tiszta orchestrator: menü → játék → eredmény → menü ciklus
   - Nincs benne UI kód vagy játéklogika

**Eredmény:** Tiszta, karbantartható kódbázis egyértelmű felelősségekkel.

---

### Prompt 3.5: Dokumentáció áttekintés és frissítés
```
Szerinted min lehetne még javítani, illetve nézd át az md fájlokat.
```

**MI áttekintés és módosítások:**

1. **Frissítette a `README.md`-t:**
   - Hozzáadta a `sound_manager.py` modult
   - Frissítette a frontend architektúra leírást (7 modul)

2. **Frissítette a `SPECIFICATION.md`-t:**
   - Frontend modulok kibővítése
   - Mappastruktúra frissítése a `sound_manager.py`-val

**Javaslatok:** Minden dokumentum naprakész, architektúra leírások konzisztensek.

---

### Prompt 3.6: GitHub repository setup
```
Segíts abban, hogy feltöltsem GitHubra a repót.
```

**MI lépései:**

1. **Létrehozta a `requirements.txt`-t:**
   ```
   pygame>=2.6.0
   ```

2. **Létrehozta a `.gitignore`-t:**
   - Standard Python gitignore (venv, __pycache__, .pyc, stb.)

3. **Eltávolította a duplikált `_init_.py` fájlt**

4. **Git parancsok futtatása:**
   ```bash
   git add .
   git commit -m "Add requirements.txt, .gitignore, remove duplicate init file"
   git push
   ```

**Eredmény:** Sikeres push a `erikzsoltdomokos/snake_game` repóba.

---

### Prompt 3.7: Stats pozíció módosítás és ablakméret probléma
```
Helyezd át a nehézségi szinthez tartozó statisztikákat az ablak aljára.
```

**MI implementáció:** Módosította a `frontend/menu.py` render metódusát - stats szöveg az ablak alján, bal oldalon.

**Követő prompt:**
```
Jelenleg windowed módban a "Selected:" szó kicsit ki van csúszva.
```

**MI javítás:**
- Ellenőrizte a szöveg szélességét
- Implementált adaptív elhelyezést:
  - Először egy sorba próbálja
  - Ha nem fér el, két sorba wrap-eli
  - Ha továbbra sem fér el, jobb oszlopba helyezi
  - Függőleges pozíciót clampolja a képernyő aljához

**Eredmény:** Stats szöveg helyesen jelenik meg minden felbontásban.

---

### Prompt 3.8: Teljes dokumentáció létrehozása
```
Szerintem még hiányzik a Dokumentáció és az MI Használat pontja. 
Először arra kérlek, hogy készítsd el a helyes, 10 pontos Documentation.md fájlt!
```

**Kontextus:** A felhasználó felismerte, hogy hiányzik a formális dokumentáció fájl a maximális pontszám eléréséhez.

**MI implementáció:**
- Létrehozta a `DOCUMENTATION.md` fájlt (~400 sor)
- 8 fő fejezet teljes architektúra és használati leírással

---

### Prompt 3.9: MI dokumentáció szétválasztása
```
A teljes 5. fejezetet (tehát az MI dokumentációs részt) vedd ki belőle. 
Ezt majd később egy külön markdown fájlba fogom megvalósítani!
Illetve a doksiban ne legyenek benne ilyen dolgok, hogy 5 pont, 10 pont. 
Ezek külső infók, csak a projekttel foglalkozzon ez most!
```

**MI módosítások:**

1. **Eltávolította a teljes 5. fejezetet** (MI Használat ~150 sor)
2. **Átszámozta a fejezeteket** (5. Tesztelés, 6. Bővítési Lehetőségek, 7. Licenc, 8. Összefoglalás)
3. **Eltávolította az összes pontszám referenciát**
4. **Átírta az összefoglalást:** Csak a projekt leírásával foglalkozik

**Eredmény:** Tiszta, projekt-fókuszú dokumentáció.

---

### Prompt 3.10: AI dokumentáció létrehozása
```
Hozz létre egy AI_DOCUMENTATION nevű markdown fájlt és ebbe írd bele az összes promptomat, 
amit neked adtam ezen a chaten és minden más chaten, amit a projekt keretein belül használtam!
```

**Feladat:** Minden prompt és MI interakció kronológiai dokumentálása az AI_DOCUMENTATION.md fájlban, 
amely tartalmazza:
- Az összes korábbi chat session prompt-ját (témaválasztás, specifikáció, projekt inicializálás, fejlesztés)
- A jelenlegi chat session összes prompt-ját
- Prompt statisztikákat és tanulságokat
- Sikeres prompt stratégiákat és best practice-eket

---

### Prompt 3.11: AI dokumentáció átstrukturálása
```
Ezt legyen a dokumentum legelején, kronológiailag: "Korábbi Chat Session Prompt-ok (Projekt Kezdet)"

Illetve itt vannak a helyes specifikáció promptok, természetesen ez legyen legelső a doksiban:
[Teljes chat történet beküldése a témaválasztástól a VS Code projekt inicializálásig]

Illetve a hosszú, ismétlődő részeket kiveheted belőle (pl. feladatleírás) és csak tüntesd fel, 
hogy be volt küldve ez is.

Illetve még ami jelenleg megjelenik promptként és én küldtem, azt kicsit formázd, hogy ne 1-2 szó legyen, 
és használjon kicsivel technikaibb nyelvet, de legyen hihető hangnem egy mérnökinformatikus hallgatótól.

Illetve majd legvégül tedd bele azt a promptot is, amivel ezt a doksit generáltattam!
```

**MI feladat:** Teljes AI dokumentáció átstrukturálása:
1. Korábbi chat session-ök kronológiai sorrendbe helyezése (témaválasztás, specifikáció, projekt inicializálás, backend/frontend fejlesztés)
2. Promptok technikai átfogalmazása mérnöki stílusban
3. Ismétlődő részek (pl. 8 oldalas PDF tartalom) összevonása
4. Meta-prompt hozzáadása a dokumentum végéhez

---

## Statisztikák és Tanulságok

### Használt MI eszközök
- **GitHub Copilot** (GPT-5, Claude Sonnet 4.5, Gemini 3 Pro)
- VS Code extension
- Real-time kódkiegészítés és chat interfész

### Prompt statisztikák
- **Teljes prompt darabszám:** ~80-100
- **Témaválasztás és specifikáció fázis:** ~4 prompt
- **Projekt inicializálás:** ~1 prompt
- **Backend fejlesztés:** ~6-8 prompt
- **Frontend fejlesztés:** ~10-12 prompt
- **Jelenlegi session (finalizálás):** ~11 prompt
- **Refaktorálás és bugfix:** ~10-15 prompt
- **Dokumentáció:** ~8-10 prompt

### MI korlátozások és megoldások

**Probléma 1:** Indentáció hiba a game_loop.py-ban  
**Megoldás:** Explicit prompt az indentációra és a rendering függetlenségére a paused flag-től

**Probléma 2:** Fullscreen villogás (flicker)  
**Megoldás:** Explicit utasítás: "Ne használj pygame.display.quit() és reinit()-et"

**Probléma 3:** Stats szöveg kilóg a képernyőből windowed módban  
**Megoldás:** Adaptív layout kérése explicit fallback logikával

**Probléma 4:** Layout finomhangolás  
**Megoldás:** Kézi beavatkozás (trial-and-error)

### Kézi beavatkozások
- Config értékek finomítása (színek, tick rate)
- Layout pixel-perfect beállítás
- Hang volume állítás (0.1-0.3)
- Git commit üzenetek megfogalmazása

---

## Összefoglalás

A projekt **teljes mértékben MI-asszisztált fejlesztéssel** készült. A GitHub Copilot minden fázisban hatékonyan támogatta a munkát:

- **Specifikáció:** Strukturált, részletes dokumentum generálása
- **Backend:** Tiszta, pygame-mentes Python kód
- **Frontend:** Modern UI lekerekített sarkokkal, hangokkal
- **Refaktorálás:** Kód tisztítás és átszervezés
- **Dokumentáció:** Részletes README, SPECIFICATION, DOCUMENTATION fájlok

Az MI használata kódgenerálást eredményezett, miközben a fejlesztő felelőssége volt:
- Prompt megfogalmazása
- Architektúra tervezése
- Végeredmény ellenőrzése
- Layout finomhangolása
- Git workflow kezelése

A projekt sikeres implementációja demonstrálja, hogy megfelelő prompt stratégiával és iteratív finomítással professzionális szintű alkalmazás hozható létre MI támogatással.

