from pathlib import Path

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QHBoxLayout,
    QStackedWidget,
    QStyle,
    QTabBar,
    QVBoxLayout,
    QWidget,
)

from redlineos.ui.ribbon.ribbon_button import RibbonButton
from redlineos.ui.ribbon.ribbon_group import RibbonGroup
from redlineos.ui.ribbon.ribbon_tab import RibbonTab


class Ribbon(QWidget):
    open_requested = Signal(Path)
    save_requested = Signal()
    close_requested = Signal()
    zoom_in_requested = Signal()
    zoom_out_requested = Signal()
    fit_page_requested = Signal()
    next_page_requested = Signal()
    previous_page_requested = Signal()
    comment_panel_requested = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(120)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Full-width blue header containing the tab bar
        header = QWidget()
        header.setFixedHeight(30)
        header.setStyleSheet("background-color: #2c5f8a;")
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(0, 0, 0, 0)
        header_layout.setSpacing(0)

        self._tab_bar = QTabBar()
        self._tab_bar.setExpanding(False)
        self._tab_bar.setStyleSheet("""
            QTabBar { background: transparent; }
            QTabBar::tab {
                background: transparent;
                color: rgba(255, 255, 255, 0.85);
                padding: 5px 16px;
                font-size: 9pt;
                border: none;
                min-width: 60px;
            }
            QTabBar::tab:selected {
                background: #f0f0f0;
                color: #2c5f8a;
                font-weight: bold;
                border-top-left-radius: 3px;
                border-top-right-radius: 3px;
            }
            QTabBar::tab:hover:!selected {
                background: rgba(255, 255, 255, 0.15);
                color: white;
            }
        """)
        header_layout.addWidget(self._tab_bar)
        header_layout.addStretch()
        layout.addWidget(header)

        self._stack = QStackedWidget()
        self._stack.setStyleSheet("background-color: #f0f0f0; border-bottom: 1px solid #cccccc;")
        layout.addWidget(self._stack)

        self._tab_bar.currentChanged.connect(self._stack.setCurrentIndex)

        self._build_tabs()
        self._apply_button_styles()

    def _build_tabs(self) -> None:
        self._add_home_tab()
        self._add_view_tab()
        self._add_markup_tab()
        self._add_drawing_tab()
        self._add_cad_tab()

    def _add_home_tab(self) -> None:
        tab = RibbonTab()
        style = QApplication.style()

        file_group = RibbonGroup("File")
        open_btn = RibbonButton("Open", style.standardIcon(QStyle.StandardPixmap.SP_DirOpenIcon))
        open_btn.clicked.connect(self._on_open)
        save_btn = RibbonButton("Save", style.standardIcon(QStyle.StandardPixmap.SP_DialogSaveButton))
        save_btn.clicked.connect(self.save_requested)
        close_btn = RibbonButton("Close", style.standardIcon(QStyle.StandardPixmap.SP_DialogCloseButton))
        close_btn.clicked.connect(self.close_requested)
        file_group.add_button(open_btn)
        file_group.add_button(save_btn)
        file_group.add_button(close_btn)
        tab.add_group(file_group)

        self._register_tab("Home", tab)

    def _add_markup_tab(self) -> None:
        tab = RibbonTab()

        annotate_group = RibbonGroup("Annotate")
        annotate_group.add_button(RibbonButton("Highlight"))
        comment_btn = RibbonButton("Comment")
        comment_btn.clicked.connect(self.comment_panel_requested)
        annotate_group.add_button(comment_btn)
        annotate_group.add_button(RibbonButton("Stamp"))
        tab.add_group(annotate_group)

        redline_group = RibbonGroup("Redline")
        for label in ("Pen", "Text"):
            redline_group.add_button(RibbonButton(label))
        tab.add_group(redline_group)

        self._register_tab("Markup", tab)

    def _add_drawing_tab(self) -> None:
        tab = RibbonTab()

        shapes_group = RibbonGroup("Shapes")
        for label in ("Line", "Rectangle", "Circle", "Polygon"):
            shapes_group.add_button(RibbonButton(label))
        tab.add_group(shapes_group)

        style_group = RibbonGroup("Style")
        for label in ("Color", "Line Weight"):
            style_group.add_button(RibbonButton(label))
        tab.add_group(style_group)

        self._register_tab("Drawing", tab)

    def _add_cad_tab(self) -> None:
        tab = RibbonTab()

        templates_group = RibbonGroup("Templates")
        for label in ("ANSI", "ISO"):
            templates_group.add_button(RibbonButton(label))
        tab.add_group(templates_group)

        symbols_group = RibbonGroup("Symbols")
        symbols_group.add_button(RibbonButton("Library"))
        tab.add_group(symbols_group)

        layers_group = RibbonGroup("Layers")
        layers_group.add_button(RibbonButton("Manage"))
        tab.add_group(layers_group)

        self._register_tab("CAD", tab)

    def _add_view_tab(self) -> None:
        tab = RibbonTab()
        style = QApplication.style()

        zoom_group = RibbonGroup("Zoom")
        zoom_in_btn = RibbonButton("Zoom In", style.standardIcon(QStyle.StandardPixmap.SP_ArrowUp))
        zoom_in_btn.clicked.connect(self.zoom_in_requested)
        zoom_out_btn = RibbonButton("Zoom Out", style.standardIcon(QStyle.StandardPixmap.SP_ArrowDown))
        zoom_out_btn.clicked.connect(self.zoom_out_requested)
        fit_btn = RibbonButton("Fit Page")
        fit_btn.clicked.connect(self.fit_page_requested)
        zoom_group.add_button(zoom_in_btn)
        zoom_group.add_button(zoom_out_btn)
        zoom_group.add_button(fit_btn)
        tab.add_group(zoom_group)

        pages_group = RibbonGroup("Pages")
        prev_btn = RibbonButton("Previous", style.standardIcon(QStyle.StandardPixmap.SP_ArrowLeft))
        prev_btn.clicked.connect(self.previous_page_requested)
        next_btn = RibbonButton("Next", style.standardIcon(QStyle.StandardPixmap.SP_ArrowRight))
        next_btn.clicked.connect(self.next_page_requested)
        pages_group.add_button(prev_btn)
        pages_group.add_button(next_btn)
        tab.add_group(pages_group)

        self._register_tab("View", tab)

    def _register_tab(self, title: str, tab: RibbonTab) -> None:
        self._tab_bar.addTab(title)
        self._stack.addWidget(tab)

    def _on_open(self) -> None:
        path, _ = QFileDialog.getOpenFileName(self, "Open PDF", "", "PDF Files (*.pdf)")
        if path:
            self.open_requested.emit(Path(path))

    def _apply_button_styles(self) -> None:
        self.setStyleSheet(self.styleSheet() + """
            QToolButton {
                background: transparent;
                border: 1px solid transparent;
                border-radius: 3px;
                padding: 3px 4px;
                font-size: 9pt;
                color: #1a1a1a;
            }
            QToolButton:hover {
                background: #cce0f5;
                border-color: #99c4eb;
            }
            QToolButton:pressed {
                background: #99c4eb;
                border-color: #5ba0d4;
            }
        """)
