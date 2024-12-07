# **Bandwidth Management with MEC APIs**

A Flask-based API for managing bandwidth on Kali Linux, leveraging `tc` (traffic control) for enforcing bandwidth limits on network interfaces.

---

## **Table of Contents**
1. [Introduction](#introduction)
2. [Team Members](#team-members)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Testing](#testing)
7. [Monitoring Tools](#monitoring-tools)
8. [Reset Bandwidth Rules](#reset-bandwidth-rules)
9. [Demo Video](#demo-video)
10. [Enhancements](#enhancements)

---

## **Introduction**
This project provides a RESTful API for bandwidth management on network interfaces using `tc` (traffic control). It is tailored for Kali Linux but works with similar Linux distributions like Ubuntu.

---

## **Team Members**
- **Ganesh Sonawane 202151054**
- **Kundan Singh 202151080**
- **Krishna Kawale 202151076**
- **Dhiraj Kumar Barela 202152310**
- **Adarsh Maddheshiya 202151004**

---

## **Requirements**
- Kali Linux or similar Linux distribution
- Python 3.x
- `tc` (traffic control)
- Monitoring tools (`iftop`, `nload`) (optional)
- `iperf3` for bandwidth testing (optional)

---

## **Installation**

1. **Update the System:**
   ```bash
   sudo apt update && sudo apt upgrade -y
2. **Install Required Packages:**
   ```bash
   sudo apt install curl build-essential python3 python3-pip iproute2 iftop nload -y
3. **Set Up the Project:**
   ```bash
   mkdir bandwidth-management && cd bandwidth-management
4. **Install Flask:**
   ```bash
   pip3 install flask
5. **Create the API Script:**
   - Create a Python file:
   ```bash
   nano mec_api.py
## **Usage**
1. **Run the API:**
   ```bash
   python3 mec_api.py
- The API will start and listen on http://0.0.0.0:5000.
2. **Send a POST Request:**
```
  curl -X POST -H "Content-Type: application/json" -d '{"device": "eth0", "bandwidth": "1mbit"}' http://localhost:5000/manage_bandwidth
```
- Expected Response:
    ```bash
    "message": "Bandwidth set to 1mbit for eth0"
  
## Testing
1. Install iperf3:
    ```bash
   sudo apt install iperf3
2. Simulate Traffic:
- Start the server:
     ```bash
  iperf3 -s
- Run a client test
     ```bash
  iperf3 -c <server_ip>
- Observe the impact of bandwidth limitations.

# Monitoring Tools

## Install Tools

- To monitor bandwidth, install the required tools using:

   ```
   sudo apt install iftop nload
   ```
    
## Monitor Bandwidth:
- Use nload :
  ```bash
  nload
- Use iftop:
  ```bash
  sudo iftop

## Reset Bandwidth Rules
- To remove or reset bandwidth limitations on a network interface, run:
  ```
    sudo tc qdisc del dev eth0 root
  ```
## Demo Video
🎥 Check out the demo video here to see the API in action!
- [Demonstration](https://drive.google.com/file/d/17H8HOKrc7OWB7ZjU2bH_2ew9U5UzAPsN/view?usp=drive_link)
- [Report](https://www.overleaf.com/9645693241mscjpytqnjvp#116a5f).
- [Drive Folder](https://drive.google.com/drive/folders/1wPBKR3rj-AFaZL3amj5Fm33kL2hKT9lH?usp=drive_link)

## Enhancements
1. Deploy API as a Service:
   -Create a systemd service file:
   ```bash
   sudo nano /etc/systemd/system/mec_api.service
- Add the following content:
  ```
  [Unit]
  Description=MEC API Service
  After=network.target

  [Service]
  ExecStart=/usr/bin/python3 /path/to/mec_api.py
  WorkingDirectory=/path/to/
  Restart=always
  User=root

  [Install]
  WantedBy=multi-user.target
  ```
  
- Reload systemd and enable the service
  ```
  sudo systemctl daemon-reload
  sudo systemctl enable mec_api.service
  sudo systemctl start mec_api.service
  ```

2. Extend API Functionality:
  - Add endpoints for deleting or modifying bandwidth rules.
  - Support multiple network interfaces.

   
4. Integrate with a Frontend:
  - Use frameworks like React or Angular to manage bandwidth visually.




