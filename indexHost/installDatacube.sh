sudo apt-get install git


cd ~/Datacube
git clone https://github.com/ceos-seo/agdc-v2.git -b master
git clone https://github.com/ceos-seo/data_cube_ui.git -b master
git clone https://github.com/ceos-seo/data_cube_notebooks.git -b master
cd ~/Datacube/data_cube_ui
git submodule init && git submodule update
cd ~/Datacube/data_cube_notebooks
git submodule init && git submodule update

