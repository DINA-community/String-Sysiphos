#!bin/usr/bash

uv run python3 lazy.py

sleep 1

rm -rf .venv
rm uv.lock
