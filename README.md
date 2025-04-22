This is a multilingual, command‑line weather client. It supports English (`en`), Spanish (`es`) and Latin (`la`) and fetches current weather and wind speed from wttr.in.

### 1. Language Selection
- Prompts until a valid code is entered:
  - `en` – English  
  - `es` – Spanish  
  - `la` – Latin  

### 2. Language‑Specific API Wrappers
After selection, the script binds two functions:

- `get_weather(location)`:  
  - Requests `https://wttr.in/{location}?format=%C+%t`  
  - Returns “Condition + Temperature” (e.g. “☀️  15°C”) or an error message in the chosen language.  

- `get_wind_speed(location)`:  
  - Requests `https://wttr.in/{location}?format=%w`  
  - Returns wind details (e.g. “→↗ 5 km/h”) or an error message in the chosen language.  

### 3. Location Input
- Prompts in the selected language:
  - **English:** `Enter a location: `  
  - **Spanish:** `Ingrese una ubicación: `  
  - **Latin:** `Intra locum: `  
- Echoes back:  
  - **English:** `Your location is: <location>`  
  - **Spanish:** `Su ubicación es: <location>`  
  - **Latin:** `Locus tuus est: <location>`

### 4. Displaying Results
1. **Weather**  
   - Prints:  
     - English: `The weather in <location> is: <weather>`  
     - Spanish: `El clima en <location> es: <weather>`  
     - Latin: `Tempestas in <location> est: <weather>`  

2. **Wind Speed**  
   - Prints:  
     - English: `The wind speed in <location> is: <wind speed>`  
     - Spanish: `La velocidad del viento en <location> es: <wind speed>`  
     - Latin: `Velocitas venti in <location> est: <wind speed>`

3. **Local Time**  
   - Uses `time.localtime()` and `strftime("%H:%M:%S")`  
   - Prints `Local Time: HH:MM:SS`

---
