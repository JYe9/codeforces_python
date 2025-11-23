#!/bin/bash
# Setup script for Codeforces Python environment

echo "Setting up Codeforces Python environment..."

# Check if conda is installed
if ! command -v conda &> /dev/null
then
    echo "Error: conda is not installed!"
    echo "Please install Anaconda or Miniconda first."
    echo "Visit: https://docs.conda.io/en/latest/miniconda.html"
    exit 1
fi

# Create conda environment
echo "Creating conda environment 'codeforces'..."
conda env create -f environment.yml

# Activate environment
echo ""
echo "Environment created successfully!"
echo ""
echo "To activate the environment, run:"
echo "  conda activate codeforces"
echo ""
echo "To deactivate, run:"
echo "  conda deactivate"
echo ""
echo "Setup complete! Happy coding!"

