
mkdir $1
cd $1
touch index.py
touch README.md
touch input.txt
touch output.txt
echo "import sys\nsys.stdin = open('./$1/input.txt', 'r')\nsys.stdout = open('./$1/output.txt', 'w')\n" >> index.py
cd ..
