import time # stopwatch

# vars
memory = [0] * 30
memoryPointer = 0
loopPositions = []
loopAmount = 0
loopStack = []
codePointer = 0
output = ""
overflow = True

try:
    filepath = input("Path of your .bfp2 file?\n> ")
    code = "".join(open(filepath, 'r').readlines())
except:
    print("\nInvalid file/keyboard interrupt\n")
    exit()

# compile stopwatch
startTime = time.time()

# interpreter
while codePointer < len(code):
    cmd = code[codePointer]
    
    match cmd:
        case "+":
            memory[memoryPointer] += 1
            if memory[memoryPointer] > 255 and overflow:
                memory[memoryPointer] = 0

        case "-":
            memory[memoryPointer] -= 1
            if memory[memoryPointer] < 0:
                if overflow:
                    memory[memoryPointer] = 255
                else:
                    memory[memoryPointer] = 0
            
        case ".":
            # print ascii letter of the value of current cell pointer is at
            try:
                charToPrint = chr(memory[memoryPointer])
            except IndexError:
                charToPrint = " "

            print(charToPrint, end="", flush=True)
            
        case ":":
            # print number of current cell
            print(str(memory[memoryPointer]), end="", flush=True)

        case ",":
            # input (hard, because you have to limit to one character and ascii is stupid)

            charInput = input("Input one character: ")
            
            if len(charInput) != 1:
                charInput = chr(0)

            memory[memoryPointer] = ord(charInput)

        case ";":
            # input but number
            try:
                temp = input("Number input: ")
                temp = temp.split(" ")[0]
                temp = int(temp)
            except:
                memory[memoryPointer] = 0
                codePointer += 1
                continue
                
            memory[memoryPointer] = temp

        case ">":
            memoryPointer += 1
            if memoryPointer >= len(memory):
                memory.append(0)
        case "<":
            memoryPointer -= 1

        # the hard part: loops (copied from chatgpt lmao)

        case "[":
            if memory[memoryPointer] == 0:
                # skip loop
                loopAmount = 1
                while loopAmount > 0:
                    codePointer += 1
                    if code[codePointer] == '[':
                        loopAmount += 1
                    elif code[codePointer] == ']':
                        loopAmount -= 1
            else:
                # enter loop
                loopStack.append(codePointer)
        
        case "]":
            if memory[memoryPointer] != 0:
                # go back to to the '['
                codePointer = loopStack[-1]
            else:
                # exit
                loopStack.pop()
                
        case "'":
            overflow = not overflow
            
        case _:
            pass

    codePointer += 1

print(f"\n\nTook {time.time() - startTime} seconds")

temp = input("Show memory? ('yes' if yes, anything else if no)\n> ")
if temp.lower() == "yes":
    print(f"\n\nmemory:\n{memory}\nmemory pointer: {memoryPointer}")

print("\n==========================\n")