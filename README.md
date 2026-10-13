# quizlet

## Run the study hub

Open `index.svg` directly in a modern browser. It launches the full embedded HTML app in a new `about:blank` tab; no separate server, backend, or proxy is needed.

The app parses common card formats instantly on-device. Less common formats use SmolLM2 locally in the browser, with WebGPU acceleration when available and a WebAssembly CPU fallback. The parser pins a known model revision and compatible Transformers.js/ONNX Runtime versions. Imported questions and answers stay together in a single card, answer points are highlighted, and uncertain AI results preserve the original card text instead of dropping or moving its content. On first AI use, the browser downloads the model weights (about 118 MB for GPU or 137 MB for CPU) directly from Hugging Face; Transformers.js and ONNX Runtime/WASM are loaded from jsDelivr. Downloads are cached by the browser. If the SVG is opened with a browser or extension that blocks cross-origin `fetch` from its `about:blank` tab, AI model downloads may be blocked; allow the Hugging Face and jsDelivr domains in browser privacy/network settings.

The interface draws on Radicle's restrained warm neutrals and muted green accents and uses JetBrains Mono, with a system monospace fallback if the font host is unavailable. The first AI use needs an internet connection; browser/device and network availability cannot be guaranteed by the app.

`index.svg` is a launcher that opens the embedded `index.html` app in a new `about:blank` tab. Click **Open study hub**; if your browser blocks pop-ups, allow them for this page and try again. Open the SVG as a document, not as an image. After changing the app, regenerate the bundle with `python3 build_svg.py`.