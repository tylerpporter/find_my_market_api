#! /usr/bin/env bash
export DATABASE_URL="postgresql://postgres@localhost/market_api_test"
pytest -s --cov=app --cov-report=html
