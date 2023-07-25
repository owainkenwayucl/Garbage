# Docker VM

Install AlmaLinux 9.2 then...


```
dnf install yum-utils
```
(this step may be unnecessary?)


Then:

```
dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo
dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Make sure Repo key matches:

```
060A 61C5 1B55 8A7F 742B 77AA C52F EB6B 621E 9F35
```
