
mkdir ~/Datacube
sudo mkdir -p /datacube/{original_data,ingested_data}
sudo chmod -R 777 /datacube/
sudo apt-get install -y python3-pip
sudo pip3 install virtualenv
virtualenv ~/Datacube/datacube_env

alias dcenv='source ~/Datacube/datacube_env/bin/activate && python -V'

echo alias dcenv='source ~/Datacube/datacube_env/bin/activate && python -V'
