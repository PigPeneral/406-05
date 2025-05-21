# Note

---

## 網頁設計與AIOT(D) Note

### about SSH and sftp(ex)

#### file: sftp.json

```JSON
#Filezila
{
    "name": "*****-*****",
    "host": "******",
    "protocol": "ftp",
    "port": 21,
    "username": "****",
    "password": "**********",
    "remotePath": "/",
    "uploadOnSave": false,
    "useTempFile": false,
    "openSsh": false
}
#sftp
{
    "name": "*****-*****",
    "host": "******",
    "protocol": "sftp",
    "port": 22,
    "username": "****",
    "password": "**********",
    "remotePath": "C:/**/**/**/**",
    "uploadOnSave": false,
    "useTempFile": false,
    "openSsh": false
}
#Private Key
{
    "name": "*****-*****",
    "host": "******",
    "protocol": "sftp",
    "port": 22,
    "username": "****",
    "privateKeyPath": "C:/**/**/**/**",
    "remotePath": "C:/**/**/**/**",
    "uploadOnSave": false,
    "useTempFile": false,
    "openSsh": false
}
#Remote SSH
```

#### To: .ssh

```ssh
#****-********
Host ********
Hostname ****.****
Identityfile C:\********\****\.ssh\id_rsa
IdentitiesOnly yes
Port 22
User ******
ForwardX11 yes
```
