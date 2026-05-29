import os
import time
import json
from dotenv import load_dotenv
from proxmoxer import ProxmoxAPI

load_dotenv()

# Inicializa a API
proxmox = ProxmoxAPI(
    host= os.getenv("PROXMOX_HOST"),
    user= os.getenv("PROXMOX_USER"),
    token_name= os.getenv("PROXMOX_TOKEN_NAME"),
    token_value= os.getenv("PROXMOX_TOKEN_SECRET"),
    verify_ssl= False,
    service='PVE'
)
# Exemplo: Listar nós e VMs
try:
    version = proxmox.version.get()
    print(f"Proxmox VE {version['version']} (Release {version['release']})")

except Exception as e:
   print(f"Erro {e} na chamada da API")

with open('<caminho-arquivo->/perfis.json', 'r', encoding='utf-8') as arquivo:
    PERFIS = json.load(arquivo)

def provisionar_vm(node, nome, perfil):
    config = PERFIS[perfil]
    vmid = proxmox.cluster.nextid.get()

    upid = clone_vm(
        node,
        config["template_id"],
        vmid,
        nome
    )

    aguardar_clone(node, upid)

    proxmox.nodes(node).qemu(vmid).config.put(
        cores=config['cores'],
        memory=config['memory'],
        cpu=config['cpu'],
        onboot=config['onboot'],
        net0=f"virtio,bridge={config['bridge']}",
        ipconfig0="ip=dhcp",
    )
    print(f"✅ VM {nome} (ID: {vmid}) provisionada com perfil {perfil}!")
    return vmid

def aguardar_clone(node, upid, timeout=900):
    print("Aguardando clone finalizar...")

    inicio = time.time()

    while True:
        task = (
            proxmox
            .nodes(node)
            .tasks(upid)
            .status
            .get()
        )

        status = task["status"]
        exitstatus = task.get("exitstatus")

        if status == "stopped":
            if exitstatus == "OK":
                print("✅ Clone finalizado!")
                return

            raise RuntimeError(
                f"Clone falhou: {exitstatus}"
            )

        if time.time() - inicio > timeout:
            raise TimeoutError(
                "Timeout aguardando clone."
            )

        print("⏳ Clonando...")
        time.sleep(5)

def clone_vm(node, template_id, new_vmid, name, full_clone=True):
    upid = proxmox.nodes(node).qemu(template_id).clone.create(
        newid=new_vmid,
        name=name,
        full=1 if full_clone else 0,
        target=node
    )

    print(
        f"VM {new_vmid} ({name}) clonando "
        f"do template {template_id}"
    )

    return upid

# Input → só coleta os dados e chama provisionar_vm
def input_provisionar():
    print("\nPerfis disponíveis:")
    for perfil in PERFIS:
        print(f"  - {perfil}")

    node = input("\nDigite o nó: ")
    nome = input("Nome da VM: ")
    perfil = input("Qual perfil: ")

    provisionar_vm(node, nome, perfil)

try:
    input_provisionar()

except Exception as e:
    print(f"Ocorreu o erro {e} no provisionamento da vm")
