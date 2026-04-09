#/bin/env - sh
echo "WARNING : Please run this command in the folder where the project is present"
echo "Press CTRL + C to cancel"
echo "Running in 3..."
sleep 1
echo "Running in 2..."
sleep 1
echo "Running in 1..."
sleep 1
echo "installing python3"
apt update
apt install -y python3 python3-venv curl zstd git
echo "installing ollama"
curl -fsSL https://ollama.com/install.sh | sh
echo "starting ollama"
service ollama start
echo "Creating python3 environment"
python3 -m venv venv
source venv/bin/activate
echo "Installing dependencies"
pip install -r requirements-demo.txt
echo "Pulling ollama demo embedding model"
ollama pull nomic-embed-text
echo "Installation complete\a"
echo "Downloading the project with demo"
echo "Run python demo.py to confirm if its working"
