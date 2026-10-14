import base64
from pathlib import Path
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parent
MODEL_ARCHIVE = ROOT / "assets" / "smollm2-135m-instruct-cpu.zip"
MODEL_ARCHIVE_PLACEHOLDER = "__SMOLLM_MODEL_ARCHIVE_BASE64__"
SVG_OUTPUT = ROOT / "quiz1.svg"
SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)


def svg_element(parent, name, attributes=None, text=None):
    element = ET.SubElement(parent, f"{{{SVG_NS}}}{name}", attributes or {})
    element.text = text
    return element


def build():
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    if html.count(MODEL_ARCHIVE_PLACEHOLDER) != 1:
        raise ValueError("index.html must contain exactly one embedded model archive placeholder")
    model_archive = base64.b64encode(MODEL_ARCHIVE.read_bytes()).decode("ascii")
    html = html.replace(MODEL_ARCHIVE_PLACEHOLDER, "")
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
    svg_element(svg, "metadata", {"id": "model-archive"}, model_archive)
    svg_element(
        svg,
        "style",
        text="""text { font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
.background { fill: #f7f8fa; }
.card { fill: #fff; stroke: #e7e9ed; stroke-width: 1; }
.title { fill: #17191d; font-size: 26px; font-weight: 650; }
.copy { fill: #737983; font-size: 15px; }
.button { fill: #17191d; cursor: pointer; }
.button:hover { fill: #363a40; }
.button:focus { stroke: #aeb4bd; stroke-width: 3; }
.button-label { fill: #fff; font-size: 15px; font-weight: 600; pointer-events: none; }
.status { fill: #737983; font-size: 12px; }""",
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
  appWindow.document.write(`<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Opening Study Hub</title><style>
    *{box-sizing:border-box}body{margin:0;min-height:100vh;display:grid;place-items:center;background:#f7f8fa;color:#17191d;font:14px system-ui,sans-serif}
    main{display:grid;justify-items:center;gap:14px}.spinner{width:24px;height:24px;border:2px solid #e7e9ed;border-top-color:#1c77ff;border-radius:50%;animation:spin .8s linear infinite}
    p{margin:0;color:#737983}@keyframes spin{to{transform:rotate(360deg)}}
  </style></head><body><main role="status" aria-live="polite"><span class="spinner"></span><p>Preparing your study hub…</p></main></body></html>`);
  document.getElementById("status").textContent = "Preparing study hub...";
  requestAnimationFrame(() => setTimeout(() => {
    try {
      const appSource = document.getElementById("app-source").textContent;
      const archiveElement = document.getElementById("model-archive");
      const modelArchive = archiveElement.textContent;
      appWindow.document.open();
      appWindow.document.write(appSource);
      appWindow.document.close();
      appWindow.document.getElementById("embeddedModelArchive").textContent = modelArchive;
      appWindow.document.dispatchEvent(new appWindow.Event("embeddedmodelready"));
      archiveElement.textContent = "";
      document.getElementById("status").textContent = "Study hub opened in a new tab.";
    } catch (error) {
      appWindow.document.body.innerHTML = "<main><p>The study hub could not be opened. Close this tab and try again.</p></main>";
      document.getElementById("status").textContent = `Could not open study hub: ${error.message}`;
    }
  }, 30));
}""",
    )
    SVG_OUTPUT.write_bytes(ET.tostring(svg, encoding="utf-8", xml_declaration=True))


if __name__ == "__main__":
    build()
