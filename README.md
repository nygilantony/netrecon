# NetRecon v2.1

**Modular Network Reconnaissance Framework**

NetRecon is a lightweight, multi-threaded network reconnaissance tool designed for fast host discovery and TCP port scanning. It is built for learning, internal assessments, and authorized security testing.

---

## 🔥 Features

* ARP-based host discovery (local network)
* Multi-threaded TCP connect port scanning
* Configurable port scan profiles
* Service identification (basic)
* Banner grabbing for detected services
* JSON report generation
* Clean CLI interface with colored output
* Interrupt handling (Ctrl + C safe exit)

---

## ⚙️ Port Scan Profiles

| Profile | Range   | Description             |
| ------- | ------- | ----------------------- |
| 1       | 1–1024  | Well-known ports (safe) |
| 2       | 1–5000  | Fast extended scan      |
| 3       | 1–30000 | Aggressive scan         |
| 4       | 1–65535 | Full port scan          |

---

## 🚀 Usage

```bash
sudo python3 main.py --target 192.168.1.0/24
```

Optional arguments:

```bash
--threads 50
```

---

## 🧠 How It Works

1. Performs ARP scan to discover live hosts
2. Iterates through discovered hosts
3. Scans selected port range using TCP connect method
4. Identifies common services based on port numbers
5. Attempts banner grabbing on open ports
6. Stores results in structured JSON report

---

## 📂 Project Structure

```
netrecon/
│── core/
│   ├── engine.py
│   ├── config.py
│
│── scan/
│   ├── tcp_connect.py
│
│── discovery/
│   ├── arp.py
│
│── fingerprint/
│   ├── banners.py
│
│── output/
│   ├── console.py
│   ├── reports.py
│
│── utils/
│   ├── ui.py
│   ├── services.py
│
│── main.py
│── README.md
```

---

## 📊 Example Output

```
[+] Host discovered: 192.168.1.1

[+] Open ports:
21/tcp (FTP)
80/tcp (HTTP)
443/tcp (HTTPS)
```

---

## 📁 Report Output

Reports are saved as:

```
netrecon_<timestamp>.json
```

---

## ⚠️ Disclaimer

This tool is intended **for educational purposes and authorized testing only**.
Do not use it on networks or systems without proper permission.

---

## 🧑‍💻 Author

Nygil Antony

---

## 🚧 Future Improvements

* Service version detection
* OS fingerprinting
* UDP scanning
* Web vulnerability checks
* Nmap-like advanced scanning modes

---
