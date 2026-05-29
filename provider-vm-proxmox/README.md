# Proxmox VM Provisioner

Provisionamento automatizado de VMs em ambientes Proxmox VE utilizando Python e cloud-init.

## Objetivo

Automatizar a criação de máquinas virtuais utilizando perfis padronizados para reduzir erros operacionais e acelerar provisionamento de infraestrutura.

## Features

- Clone automatizado de templates
- Async task tracking via UPID
- Profiles declarativos via JSON
- Auto geração de VMID
- Timeout handling
- Configuração automática via cloud-init

## Stack

- Python
- Proxmox VE API
- Proxmoxer
- Cloud-init

## Estrutura

```text
provider_vm.py
perfis.json
```

## Exemplo de execução

```bash
python provider_vm.py
```

## Exemplo de profiles

```json
{
  "dev": {
    "template_id": 9100,
    "cores": 1,
    "memory": 2048
  }
}
```
