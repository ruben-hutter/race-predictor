# Race Pace Predictor

This script allows you to calculate your predicted race pace based on a given distance and a predicted time (e.g., from Garmin). It supports common race distances as well as custom inputs.

## Features
- Supports predefined race distances: 5K, 10K, Half Marathon, Marathon.
- Allows custom distance input.
- Accepts predicted time in HH:MM:SS or MM:SS format.
- Calculates pace in both minutes per kilometer (min/km) and minutes per mile (min/mile).

## Usage
Run the script from the terminal:

```sh
python3 main.py
```

Follow the prompts to:
1. Select a race distance or enter a custom distance.
2. Enter your predicted time.
3. View the calculated pace.

### Example Run
```plaintext
Enter the distance you would like to predict your pace for:
1. 5k
2. 10k
3. Half Marathon
4. Marathon
5. Custom Distance
Enter your selection: 2
Enter your predicted time for 10k (HH:MM:SS) or (MM:SS): 50:00
Pace: 5:00 min/km
Pace: 8:03 min/mile
```

## Requirements
- Python 3.6 or later

## Future Improvements
- Graphical interface or web-based calculator.
- Get data from Garmin API directly.

