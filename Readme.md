# Sudoku

## Vorgehen
1. Sudoku-Aufbau (Skalierbarkeit -> 3x3 -- 4x4 -- 5x5 ...)
1. Sudoku-Problem erstellen
    * Random Lsg. und prüfen ob lösbar
    * Korrekte Lsg. erstellen (Verwendung von Code scnipseln für den späteren Sudoku-Löser)
3. Sudoku Lösen
    * Alg. 1: Brute Force & Backtracking
    * Alg. 2: alle möglichen merken -> gegeneinander ausschließen
    * Alg. 3: ILP / SMT
    * Alg. 4: Brute Force & dynamisches Backtracking
    * Alg. 5: Exact Cover (Mathematische Lösung)

## Backend
* Sudoku-Feld Speicherung
    * Eine Einheit (Liste von Listen): 3x3 (4x4 ...) Feld
    * Sudoku (Liste von Listen): 3x3 (4x4 ...) an Einheiten
    * Dictionary oder Array -> Geschwindigkeit oder Lesbarkeit im Code

## Frontend