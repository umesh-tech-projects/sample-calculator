### Application overview
Simple, modern-looking desktop calculator built with Python and Tkinter. It supports basic arithmetic, percentage, sign toggle, keyboard input, and a clean responsive layout.

### Application features
- **Basic operations**: addition, subtraction, multiplication, division
- **Percentage**: quick percent calculation of the current value
- **Sign toggle (±)**: switch between positive and negative values
- **Clear (C)**: reset the current input and state
- **Keyboard support**: digits, decimal, operators (+, -, *, /), Enter/Return, Escape
- **Error handling**: graceful handling of division by zero and bad input
- **Consistent UI**: themed display and buttons with grid-based resizing

### Requirements for the application
- **Python**: 3.8+ recommended (3.6+ should work)
- **Tkinter**: ships with most standard Python distributions
- No third-party packages are required

If Tkinter is missing on your system, install the OS-specific Tk packages (on Windows it’s included with python.org installers; on Linux, install your distro’s Tk package).

### Installation & Setup
1. Ensure Python 3.8+ is installed.
2. Clone or download this repository to your machine.
3. (Optional) Create and activate a virtual environment.
4. Review `requirements.txt` (no external deps needed).

### File Structure
```
sample calculator/
  ├─ calculator.py        # Tkinter GUI application
  ├─ requirements.txt     # Notes on dependencies (built-in only)
  ├─ README.md            # This documentation
  └─ app_description.txt  # Project description (optional notes)
```

### How to run & use
- From a terminal in the project directory, run:
  ```bash
  python calculator.py
  ```
- Click buttons or use the keyboard:
  - Digits 0-9 and `.` for decimal
  - Operators: `+`, `-`, `*`, `/`
  - Enter/Return for equals, `Esc` or `c` to clear
- Use `±` to toggle sign and `%` for percentage.

### From the technical POV
- **Stack**: Python + Tkinter only (no external libraries)
- **Architecture**:
  - `Calculator` class encapsulates UI construction, state, and event handlers
  - Display uses a `tk.Label`; buttons are `tk.Button` arranged via `grid`
  - Keyboard events are bound to the root window and mapped to calculator actions
- **State management**:
  - `current`: string of current input/display
  - `total`: running total for operations
  - `operator`: current pending operator
  - `result`: flag to manage post-equals input behavior
- **UX details**:
  - Window briefly set top-most to avoid hidden launch
  - Display trims overly long strings for readability
- **Error handling**: division by zero guarded; unexpected callback errors surfaced with a dialog

### From the developer POV
- **Entry point**: run `main()` in `calculator.py`
- **Extensibility**:
  - Add new buttons in `create_buttons()` and map their actions in `button_click()`
  - Implement the behavior in a dedicated method (e.g., `square_root()`) and update the display via `update_display()`
  - For keyboard mappings, update `key_press()` (include symbol mapping if needed)
- **Styling**: tweak colors/fonts in `button_config`, display `Label`, and container frames
- **Testing**: manual UI testing is sufficient for this scope; for logic isolation, consider extracting pure functions for unit tests
- **Dependencies**: keep it zero-dependency; Tkinter is included with standard Python installs


