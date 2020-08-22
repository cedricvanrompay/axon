# Axon - Synapse admin CLI

## Setup

Clone the repository:

```
git clone https://forge.tedomum.net/tedomum/axon.git
```

Create a virtual environment and install requirements:

```
virtualenv -p python3 venv
source bin/venv/activate
pip install -r requirements.txt
```

## Usage

Set configuration environment variables:

```
export AXON_HOMESERVER=https://homeserver.url
export AXON_TOKEN=M......x
```

You can obtain an admin Matrix token from any Matrix client.

Get all commands using `--help`:

```
python -m axon.cli --help
python -m axon.cli user --help
python -m axon.cli room --help
```
