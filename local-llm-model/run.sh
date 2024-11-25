#!/bin/sh

set -e

# Run the app
exec uvicorn main:app --reload