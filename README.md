# RedlineOS

A free and open-source PDF editor built with Python and PySide6, designed for engineers, architects, and technical professionals who need powerful markup, drawing, and CAD-style annotation tools — without the licensing cost.

---

## Features

### Advanced Markup & Annotation
- Highlight, underline, and strikethrough text
- Add comments, sticky notes, and stamps
- Redline markup with color-coded review layers
- Measurement and callout annotations

### Line Drawing & Freehand Tools
- Freehand pen and pencil tools
- Geometric shape drawing (lines, arcs, rectangles, circles, polygons)
- Snap-to-grid and snap-to-object support
- Adjustable stroke width, color, and opacity

### CAD-Style Templates & Symbols
- Engineering and architectural symbol libraries
- Title block templates (ANSI, ISO, custom)
- Reusable annotation blocks and stamps
- Layer management for organized markup

### Import & Export
- Open and save PDF files
- Export to PDF, SVG, and DXF
- Import SVG and DXF overlays onto PDF pages
- Flatten annotations to a permanent layer or keep them editable

---

## Getting Started

### Requirements

- Python 3.13+
- PySide6
- PyMuPDF
- ezdxf

### Installation

```bash
git clone https://github.com/cbailey03/RedlineOS.git
cd RedlineOS
pip install -r requirements.txt
python main.py
```

> **Note:** Package distribution via PyPI and installers for Windows/macOS/Linux are planned for a future release.

---

## Project Structure

```
RedlineOS/
├── main.py                          # Entry point
├── requirements.txt
├── pyproject.toml
├── redlineos/
│   ├── app.py                       # QMainWindow setup
│   ├── ui/
│   │   ├── main_window.py
│   │   ├── toolbar.py
│   │   ├── panels/
│   │   │   ├── layers_panel.py
│   │   │   ├── properties_panel.py
│   │   │   └── symbol_library_panel.py
│   │   └── dialogs/
│   │       ├── export_dialog.py
│   │       └── settings_dialog.py
│   ├── canvas/
│   │   ├── pdf_canvas.py            # Main drawing surface widget
│   │   ├── renderer.py              # PyMuPDF → QImage
│   │   └── viewport.py              # Pan/zoom state
│   ├── tools/
│   │   ├── base_tool.py             # Abstract base (on_press/move/release)
│   │   ├── select_tool.py
│   │   ├── pen_tool.py
│   │   ├── shape_tool.py
│   │   ├── text_tool.py
│   │   ├── markup_tool.py
│   │   └── measurement_tool.py
│   ├── annotations/
│   │   ├── base_annotation.py
│   │   ├── markup.py                # Highlights, comments, stamps
│   │   ├── drawing.py               # Freehand, shapes
│   │   └── cad.py                   # CAD symbols, title blocks
│   ├── document/
│   │   ├── document.py
│   │   ├── page.py
│   │   └── layers.py
│   ├── io/
│   │   ├── pdf_reader.py
│   │   ├── pdf_writer.py
│   │   ├── svg_handler.py
│   │   └── dxf_handler.py
│   ├── symbols/
│   │   ├── library.py
│   │   └── templates/
│   │       ├── ansi.py
│   │       └── iso.py
│   └── utils/
│       ├── geometry.py
│       └── config.py
├── assets/
│   ├── icons/
│   ├── templates/
│   └── symbols/
└── tests/
    ├── test_document.py
    ├── test_annotations.py
    ├── test_tools.py
    └── test_io.py
```

---

## Project Status

RedlineOS is in early development. Core PDF rendering and the drawing canvas are being built first, followed by the annotation toolset and CAD symbol library.

| Area | Status |
|---|---|
| PDF rendering | Planned |
| Drawing canvas | Planned |
| Markup tools | Planned |
| CAD symbols | Planned |
| DXF export | Planned |

---

## Contributing

Contributions are welcome. Please open an issue to discuss a feature or bug before submitting a pull request.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes
4. Open a pull request against `main`

See [CONTRIBUTING.md](CONTRIBUTING.md) for more detail (coming soon).

---

## License

RedlineOS is released under the [GNU Affero General Public License v3.0 (AGPL-3.0)](LICENSE).
