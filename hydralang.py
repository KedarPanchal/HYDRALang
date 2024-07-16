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
                    head_idx = head_idx - 1 if head_idx > 0 else len(heads) - 1
                case '[':
                    if heads[head_idx] >= 0b10000000:
                        bracket_stack.append(i)
                    else:
                        bracket_count = 1
                        i_start = i
                        for j in range(i, len(code)):
                            if code[j] == '[':
                                bracket_count += 1
                            elif code[j] == ']':
                                bracket_count -= 1
                            
                            if bracket_count == 0:
                                i = j
                                break
                        if i == i_start:
                            raise SyntaxError(f"Error: Mismatched bracket at command {i}")
                case ']':
                    if len(bracket_stack) == 0:
                        raise SyntaxError(f"Error: Mismatched bracket at command {i}")
                    elif heads[head_idx] >= 0b10000000:
                        i = bracket_stack.pop() - 1                      
                case _:
                    continue
            i += 1
    except SyntaxError as e:
        print(e.message, file=sys.stderr)

if __name__ == "__main__":
    main()
