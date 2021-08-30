## DjangoChannels

### Step1
```
pip install django channels channels_redis
```

### Step2 install docker
```
sudo apt update
sudo apt upgrade
sudo apt install docker.io
```

### important 
Start Docker and enter the following command to enable it after every time the system reboots.
```
sudo systemctl enable --now docker
```

To disable it again, simply type in the following command.
```
$ sudo systemctl disable --now docker
```
### Set user Privilages
```
sudo usermod -aG docker YourUsername

sudo chmod 666 /var/run/docker.sock

docker run -p 6379:6379 -d redis:5

sudo netstat -pna | grep 6379
```