#/bin/env - bash
echo "WARNING : Please run this command in the folder where the project is present"
echo "Press CTRL + C to cancel"
echo "Running in 3..."
sleep 1
echo "Running in 2..."
sleep 1
echo "Running in 1..."
sleep 1
echo "installing dependencies"
apt update
apt install -y python3 python3-venv curl zstd git
echo "Creating python3 environment"
python3 -m venv venv
source venv/bin/activate
echo "Installing demo program dependencies"
pip3 install -r requirements-demo.txt
echo "installing ollama (This will take a lot of time)"
curl -fsSL https://ollama.com/install.sh | sh
echo "starting ollama"
service ollama start
echo "Pulling ollama demo embedding model (this will take a lot of time)"
ollama pull nomic-embed-text
echo "Downloading the project with demo"
git clone https://github.com/Koshin-S-Hegde/manvitha/
echo "Installation complete :3"
echo "Further instructions :"
echo "Run this command : cd manvitha"
echo "Run this command after the previous command : python3 demo.py"
