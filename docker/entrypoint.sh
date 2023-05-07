#!/bin/bash
cd src
uvicorn app:app --host 0.0.0.0 --port 1234 --reload
exec "$@"
