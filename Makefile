# Makefile for the website
.PHONY: start dev install

# Plain static server (no auto-reload)
start:
	python3 -m http.server 8000

# Install dev tools once (live reload)
install:
	npm install

# Local preview with auto-reload when HTML/CSS/JS change
node_modules: package.json
	npm install

dev: node_modules
	npm run dev