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
.
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── nightly-rotate-secrets.yml (optional)
├── ansible/
│   ├── inventories/
│   │   ├── prod/
│   │   │   ├── hosts.ini
│   │   │   └── group_vars/
│   │   │       └── all.yml (vault-encrypted example)
│   │   └── test/
│   │       ├── hosts.ini
│   │       └── group_vars/
│   │           └── all.yml (vault-encrypted example)
│   ├── playbooks/
│   │   ├── deploy.yml
│   │   └── teardown.yml
│   └── roles/
│       ├── swarm-init/
│       │   └── tasks/main.yml
│       ├── swarm-networks/
│       │   └── tasks/main.yml
│       ├── swarm-secrets/
│       │   └── tasks/main.yml
│       └── stack-deploy/
│           └── tasks/main.yml
├── docker/
│   ├── wazuh-dashboard/Dockerfile (optional extension)
│   └── README.md
├── stack/
│   └── wazuh-stack.yml
├── configs/
│   └── traefik/
│       ├── dynamic.yml
│       └── acme.json (created at runtime, chmod 600)
├── secrets-templates/
│   ├── dashboard_password.txt.tmpl
│   ├── wazuh_api_password.txt.tmpl
│   └── tls/
│       ├── fullchain.pem.tmpl
│       └── privkey.pem.tmpl
├── security/
│   ├── TRAEFIK.md
│   ├── TLS-OPTIONS.md
│   └── trivy/
│       └── .trivyignore
├── tests/
│   ├── selenium/
│   │   ├── requirements.txt
│   │   ├── conftest.py
│   │   └── test_dashboard.py
│   └── api/
│       └── test_wazuh_api.py
├── trivy/
│   └── trivy-config.yaml
├── rules/
│   ├── local_rules.xml
│   └── decoders/local_decoder.xml
├── scripts/
│   ├── push-secrets-to-swarm.py
│   ├── seed-known-users.py (bonus: optional baseline builder)
│   └── inject-ssh-sample-logs.sh
├── Makefile
└── README.md (this document split into repo readme)
---

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
