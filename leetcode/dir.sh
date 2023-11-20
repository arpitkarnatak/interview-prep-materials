
mkdir leetcode_$1
cd leetcode_$1
touch index.py
touch input.txt
touch output.txt
echo "import sys\nsys.stdin = open('./leetcode_$1/input.txt', 'r')\nsys.stdout = open('./leetcode_$1/output.txt', 'w')\n" >> index.py
cd ..
