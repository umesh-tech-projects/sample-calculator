## Application overview

Simple desktop calculator built with Python and tkinter. It performs basic arithmetic, supports a few utility functions, and provides both mouse and keyboard input with a clean, color‑coded UI.

## Application features  

- **Basic arithmetic**: `+`, `−`, `×`, `÷`
- **Functions**: `C` (clear), `±` (sign change), `%` (percentage), `.` (decimal), `=` (evaluate)
- **Keyboard support**: Digits `0-9`, `.`, `+ - * /`, `Enter`, `Esc`, `c`
- **Error handling**: Division by zero and invalid operations display `Error`
- **Display formatting**: 12‑character display; trims trailing `.0` where applicable
- **Memory (MC)**: Clears internal memory placeholder and display

## Requirements for the application

- Python 3.6+
- No external packages (uses the standard library and tkinter)

## Installation & Setup

1. Ensure Python is installed: `python --version`
2. If needed, install from `https://www.python.org/downloads/`
3. Download/clone this project to your machine

## File Structure

```
sample calculator/
├── calculator.py      # Main tkinter application and logic
├── requirements.txt   # (empty/placeholder; tkinter ships with Python)
└── README.md          # This file
```

## How to run & use

1. Open Command Prompt or PowerShell
2. Navigate to the project directory:
   ```bash
   cd "C:\Users\Umesh M\Documents\Cursor projects\python projects\sample calculator"
   ```
3. Launch the app:
   ```bash
   python calculator.py
   ```
4. Use the on‑screen buttons or your keyboard:
   - Numbers: `0‑9`, decimal: `.`
   - Operators: `+`, `−`, `×`, `÷` (keyboard: `+`, `-`, `*`, `/`)
   - Evaluate: `=` or `Enter`
   - Clear: `C` or `Esc`/`c`
   - Sign: `±`, Percent: `%`, Memory Clear: `MC`

## From the technical POV

This app is a single‑window tkinter GUI with one main class `Calculator` orchestrating state, UI, and event handling.

- **Entry point**: `main()` creates a `tk.Tk()` root, instantiates `Calculator(root)`, then calls `root.mainloop()` to start the tkinter event loop.
- **State model** (instance attributes):
  - `current`: string of the number shown on the display (user input/result)
  - `total`: float accumulator holding the left operand when an operator is chosen
  - `operator`: one of `+`, `−`, `×`, `÷` or empty when none is pending
  - `result`: boolean indicating last action produced a finalized result
  - `input_value`: boolean flag indicating the next input will start fresh (present for clarity; write path uses `current` and `result` flags)
  - `memory`: numeric placeholder for memory features (currently only cleared via `MC`)
- **UI composition**:
  - Display: `tk.Label` inside a top `tk.Frame` with right‑aligned text
  - Buttons: 5×4 grid of `tk.Button` placed in a `tk.Frame`, color‑coded by role
  - Grid weights ensure even resizing inside the button frame
- **Event routing**:
  - Mouse: All buttons call `button_click(char)` which dispatches to typed handlers
  - Keyboard: Root binds `<Key>` to `key_press(event)`; maps `+ - * /` to `+ − × ÷`, supports `Enter`, `Esc`, `c`
- **Core handlers**:
  - `number_press(num)`: Appends digit to `current`; resets after a result
  - `decimal_press()`: Adds one `.` if absent; resets after a result
  - `operator_press(op)`: If an operator is already pending and there is a new right operand, it resolves first via `equals_press()`; then stores `total=float(current)`, sets `operator=op`, resets `current` to `"0"`
  - `equals_press()`: Applies the pending operator between `total` and `float(current)`; sets `current` to a formatted string, clears `operator`, flags `result=True`
  - `clear()`: Resets `current`, `total`, `operator`, `result`
  - `plus_minus()`: Toggles sign of `current`
  - `percentage()`: Divides `current` by 100
  - `memory_clear()`: Resets `memory` and sets `current` to `"0"`
- **Formatting & constraints**:
  - Display trimmed to 12 characters in `update_display()`
  - Integer results are rendered without `.0` (e.g., `6.0` → `6`)
  - Division by zero sets `current` to `"Error"` and returns early

Performance is trivial given the UI’s size; responsiveness relies on tkinter’s event loop, which remains unblocked because operations are simple and synchronous.

## From the developer POV

This section explains code structure and how to extend or modify the app.

- **Class design**:
  - `Calculator` encapsulates both presentation and logic. For larger apps, consider splitting view (widgets) and controller (logic/state) into separate classes/modules.

- **Widget creation**:
  - `create_buttons()` declares a 2D `buttons` layout and loops to create/configure `tk.Button` widgets with appropriate colors and a shared `command` callback.
  - Button callbacks use `lambda t=text: self.button_click(t)` to capture each button’s label.

- **Input pipeline**:
  - All inputs normalize into a small set of handler methods. This centralization simplifies validation and formatting (e.g., single decimal logic, sign toggling, display truncation).

- **Computation flow**:
  - Selecting an operator captures the left operand (`total=float(current)`) and defers computation until `=` or a subsequent operator press.
  - Pressing a second operator triggers eager evaluation (`equals_press`) to support chained operations like `2 + 3 × 4` (left‑associative in this implementation).

- **Error handling**:
  - Guarded division by zero; other failures fall back to setting `current="Error"`.
  - You may replace broad `except:` with specific exceptions (`ValueError`, `ZeroDivisionError`) for clarity.

- **Formatting decisions**:
  - `update_display()` enforces a 12‑character limit to keep UI tidy.
  - Integer results show without a decimal part to improve readability.

- **Keyboard mapping**:
  - `key_press` reads `event.char` and `event.keysym`, mapping raw keys (`+ - * /`) to UI symbols (`+ − × ÷`).
  - Duplicated handling of `Enter` via `=`/`Return` ensures reliability across platforms.

- **Extending features**:
  - Memory functions: Add `MR` (recall), `M+` (add), `M−` (subtract). Store/read from `self.memory` and update display/state accordingly.
  - Scientific ops: Add buttons and handlers for `sqrt`, `pow`, etc. Keep the same dispatch pattern in `button_click`.
  - Input polish: Implement backspace, thousands separators, or longer display area.
  - Validation: Replace broad exceptions; add unit tests around handlers for arithmetic and formatting.

- **Structure tips for refactors**:
  - Extract a small `CalculatorState` dataclass for `current`, `total`, `operator`, `result` to make logic testable without tkinter.
  - Separate `view.py` (widgets/layout) from `controller.py` (handlers/logic) so UI changes don’t affect logic tests.

---

Enjoy your calculator! 🧮