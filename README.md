# Monitorando Nextcloud com API e com Zabbix 
## Pré requisitos
Instale os pacotes Git e Python3.7 no servidor Nextcloud a ser monitorado.

```bash
apt install git python3.7 python3-venv -y
```

### Baixando
No Nextcloud, crie o diretório onde vão ficar os arquivos e clone o repositório.

```bash
mkdir -p /etc/zabbix/scripts
cd /etc/zabbix/scripts/
git clone https://github.com/lenoncorrea/zabbix-nextcloud-api.git
```

### Ajustando
Copie o arquivo '.conf' para o local correto (contém o UserParameter do Zabbix) e ajuste as permissões.

```bash
mv /etc/zabbix/scripts/zabbix-nextcloud-api/nextcloud_api.conf /etc/zabbix/zabbix_agentd.conf.d/
chmod 755 /etc/zabbix/zabbix_agentd.conf.d/nextcloud_api.conf
chmod 755 /etc/zabbix/scripts/zabbix-nextcloud-api/api_nextcloud.py
```
### VirtualEnv
Crie um venv na pasta do nosso script e instale os requerimentos.

```bash
python3 -m venv /etc/zabbix/scripts/zabbix-nextcloud-api/venv
. /etc/zabbix/scripts/zabbix-nextcloud-api/venv/bin/activate
pip install -r /etc/zabbix/scripts/zabbix-nextcloud-api/requirements.txt
```

### Nextcloud
Agora, na interface WEB do Nextcloud, crie um usuário com privilégios de Administrador (para que tenha acesso as informações da API). Após, para obter o 'apppassword' (necessário para nosso uso), siga documentação do Nextcloud, disponível em: [Documentação API Nextcloud](https://docs.nextcloud.com/server/latest/developer_manual/client_apis/LoginFlow/).

### Ajuste Zabbix Agent e Restart
Retorne ao servidor Nextcloud (a ser monitorado). Por padrão o Zabbix não aceita alguns parametros no retorno, então realizamos este ajuste, e após restartamos o Agent.

```bash
sed -i 's/# UnsafeUserParameters=0/UnsafeUserParameters=1/' /etc/zabbix/zabbix_agentd.conf
systemctl restart zabbix-agent
```

### Importe o template no Zabbix, atrele ao Nextcloud, e altere as váriaveis a seguir (nos Macros do servidor a ser monitorado).
#### O template é 'zabbix-nextcloud.xml' que esta neste repositório.
```python
BASEURL = 'URL_DO_NEXTCLOUD'
USER = 'USUARIO_CRIADO'
TOKEN = 'APPPASSWORD'
```

## Contribuição

Achou algum bug ou tem uma sugestão de melhoria? Envie-me!

## Licença
[MIT](https://github.com/lenoncorrea/zabbix-nextcloud-api/blob/master/LICENSE)
