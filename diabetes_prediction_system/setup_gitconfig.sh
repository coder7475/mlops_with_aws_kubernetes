#!/bin/bash
# setup_git_config.sh
# Configure Git user identity (global)

# Set Git user configuration globally
git config --global user.name "coder7475"
git config --global user.email "robiulhossain7475@gmail.com"

# Optional: set default branch name to main
git config --global init.defaultBranch main

# Optional: enable credential caching (15 minutes)
git config --global credential.helper 'cache --timeout=900'

echo "✅ Git global configuration has been set successfully!"
echo
echo "Current Git configuration:"
git config --list | grep 'user\|init.defaultBranch\|credential.helper'
