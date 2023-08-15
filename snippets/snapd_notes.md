systemctl enable --now snapd
ln -s /var/lib/snapd/snap /snap

snap install firefox
snap install --classic code
