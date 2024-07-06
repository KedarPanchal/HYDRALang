import sys

code = sys.stdin.read().strip() if len(sys.argv) < 2 else sys.argv[1]
print(code)