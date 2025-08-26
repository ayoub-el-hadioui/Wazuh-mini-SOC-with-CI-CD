# 🛡️ Mini SOC – Wazuh + CI/CD on Docker Swarm

## 📖 Overview
This project implements a **Mini SOC** with:
- **Wazuh** (Manager, Indexer, Dashboard)
- **Docker Swarm** for orchestration
- **Traefik** for HTTPS & reverse proxy
- **GitHub Actions** with self-hosted runners for CI/CD
- **Trivy** for container security scanning
- **Selenium & API tests** for validation
- **Ansible** for automated deployment

The setup follows the SOC Architect Challenge requirements.

---

## 🏗️ Architecture
![Architecture Diagram](docs/mini-soc-arch.png)

**Flow:**
1. Developer pushes code → GitHub Actions triggers pipeline
2. CI/CD pipeline:
   - Build images
   - Scan with Trivy
   - Run tests
   - Deploy via Ansible → Docker Swarm
3. Traefik exposes Wazuh dashboard securely over HTTPS
4. SOC Analysts access dashboard

---

## 📂 Repo Structure


## ⚡ Prerequisites
- Docker + Docker Swarm
- Ansible
- Trivy
- Python 3 + Selenium + ChromeDriver
- GitHub Actions **self-hosted runner**

---

## 🚀 How to Run
### 1. Initialize Swarm
```bash
docker swarm init

ansible-playbook ansible/playbooks/deploy.yml -i ansible/inventories/prod/hosts.ini

3. Access Dashboard

URL: https://<your-ip-or-domain>/

Credentials: admin / <secret-from-swarm>


.github/workflows/ci-cd.yml # CI/CD pipeline
