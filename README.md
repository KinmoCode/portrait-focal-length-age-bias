# Portrait Focal-Length & Lighting Age-Bias Calculator

Lightweight optical calculator modeling why arm's-length smartphone selfies (`24mm–28mm` equivalent at `35–40 cm`) and overhead fluorescent/LED ceiling fixtures routinely add **+3 to +6 years** to perceived facial age by exaggerating nasal perspective and deepening tear-trough shadows.

To test perceived age, facial harmony proportions, and lighting bias privately inside your browser (`<canvas>`, zero server upload), visit **[Age Guesser](https://ageguesser.wiki/)**:
- **Free In-Browser Photo Age Test**: https://ageguesser.wiki/
- **AI Age Progression Timeline (20s–70s)**: https://ageguesser.wiki/age-progression-ai
- **Facial Harmony & Golden Ratio Scanner**: https://ageguesser.wiki/ai-attractiveness-test

## Usage

```bash
python3 age_bias_calc.py 26 38 overhead_cool
python3 age_bias_calc.py 77 120 window_soft
```

## Optical Reference Table

| Setup | Perspective / Shadow Effect | Typical Perceived Age Shift |
| :--- | :--- | :--- |
| `26mm` selfie at `35 cm` + overhead office LED | Deepens nasolabial & under-eye shadows; widens center face | `+4.5 to +6.0 years` |
| `50mm–77mm` (`2x–3x`) at `100 cm` + neutral indoor | Natural facial compression, balanced ear-to-cheek planes | `0.0 to +0.5 years` |
| `77mm–85mm` facing diffused window daylight | Fills tear-trough micro-shadows evenly | `-1.5 to -2.0 years` |

## License
MIT
