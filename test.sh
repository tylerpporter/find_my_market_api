#! /usr/bin/env bash
export DATABASE_URL="postgresql://postgres@localhost/market_api_test"
export PYTHONPATH="$PYTHONPATH:/users/zachholcomb/turing/4module/find_market/find_my_market_api"
pytest -s --cov=app --cov-report=html
