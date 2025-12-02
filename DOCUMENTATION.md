# Snake Game - Dokumentáció
## Szoftverfejlesztés MI támogatással – Házi feladat

---

## 1. Bevezetés

Ez a dokumentum a Snake játék teljes körű leírását tartalmazza. A projekt célja egy klasszikus Snake játék modern implementációja Python és pygame használatával, ahol a backend és frontend szigorúan el van választva egymástól. A játékot teljes mértékben mesterséges intelligencia (MI) támogatással fejlesztettük, a specifikációtól a tesztelésig.

### 1.1 Projekt célja

- Klasszikus Snake játék élmény biztosítása modern technológiákkal
- Backend-frontend szétválasztás demonstrálása
- Tiszta, karbantartható és bővíthető kódbázis létrehozása
- MI-asszisztált fejlesztési munkafolyamat bemutatása

### 1.2 Célközönség

A játék minden korosztály számára könnyen használható, de a dokumentáció elsősorban a fejlesztőket, kódellenőröket és az oktatási célú értékelést támogatja.

---

## 2. Telepítés és Futtatás

### 2.1 Rendszerkövetelmények

- **Operációs rendszer:** Windows 10/11, macOS 10.14+, Linux (Ubuntu 20.04+)
- **Python verzió:** 3.10 vagy újabb
- **RAM:** Minimum 2 GB
- **Lemezterület:** ~50 MB a projekt és függőségek számára
- **Grafikus környezet:** pygame kompatibilis display

### 2.2 Telepítési lépések

1. **Projekt letöltése:**
   ```bash
   git clone https://github.com/erikzsoltdomokos/snake_game.git
   cd snake_game
   ```

2. **Virtuális környezet létrehozása (ajánlott):**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

3. **Függőségek telepítése:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Játék indítása:**
   ```bash
   python main.py
   ```

### 2.3 Hibaelhárítás

**Probléma:** `ModuleNotFoundError: No module named 'pygame'`  
**Megoldás:** Futtasd újra: `pip install pygame>=2.6.0`

**Probléma:** Fekete képernyő játék indításakor  
**Megoldás:** Ellenőrizd, hogy a grafikus kártya driverei naprakészek-e, vagy próbáld ki ablakos módban (F billentyű a menüben).

**Probléma:** Hang nem szól  
**Megoldás:** A hangok szintetizáltak és automatikusak. Ha nem hallasz hangot, ellenőrizd a rendszer hangerejét és hogy nem némítva van-e a pygame mixer.

---

## 3. Használati Útmutató

### 3.1 Főmenü

A játék indításakor a főmenü fogad, ahol a következő lehetőségek érhetők el:

#### Nehézségi szintek kiválasztása
- **Fel/Le nyíl** vagy **W/S:** Váltás a nehézségi szintek között (Easy, Normal, Hard)
- **Enter** vagy **Space:** Játék indítása a kiválasztott beállításokkal

#### Beállítások
- **R billentyű:** Wrap mód (átjárható falak) be/ki kapcsolása
  - **Ki (alapértelmezett):** Falnak ütközés véget vet a játéknak
  - **Be:** A kígyó átmegy a falakon és a túloldalon jelenik meg
- **F billentyű:** Fullscreen/Windowed mód váltása
  - A beállítás megmarad a játék és menü között is
- **H** vagy **F1:** Top 10 Highscores megjelenítése/elrejtése

#### Kilépés
- **Esc** vagy **Q:** Kilépés az alkalmazásból

### 3.2 Játék közben

#### Irányítás
- **Nyilak (↑ ↓ ← →)** vagy **W A S D:** Kígyó irányítása
- **P:** Szünet (Pause) be/ki kapcsolása
  - Szünet alatt megjelenik egy stílusos overlay a billentyűparancsokkal
- **T:** Téma váltása (Sár/Vibráló színvilág között)
- **F:** Fullscreen mód váltása játék közben is
- **Esc:** Kilépés a menübe (aktuális játék elvész)

#### Játékszabályok

1. **Cél:** Minél több alma megevése a pontszám növeléséért
2. **Növekedés:** Minden alma után a kígyó hosszabbodik
   - Easy: 1 egység növekedés almánként
   - Normal: 2 egység növekedés almánként
   - Hard: 3 egység növekedés almánként
3. **Bónusz étel:** Időnként megjelenik arany színű bónusz étel, amely:
   - Extra pontot ér
   - Csak rövid ideig elérhető (~10-15 másodperc)
   - Eltűnik, ha nem fogyasztod el időben
4. **Game Over feltételek:**
   - **Normál módban:** Falnak vagy saját testnek ütközés
   - **Wrap módban:** Csak saját testnek ütközés (falak átjárhatók)

### 3.3 Eredmények és Highscore

#### Game Over képernyő
Játék végeztével megjelenik egy stílusos overlay a következő információkkal:
- Elért pontszám
- Nehézségi szint és pályaméret
- **R billentyű:** Azonnali újraindítás ugyanazokkal a beállításokkal
- **Bármely más billentyű:** Visszatérés a főmenübe

#### Top 10 Highscore
- Ha az eredményed bekerül a legjobb 10 közé, a rendszer bekéri a nevedet (max 16 karakter)
- A highscore-ok JSON fájlban tárolódnak (`assets/highscores.json`)
- A főmenüben **H** vagy **F1** billentyűvel megtekintheted a Top 10-et:
  - Rang, pontszám, nehézségi szint, pályaméret, játékos neve

---

## 4. Architektúra

### 4.1 Általános felépítés

A projekt követi a **backend-frontend szétválasztás** elvét:

```
┌─────────────────────────────────────────┐
│            main.py (Orchestrator)        │
│  - Menü kezelés                          │
│  - Játék indítás                         │
│  - Score mentés és név prompt            │
└──────────────┬──────────────────────────┘
               │
       ┌───────┴────────┐
       │                │
┌──────▼──────┐  ┌──────▼──────────┐
│   Backend   │  │    Frontend      │
│ (Tiszta     │  │  (pygame alapú)  │
│  Python)    │  │                  │
└─────────────┘  └──────────────────┘
```

### 4.2 Backend struktúra

A backend **NEM használ pygame-et**, tisztán Python logika, így könnyen tesztelhető és újrafelhasználható.

#### `backend/state.py`
- **Szerepe:** Központi játékállapot kezelés
- **Főbb osztályok/metódusok:**
  - `GameState` dataclass: tárolja a pályaméretet, nehézséget, kígyót, ételeket, pontszámot, wrap mód flag-et, RNG seed-et
  - `GameState.new(...)`: Új játék inicializálása
  - `GameState.update()`: Tick-alapú frissítés – mozgás, ütközések, evés, növekedés
  - `_growth_amount()`: Nehézség alapú növekedési ráta

#### `backend/snake.py`
- **Szerepe:** Kígyó modellje
- **Fő funkciók:**
  - `Snake` dataclass: test koordináták listája, irány, várakozó növekedés
  - `set_direction(new_dir)`: Irányváltás kezelése, megelőzi a 180°-os fordulatot
  - `next_head()`: Következő fej pozíció kiszámítása
  - `move()`: Mozgás végrehajtása (fej hozzáadása, farok eltávolítása vagy növekedés)
  - `grow(amount)`: Várakozó növekedés számláló növelése

#### `backend/food.py`
- **Szerepe:** Étel generálás
- **Funkció:** `spawn_food(grid_size, occupied)` – véletlen szabad cellát keres, ahol nincs kígyó

#### `backend/collision.py`
- **Szerepe:** Ütközésdetektálás
- **Funkciók:**
  - `is_out_of_bounds(pos, grid_size)`: Falütközés ellenőrzés
  - `hits_self(head, body)`: Önmagába harapás ellenőrzés

#### `backend/difficulty.py`
- **Szerepe:** Nehézségi szintek definíciója
- **Enum:** `Difficulty.EASY`, `Difficulty.NORMAL`, `Difficulty.HARD`
- **Funkció:** `get_tick_rate(difficulty)` – FPS visszaadása (pl. EASY=8, NORMAL=12, HARD=18)

### 4.3 Frontend struktúra

A frontend felelős a **vizualizációért, felhasználói bemenetért, hangokért és a UI elemekért**.

#### `frontend/menu.py`
- **Szerepe:** Főmenü rendszer
- **Menu osztály:**
  - `handle_events()`: Billentyűzet és egér események (nehézség választás, beállítások, játék indítás)
  - `render(screen, fullscreen)`: Teljes menü kirajzolása (nehézségi opciók, vezérlők listája, fullscreen pill, highscore panel)
  - `get_selected_difficulty()`, `get_grid_size()`: Aktuális beállítások lekérdezése

#### `frontend/screens.py`
- **Szerepe:** Overlay képernyők (game over, név prompt)
- **Funkciók:**
  - `qualifies_top10(existing_scores, new_score, n=10)`: Ellenőrzi, hogy a score Top 10-es-e
  - `prompt_name(screen, score, difficulty, grid_size)`: Név bekérő UI (max 16 karakter, Enter/Esc)
  - `show_game_over(screen, score, difficulty, grid_size)`: Stílusos game over overlay, R = restart, egyéb = menü

#### `frontend/renderer.py`
- **Szerepe:** Játék vizualizáció
- **Renderer osztály:**
  - Két téma: `mud` (sár) és `vibrant` (élénk)
  - `draw_grid(grid_size)`: Sakktábla mintás háttér
  - `draw_snake(body)`: Kígyó kirajzolása lekerekített sarkokkal, fejjel és testtel különböző színnel
  - `draw_food(food)`: Alma alakú étel (ellipszis + levél + árnyék)
  - `draw_hud(score, paused)`: Pontszám és szünet jelzés kiírása
  - `draw_pause_overlay()`: Szünet képernyő doboza központosítva
  - `render(state, paused)`: Teljes képkocka kirajzolása
  - `toggle_theme()`: Témaváltás

#### `frontend/input_handler.py`
- **Szerepe:** Billentyűzet bemenet kezelése
- **InputHandler osztály:**
  - `process_events(state, paused)`: pygame events feldolgozása, irányváltás, szünet, kilépés
  - Visszatérési érték: `(running, paused)` tuple

#### `frontend/game_loop.py`
- **Szerepe:** Játék fő ciklusa
- **Funkció:** `run_game(grid_size, difficulty, cell_size, wrap_edges, start_fullscreen)`
  - Inicializálja a pygame ablakot, órát, renderert, input handlert, sound managert
  - Offscreen `render_surface`-re rajzol (logikai méret), majd skálázza fullscreen/windowed méretre
  - Tick-alapú `state.update()` hívás és `renderer.render(state, paused)`
  - Hangeffektek lejátszása (evés, ütközés)
  - Fullscreen toggle F billentyűvel játék közben
  - Visszatérés: `(score, fullscreen)` tuple

#### `frontend/sound_manager.py`
- **Szerepe:** Szintetizált hangeffektek
- **SoundManager osztály:**
  - `_generate_wave(frequency, duration, volume, wave_type, decay)`: Hang generálás (sine, square, sawtooth, noise)
  - `_generate_sounds()`: 5 hang előállítása:
    - `eat`: magas "bip" (1200 Hz, rövid)
    - `bonus`: dupla tónus bónuszhoz (1800 Hz)
    - `die`: mély recsegés (150 Hz, sawtooth)
    - `menu_move`: rövid kattintás menü navigációhoz
    - `menu_select`: magasabb hang kiválasztáskor
  - `play(name)`: Hang lejátszása név alapján
  - **Előny:** Nincs szükség külső WAV fájlokra, minden tisztán kódból generált

#### `frontend/scoreboard.py`
- **Szerepe:** Highscore perzisztencia
- **Funkciók:**
  - `load_scores()`: JSON betöltés `assets/highscores.json`-ből
  - `save_score(entry)`: Új score hozzáadása és mentés (dátum, név, pontszám, nehézség, grid)

### 4.4 Főprogram (`main.py`)

A `main.py` **csak orchestrációt** végez, nem tartalmaz üzleti logikát vagy UI kódot (92 sor):

1. **Inicializáció:** pygame init, Menu osztály példányosítás, fullscreen beállítás
2. **Menü loop:**
   - `menu.handle_events()`: eseménykezelés
   - `menu.render(screen, fullscreen)`: kirajzolás
   - Fullscreen toggle kezelés (billentyű és egér)
3. **Játék indítás:**
   - `run_game(...)` hívás a kiválasztott beállításokkal
   - Visszatérés után a score és fullscreen state kezelése
4. **Top 10 ellenőrzés és név prompt:**
   - `qualifies_top10(scores, score)` – ha igen, `prompt_name(...)` hívása
   - `save_score(...)` – eredmény mentése (névvel vagy anélkül)
5. **Game Over képernyő:**
   - `show_game_over(...)` – ha R = restart, újraindítás azonos beállításokkal
6. **Kilépés:** pygame.quit()

### 4.5 Adatáramlás

```
Felhasználó input (billentyűzet)
       ↓
InputHandler (frontend)
       ↓
GameState.update() (backend) ← Tiszta logika, pygame-mentes
       ↓
Renderer.render(state) (frontend)
       ↓
pygame.display (képernyő)
```

**Előnyök:**
- Backend unit tesztelhető pygame nélkül
- Frontend könnyen cserélhető (pl. terminál UI, web frontend)
- Világos felelősségek

---

## 5. Tesztelés

### 5.1 Manuális tesztelés

A játékot minden nagyobb commit után manuálisan teszteltük:

1. **Funkcionális tesztek:**
   - Nehézségi szintek (EASY, NORMAL, HARD) működése
   - Wrap mód be/ki kapcsolása és helyes viselkedés
   - Fullscreen/windowed váltás flicker nélkül
   - Bónusz étel megjelenése és időzítése
   - Highscore mentés és név prompt
   - Pause overlay
   - Témaváltás

2. **UI/UX tesztek:**
   - Menü elemek elhelyezkedése fullscreen és windowed módban
   - Stats szöveg nem lóg ki a képernyőből
   - Game over képernyő központosítva
   - Highscore panel jobb oldalt, rendezett

3. **Hangok tesztelése:**
   - Evés hang lejátszódik alma megevésekor
   - Bónusz hang lejátszódik bónusz étel megevésekor
   - Ütközés hang játék végekor
   - Menü navigáció hangjai (move, select)

### 6.2 Hibajavítások

**Hiba:** Fekete képernyő játék indításakor  
**Ok:** `if not paused` blokkba került a rendering  
**Javítás:** Indentáció javítása, rendering mindig fut

**Hiba:** Stats szöveg kilóg windowed módban  
**Ok:** Nem volt szélesség ellenőrzés  
**Javítás:** Wrap két sorba, ha túl széles

**Hiba:** Fullscreen villogás toggle-nél  
**Ok:** display reinit  
**Javítás:** Csak `set_mode` hívás flags-szel

### 6.3 Automatizált tesztek (opcionális bővítés)

Jelenleg a backend könnyen unit tesztelhető lenne (pygame-mentes), de a projektben nem implementáltunk teszteket. Példa, amit hozzá lehetne adni:

```python
# tests/test_snake.py
def test_snake_move():
    snake = Snake(body=[(5, 5), (5, 4), (5, 3)], direction=(0, 1), movement=0, growth=0)
    snake.move()
    assert snake.body[0] == (5, 6)  # Fej előre mozgott

def test_collision_wrap():
    state = GameState.new((10, 10), Difficulty.EASY, wrap_edges=True)
    state.snake.body[0] = (-1, 5)
    # Wrap után (9, 5) lesz
    # ...
```

---

## 6. Bővítési Lehetőségek

A projekt könnyen bővíthető a következő funkciókkal:

1. **Multiplayer mód:** Két kígyó azonos pályán, split-screen vagy online
2. **Power-up-ok:** Lassítás, sebességnövelés, átlátszóság (ghost mode)
3. **Pályaszerkesztő:** Akadályok elhelyezése a pályán
4. **Leaderboard szerver:** Online highscore lista
5. **Mentés/betöltés:** Játék állapot mentése és folytatása
6. **Teljesítmény statisztikák:** Átlagos pontszám, leghosszabb kígyó, játékidő
7. **Mobil port:** Pygame alternatíva (Kivy, PyQt) vagy natív mobil (Kotlin/Swift)

---

## 7. Licenc és Források

### 7.1 Licenc
Ez a projekt oktatási célokra készült, és szabadon felhasználható, módosítható.

### 7.2 Felhasznált technológiák
- **Python 3.11** – [https://www.python.org/](https://www.python.org/)
- **pygame 2.6.1** – [https://www.pygame.org/](https://www.pygame.org/)
- **GitHub Copilot** – [https://github.com/features/copilot](https://github.com/features/copilot)

### 7.3 Fejlesztő
- **Név:** Erik Zsolt Domokos
- **GitHub:** [https://github.com/erikzsoltdomokos](https://github.com/erikzsoltdomokos)
- **Projekt repo:** [https://github.com/erikzsoltdomokos/snake_game](https://github.com/erikzsoltdomokos/snake_game)

---

## 8. Összefoglalás

Ez a Snake játék projekt bemutatja, hogyan lehet modern Python és pygame használatával egy teljes, professzionális szintű alkalmazást létrehozni. A backend-frontend szétválasztás, a tiszta architektúra és a részletes dokumentáció mind hozzájárulnak ahhoz, hogy a projekt ne csak működőképes, hanem karbantartható és bővíthető is legyen.

A projekt sikeres megvalósítása során a következő területeket implementáltuk:
- Tiszta backend logika pygame-mentes környezetben
- Modern, felhasználóbarát frontend vizuális elemekkel
- Hangeffektek szintetizált generálással
- Többféle nehézségi szint és játékmód
- Highscore rendszer adatmentéssel
- Fullscreen és windowed támogatás
