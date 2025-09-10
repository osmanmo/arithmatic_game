# Arithmetic Playground (Child-Friendly Visual Math)

A colorful, child-friendly Streamlit app to help kids visualize addition, subtraction, multiplication, and division. Instead of quizzes, the app focuses on intuitive illustrations:

- Addition: combine objects and hop on a number line
- Subtraction: take away objects and hop backwards on a number line
- Multiplication: build a rows × columns array and skip-count on a number line
- Division: make equal groups and see remainders (division as grouping)

## Quick Start

### 1) Create and activate a virtual environment (recommended)

```bash
python3 -m venv .venv
source ./.venv/bin/activate
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Run the app

```bash
streamlit run app.py
```

Then open the URL that appears (usually `http://localhost:8501`). Use the sidebar or page links to navigate between operations.

## What Kids Will See

- Bright colors, big friendly text, and emojis for objects (🍎 🍏 ⭐ 🟢)
- Live sliders to change numbers and instantly update visuals
- Division as grouping, with clear groups and remainder highlighted
- Multiplication arrays that show rows × columns clearly
- Number line hops with curved arrows forward/backward

## Project Structure

```
arithmatic_game/
├─ app.py                      # Home page and navigation
├─ visuals.py                  # Reusable drawing helpers (matplotlib)
├─ pages/
│  ├─ 1_Addition.py           # Combine objects & number line
│  ├─ 2_Subtraction.py        # Take-away & number line (backwards)
│  ├─ 3_Multiplication.py     # Array model & skip counting
│  └─ 4_Division.py           # Grouping model with remainder
├─ .streamlit/
│  └─ config.toml             # Theme
├─ requirements.txt
└─ README.md
```

## Tips for Grown-Ups

- Encourage kids to explain what they see: “How many groups?”, “How many are left?”
- Try smaller and larger numbers to explore patterns.
- Use the step controls on Division and Multiplication pages to reveal ideas gradually.

## Compatibility

- Python 3.9+
- Streamlit 1.28+

If you run into issues, try upgrading pip (`python -m pip install --upgrade pip`) and reinstalling requirements.

Enjoy learning together!
