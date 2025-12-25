


# 🐳 Docker Security Scanner

A **Python-based DevSecOps tool** that scans **Dockerfiles**, **Docker Compose files**, or **entire project directories** to detect insecure configurations and vulnerable container images.

---

## ⭐ Why this project is needed

Containers are widely used, but insecure defaults are common.  
This tool helps identify:
- Dockerfile security misconfigurations
- Insecure Docker Compose settings
- Vulnerable container base images
- Issues across multi-service and monorepo projects

Designed to reflect **real-world DevOps and security workflows**.

---

## 🚀 Key Highlights

- 🔍 Dockerfile security scanning  
- 📦 Docker Compose security scanning  
- 📁 Recursive project scanning  
- 🛡 Container vulnerability scanning using **Grype**  
- 📝 Single consolidated, timestamped report file  
- 💻 Works on Windows, Linux, and macOS  

---

## Installation
 1️⃣ Clone the repo

```bash
git clone https://github.com/vishrun/Docker-Security-Scanner.git
cd Docker-Security-Scanner
```
    
2️⃣ Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate  # Linux / macOS
```
3️⃣ Install Dependenices

🛡 Install Grype (Windows)

Download from: https://github.com/anchore/grype/releases

Extract to:
```bash
C:\Tools\Grype\grype.exe
```

Verify:
```
& "C:\Tools\Grype\grype.exe" --version
```

## Running the Scanner

Scan a Dockerfile
```
python scanner.py --dockerfile Dockerfile
```
Scan a Docker Compose file
```
python scanner.py --dockercompose docker-compose.yml
```
Scan an entire project (recommended)
```
python scanner.py --path .
```
## 📄 Output

Each run generates one report file:

```
scan_results_YYYYMMDD_HHMMSS.txt
```

The report includes:

* Dockerfile findings

* Docker Compose findings

* Container vulnerability results