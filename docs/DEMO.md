# System demo guide

[Open the live English demo](https://zxq309.github.io/cowmata/demo/?lang=en). The same files work offline as described below.

## 1. Offline visual walkthrough

Open `demo/index.html` in a browser after cloning. No installation, internet request or backend is needed. Switch English/Chinese, select a processing stage, change the scenario and move the time cursor.

For a local HTTP preview, run `python -m http.server 8000 --bind 127.0.0.1` in this repository and open `http://127.0.0.1:8000/demo/`.

The waveform and event intervals are illustrative synthetic display data. This page does not run a model, display real cattle records or produce calibrated risk. Missing-data scenarios remain unavailable evidence, not low-risk outcomes.

## 2. Execute actual component demos

Clone the recognition repository next to this hub and install its documented environment. Authorized team members can also clone/install the private risk repository. The runner does not clone, install or download private data for you.

Windows PowerShell, from the hub root (replace Python paths with your environments):

```powershell
python scripts/run_component_demos.py --recognition-python ../cowmata-tailring/.venv/Scripts/python.exe --out runs/component-demo.json

# Include the private decision modules when authorized and installed:
python scripts/run_component_demos.py --recognition-python ../cowmata-tailring/.venv/Scripts/python.exe --include-risk --risk-python ../cowmata-risk/.venv/Scripts/python.exe
```

Linux/macOS use the corresponding `.venv/bin/python` paths. For another checkout layout, pass `--workspace /path/to/parent` containing the component folders.

The recognition demo reads its bundled session and executes the model. The risk demo executes both evidence modules on its own synthetic V2 packet. **They are independent demos with different inputs, not a fused end-to-end prediction.** The report records actual commits, return codes and outputs; missing environments fail before execution and component errors return nonzero.

## 3. What remains

The common event adapter, calibrated fusion policy and full field deployment are still development tasks. Follow [the roadmap](ROADMAP.en.md) and [interface proposal](INTERFACES.en.md). `components.json` registers the chosen component baselines, not a compatibility certification.
