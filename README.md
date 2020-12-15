# Axon - Synapse admin CLI

Axon uses the Synapse admin API as described here: https://github.com/matrix-org/synapse/tree/master/docs/admin_api

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

## Examples

Display any room matching the "test" search string:

```
python -m axon.cli room list --search test | jq
```

List rooms that a user belongs to:

```
python -m axon.cli user get @admin:tedomum.net | jq .joined_rooms
```

Delete every room that a user belongs to:

```
python -m axon.cli user get @kaiyou:tedomum.net | jq -r '.joined_rooms[]' | python -m axon.cli room delete
```
