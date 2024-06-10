# Create NextCloud Storage
## Requirements
### Hardware
raspberry pi  
Hard Disk  
Home router  
### Softwre
VirtualBox  
ubuntu server  
snap  
nextcloud  
cloudflare or zerotier 
## Install
### Ubuntu server Install
If virtual box is used then create a virtual environment for ubuntu server and install it with nat network so that it will not have any connection to host computer.  
Use entire disk as root dir for ubuntu.  
If raspberry pi is used then use sd card to install ubuntu server or raspberry pi os.
### Install nextCloud
For ubuntu server users
```bash
sudo snap install nextcloud
```
For Debian, raspberry pi os users
```bash
sudo apt install snapd
sudo snap install nextcloud
```
### Install zerotier
If zerotier is used to connect to nextcloud then watch [this](https://www.youtube.com/watch?v=SH00ySqLaqg)  
BUT Zerotier frequently disconnects from proxy network it is very unreliable.

### Install Cloudflare
If zerotier does not work then we can use cloudflare tunnel.  
Main concept is to create temporary tunnel every time the system is rebooted.  
This will create new nextcloud link.  
And this link is then sent via email using connect.py python code.

1. Install cloudflare  
   use [this link](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/downloads/) to download deb package of cloudflare.
   ```bash
   sudo dpkg -i <filename>
   ```
2. clone this repo
   ```bash
   git clone https://github.com/Github-2lu/nextcloud.git
   ```
3. setup connect.py  
   Supposing this git repo is cloned from $HOME dir so inside $HOME/nextcloud connect.py file should be there.  
   Now edit ~/.profiles file in nano
   ```bash
   nano ~/.profiles
   ```
   add these lines in the file
   ```bash
   if [ -f "$HOME/nextcloud/connect.py" ] ; then
      python3 "$HOME/nextcloud/connect.py"
   fi
   ```
   Above code checks if the file exist or not and if exist then run it.  
   Go [here](https://developers.cloudflare.com/pages/how-to/preview-with-cloudflare-tunnel/) to know more about this.

4. Use autologin  
   Go to [this page](https://ostechnix.com/ubuntu-automatic-login/). Here in ubuntu server section follow from step 5
5. Use https  
   [Watch this](https://www.youtube.com/watch?v=p0I8pikm2P4) for more details.  
   But in summary in /var/snap/nextcloud/current/nextcloud/config/config.php file at last add "overwriteprotocol" => "https".  
   WARNING If you do this step then you can't login using the ip address then you must connect using the link sent by connect.py.
