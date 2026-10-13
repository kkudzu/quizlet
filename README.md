# quizlet

## Run the study hub

Serve this folder over localhost rather than opening `index.html` as a `file://` URL. For example, with Python installed:

```sh
python3 -m http.server 8000
```

Then open `http://localhost:8000`.

The app parses common card formats instantly on-device. Less common formats can use SmolLM2 locally in the browser, with WebGPU acceleration when available and a WebAssembly CPU fallback. On first use, the browser must download the model and Transformers.js from their public hosts; subsequent loads use the browser cache. If model download or inference fails, the app still imports every card and preserves its original text. As with any browser model, speed depends on the device and a first-time download requires a network connection.

`index.svg` is a launcher that opens the embedded `index.html` app in a new `about:blank` tab. Click **Open study hub**; if your browser blocks pop-ups, allow them for this page and try again. Open the SVG directly in a modern browser (not as an image). The SVG embeds a copy of `index.html`, so regenerate it after changing the app.