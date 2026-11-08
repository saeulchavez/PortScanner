
#!/bin/bash

if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <port> [host]"
    exit 2
fi

PORT="$1"
HOST="${2:-127.0.0.1}"

if ! [[ "$PORT" =~ ^[0-9]+$ ]] ||
   [ "$PORT" -lt 1 ] ||
   [ "$PORT" -gt 65535 ]; then
    echo "ERROR: Invalid port"
    exit 2
fi

if timeout 3 bash -c 'echo > /dev/tcp/$1/$2' _ "$HOST" "$PORT" 2>/dev/null; then
    echo "OPEN: $HOST:$PORT"
    exit 0
else
    echo "CLOSED: $HOST:$PORT"
    exit 1
fi
