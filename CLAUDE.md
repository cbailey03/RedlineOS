# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Run the application
python main.py

# Install dependencies
pip install -r requirements.txt

# Format code
black .

# Lint
ruff check .

# Run all tests
python -m pytest tests/

# Run a single test file
python -m pytest tests/test_document.py

# Run a single test by name
python -m pytest tests/test_document.py::test_function_name
```

> Note: `pytest` is not yet in `requirements.txt` — add it under a `[dev]` extra or install separately with `pip install pytest`.

## Architecture

### Entry point and app shell

`main.py` → `redlineos/app.py` (`Application`, a `QMainWindow`) → `redlineos/ui/main_window.py` (`MainWindow`, a `QWidget` set as the central widget).

`MainWindow` owns two top-level children stacked vertically: the `Ribbon` and the `PdfCanvas`. It wires their signals together (e.g. `ribbon.open_requested` → `canvas.load_document`).

MuPDF stderr output is suppressed at startup in `main.py` via `fitz.TOOLS.mupdf_display_errors(False)` to silence non-fatal structural warnings from malformed PDFs.

### Ribbon (`redlineos/ui/ribbon/`)

Custom Office-style ribbon built from four composable classes:

- `RibbonButton` — a `QToolButton` in either `LARGE` (icon above text, 54×62) or `SMALL` (icon left of text, fixed height 22) size.
- `RibbonGroup` — a `QWidget` with a horizontal button row, a hairline separator, and a centered group title at the bottom.
- `RibbonTab` — a `QWidget` with an `QHBoxLayout` of groups separated by vertical lines.
- `Ribbon` — the top-level widget (fixed height 120px). Internally uses a `QTabBar` inside a blue `QWidget` header + a `QStackedWidget` for tab content. Tab switching is wired via `QTabBar.currentChanged → QStackedWidget.setCurrentIndex`.

To add a new ribbon tab: add a `_add_<name>_tab` method in `Ribbon`, call it from `_build_tabs`, and call `_register_tab(title, tab)` at the end.

`Ribbon` emits three signals: `open_requested(Path)`, `save_requested()`, `close_requested()`. The Open button is fully functional (opens a `QFileDialog`). Save and tool buttons are stubs.

### PDF canvas (`redlineos/canvas/`)

`PdfCanvas` is a `QGraphicsView` backed by a `QGraphicsScene`. Pages are rendered as `QGraphicsPixmapItem`s stacked vertically with `PAGE_GAP = 20px` between them.

- `Renderer.render_page(page, zoom)` uses PyMuPDF (`fitz`) to rasterize a page into a `QPixmap` via `QImage(pix.samples, ...)` with `Format_RGB888`.
- Pan is handled by `QGraphicsView.DragMode.ScrollHandDrag`. Zoom is `Ctrl+scroll`, scaling the view transform anchored to the cursor.
- File drops are accepted directly on the canvas (`setAcceptDrops(True)`). Dropping a second PDF closes the first via `fitz.Document.close()`.

### Tool system (`redlineos/tools/`)

`BaseTool` is an ABC with three abstract methods: `on_press`, `on_move`, `on_release`. All drawing and annotation tools subclass it. The canvas is responsible for routing mouse events to the active tool — this wiring is not yet implemented.

### Annotation model (`redlineos/annotations/`)

`BaseAnnotation` is an ABC requiring `to_dict()` and `from_dict()`. Concrete subclasses live in `markup.py` (highlights, comments, stamps), `drawing.py` (freehand, shapes), and `cad.py` (CAD symbols, title blocks). All are stubs — the serialization contract exists but no implementations are written yet.

### Document model (`redlineos/document/`)

`Document`, `Page`, and `Layer` are plain data classes. They are not yet wired into `PdfCanvas` — the canvas currently works directly with `fitz.Document`. The intent is for `Document` to wrap `fitz.Document` and hold the annotation/layer state alongside it.

### I/O (`redlineos/io/`)

`PdfReader.open(path)` returns a `fitz.Document`. `PdfWriter`, `SvgHandler`, and `DxfHandler` are stubs. DXF support uses the `ezdxf` library.

## Key decisions

- **PySide6 over PyQt6** — LGPL license keeps the project AGPL-compatible without forcing GPL on contributors.
- **PyMuPDF over pypdf** — required for page rendering; pypdf cannot rasterize pages.
- **AGPL-3.0 license** — chosen for compatibility with PyMuPDF's AGPL license.
- **Font sizes in stylesheets must use `pt` not `px`** — Qt's px-to-point conversion can produce -1 on some systems, causing `QFont::setPointSize` warnings.
