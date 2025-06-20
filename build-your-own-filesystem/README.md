# Build Your Own Filesystem (In-Memory Shell)

This project simulates a basic in-memory filesystem with folder navigation and file creation. It mimics how directories and files are managed in real systems — ideal for understanding how hospitals, cloud AI platforms, or simulation frameworks organize their data internally.

---

## Supported Features

- `mkdir <folder>` – create folder
- `touch <file>` – create file
- `write <file> "text"` – write to file
- `read <file>` – read file content
- `ls` – list contents
- `cd <folder>` / `cd ..` – navigate
- `pwd` – show full path
- `exit` – quit shell

---

## Clinical + Simulation Relevance

In health tech systems:
- Every patient’s scans, logs, vitals = **structured folders/files**
- Digital twins store outputs by region + timestep
- Remote imaging services stage files this way in the cloud

This project helps you:
- Build better simulation environments
- Understand storage workflows in medical image routing
- Prototype a fake PACS (Picture Archiving & Communication System)

---

## How to Run

```bash
cd src/
python main.py
```

Sample session:
```bash
mkdir brain
cd brain
touch summary.txt
write summary.txt "Viability fell to 0.18 at t=40."
read summary.txt
```

---

## File Structure

- `src/main.py` – main filesystem logic
- `assets/` – flowcharts, command examples (optional)
- `NOTES.md` – your learning reflections or clinical ideas

---

## Author

**Ihunna Amugo**  
DDS Candidate | MHA | MS | REHS | PhD(c) Computational Engineering  
GitHub: [@ihunnamatata](https://github.com/ihunnamatata)
