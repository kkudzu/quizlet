# quizlet

## Run the study hub

Open `quiz1.svg` directly in a modern browser. It launches the full embedded HTML app in a new `about:blank` tab; no separate server, backend, or proxy is needed.

The app parses common formats instantly on-device. Less common cards use the pinned SmolLM2 model locally in the browser. Its CPU ONNX model and tokenizer are embedded in `quiz1.svg` as a compressed ZIP and unpacked client-side; no Hugging Face connection or model download is needed. Complex cards are sent to the model one at a time and returned as one question/answer pair. If the model cannot verify a split, the original card stays together. Answer points use Radicle Garden-inspired blue, green, and lavender highlights. The bundled SmolLM2 files are Apache-2.0 licensed; the model source and license are included in the archive.

Transformers.js and the ONNX Runtime WebAssembly engine are loaded from jsDelivr, so internet access to `cdn.jsdelivr.net` is still required for AI. The large SVG includes the compressed model archive; the model is expanded in browser memory for inference. The interface uses JetBrains Mono, a minimal neutral palette, and restrained Radicle Garden-inspired colored highlights.

`quiz1.svg` is a launcher that opens the embedded `index.html` app in a new `about:blank` tab. Click **Open study hub**; if your browser blocks pop-ups, allow them for this page and try again. Open the SVG as a document, not as an image. After changing the app, regenerate the bundle with `python3 build_svg.py`; that requires `assets/smollm2-135m-instruct-cpu.zip`, the source archive embedded in the SVG. Git LFS is configured for the SVG and model ZIP because GitHub rejects ordinary Git files larger than 100 MB.