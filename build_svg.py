from pathlib import Path
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parent
SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)


def svg_element(parent, name, attributes=None, text=None):
    element = ET.SubElement(parent, f"{{{SVG_NS}}}{name}", attributes or {})
    element.text = text
    return element


def build():
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    svg = ET.Element(
        f"{{{SVG_NS}}}svg",
        {
            "width": "100%",
            "height": "100vh",
            "viewBox": "0 0 1440 900",
            "preserveAspectRatio": "xMidYMid meet",
            "role": "application",
            "aria-labelledby": "title description",
        },
    )
    svg_element(svg, "title", {"id": "title"}, "Drivers Ed Study Hub launcher")
    svg_element(
        svg,
        "desc",
        {"id": "description"},
        "Open the interactive study hub in a new browser tab.",
    )
    svg_element(svg, "metadata", {"id": "app-source"}, html)
    svg_element(
        svg,
        "style",
        text="""text { font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
.background { fill: #f8fafc; }
.card { fill: #fff; stroke: #e2e8f0; stroke-width: 1.5; }
.title { fill: #0f172a; font-size: 30px; font-weight: 700; }
.copy { fill: #64748b; font-size: 16px; }
.button { fill: #2563eb; cursor: pointer; }
.button:hover { fill: #1d4ed8; }
.button:focus { stroke: #93c5fd; stroke-width: 4; }
.button-label { fill: #fff; font-size: 16px; font-weight: 650; pointer-events: none; }
.status { fill: #64748b; font-size: 13px; }""",
    )
    svg_element(svg, "rect", {"class": "background", "width": "1440", "height": "900"})
    svg_element(
        svg,
        "rect",
        {"class": "card", "x": "410", "y": "310", "width": "620", "height": "280", "rx": "16"},
    )
    svg_element(
        svg,
        "text",
        {"class": "title", "x": "720", "y": "390", "text-anchor": "middle"},
        "Drivers Ed Study Hub",
    )
    svg_element(
        svg,
        "text",
        {"class": "copy", "x": "720", "y": "430", "text-anchor": "middle"},
        "Launch the interactive study app in a new tab.",
    )
    button = svg_element(
        svg,
        "g",
        {
            "id": "launch-button",
            "role": "button",
            "tabindex": "0",
            "aria-label": "Launch study hub in a new tab",
            "onclick": "launchApp()",
            "onkeydown": (
                'if (event.key === "Enter" || event.key === " ") '
                "{ event.preventDefault(); launchApp(); }"
            ),
        },
    )
    svg_element(
        button,
        "rect",
        {"class": "button", "x": "565", "y": "466", "width": "310", "height": "54", "rx": "9"},
    )
    svg_element(
        button,
        "text",
        {"class": "button-label", "x": "720", "y": "500", "text-anchor": "middle"},
        "Open study hub",
    )
    svg_element(
        svg,
        "text",
        {
            "id": "status",
            "class": "status",
            "x": "720",
            "y": "555",
            "text-anchor": "middle",
            "role": "status",
            "aria-live": "polite",
        },
        "If the tab does not open, allow pop-ups and try again.",
    )
    svg_element(
        svg,
        "script",
        text="""function launchApp() {
  const appWindow = window.open("about:blank", "_blank");
  if (!appWindow) {
    document.getElementById("status").textContent =
      "Pop-up blocked. Allow pop-ups for this page, then try again.";
    return;
  }
  appWindow.opener = null;
  appWindow.document.open();
  appWindow.document.write(document.getElementById("app-source").textContent);
  appWindow.document.close();
  document.getElementById("status").textContent =
    "Study hub opened in a new tab.";
}""",
    )
    (ROOT / "index.svg").write_bytes(ET.tostring(svg, encoding="utf-8", xml_declaration=True))


if __name__ == "__main__":
    build()
