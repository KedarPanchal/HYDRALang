import sys
from hydraexceptions import SyntaxError

def main():
    code = sys.stdin.read().strip() if len(sys.argv) < 2 else sys.argv[1]
    heads = [0b00000000]
    head_idx = 0

    bracket_stack = []

    i = 0
    try:
        while i < len(code):
            match code[i]:
                case '-':
                    heads[head_idx] = heads[head_idx] ^ 0b10000000
                case ';':
                    heads[head_idx] = ((heads[head_idx] << 1) & 0b11111111) | ((heads[head_idx] & 0b10000000) >> 7)
                case '%':
                    heads.append(heads[head_idx])
                case '>':
                    head_idx = 0 if (head_idx + 1) == len(heads) else (head_idx + 1)
                case '!':
                    print(chr(heads[head_idx]), end='')
                case '#':
                    del heads[head_idx]
                    if len(heads) == 0:
                        break
                case '[':
                    bracket_stack.append(i)
                case ']':
                    if len(bracket_stack) == 0:
                        raise SyntaxError(f"Error: Mismatched bracket at command {i}")
                    elif heads[head_idx] >= 0b10000000:
                        i = bracket_stack.pop() - 1                      
                case _:
                    if not code[i].isspace():     
                        raise SyntaxError(f"Error at command {i}: Command {code[i]} not supported")
            i += 1
    except SyntaxError as e:
        print(e.message, file=sys.stderr)

if __name__ == "__main__":
    main()
