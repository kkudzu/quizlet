# quizlet

## Run the study hub

Serve this folder over localhost rather than opening `index.html` as a `file://` URL. For example, with Python installed:

```sh
python3 -m http.server 8000
```

Then open `http://localhost:8000`.

The app parses common card formats instantly on-device. Less common formats use SmolLM2 locally in the browser, with WebGPU acceleration when available and a WebAssembly CPU fallback. The parser pins a known model revision and a compatible Transformers.js/ONNX Runtime version, then checks cross-origin access to its runtime and model assets before loading. The first AI use downloads the model weights (about 118 MB for GPU or 137 MB for CPU); subsequent loads use the browser cache. A network connection is required for that first download. If the browser or network blocks the runtime/model hosts, the app reports which asset failed and still imports every card in its original wording; browser/device and network availability cannot be guaranteed by the app.

`index.svg` is a launcher that opens the embedded `index.html` app in a new `about:blank` tab. Click **Open study hub**; if your browser blocks pop-ups, allow them for this page and try again. Open the SVG directly in a modern browser (not as an image). After changing the app, regenerate the bundle with `python3 build_svg.py`.