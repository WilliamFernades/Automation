# Automation Lab

Repositório centralizado para projetos de automação voltados a infraestrutura, virtualização, provisionamento, observabilidade e operações.

O objetivo deste repositório é consolidar estudos, ferramentas e automações utilizadas em ambientes Linux e virtualização, com foco em evolução prática para áreas como:

- SRE
- DevOps
- Platform Engineering
- Infrastructure Automation
- Cloud & Virtualization

---

# Estrutura do Repositório

```text
automation/
│
├── provider-vm-proxmox/
├── monitoring/
├── ansible/
├── docker/
├── scripts/
└── observability/
```

Cada diretório representa um projeto ou conjunto de automações independentes.

---

# Projetos

## provider-vm-proxmox

Provisionamento automatizado de máquinas virtuais no Proxmox VE utilizando Python e cloud-init.

### Features atuais

- Clone automatizado de templates
- Provisionamento baseado em perfis
- Async task tracking via UPID
- Geração automática de VMID
- Timeout handling
- Configuração automática de VM

### Stack

- Python
- Proxmox API
- Proxmoxer
- Cloud-init

---

# Objetivos do Laboratório

- Automatizar operações de infraestrutura
- Reduzir processos manuais
- Padronizar provisionamento
- Implementar observabilidade
- Evoluir arquiteturas de automação
- Consolidar práticas modernas de SRE/DevOps

---

# Roadmap Geral

## Infraestrutura & Provisionamento
- [x] Provisionamento básico de VMs
- [x] Profiles declarativos
- [x] Controle de tasks async
- [ ] Logging estruturado
- [ ] Configuração via YAML
- [ ] Inventário automatizado
- [ ] Provisionamento multi-node

## APIs & Plataforma
- [ ] FastAPI
- [ ] RBAC
- [ ] API REST
- [ ] Workers assíncronos
- [ ] Task queue

## Observabilidade
- [ ] Prometheus
- [ ] Grafana
- [ ] Logs centralizados
- [ ] Métricas operacionais

## DevOps & CI/CD
- [ ] Docker
- [ ] Docker Compose
- [ ] GitHub Actions
- [ ] Testes automatizados

---

# Ambiente

Projetos desenvolvidos e testados principalmente em:

- Linux
- Proxmox VE
- Ambientes virtualizados
- Containers Docker

---

# Objetivo Profissional

Este laboratório serve como ambiente de estudo e desenvolvimento contínuo para aprofundamento em:

- Linux
- Automação
- Infraestrutura
- APIs
- Observabilidade
- Sistemas distribuídos
- Engenharia de confiabilidade (SRE)

---

# Aviso

Os projetos deste repositório estão em evolução contínua e podem sofrer mudanças estruturais frequentes.
