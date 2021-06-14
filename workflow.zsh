
echo "Process raw data..."

./process.zsh

echo "Parse data..."

python3 getData.py

echo "Build numerical matrix..."

python3 getMatrix.py

echo "Build model..."

python3 getModel.py

