import sys
import binascii

from opcode_table import opcodeTable
from opcode_args_table import opcodeArgsTable


def main() :
	if len(sys.argv) < 2:
		print "Incorrect arguements."
		exit()

	filePath = sys.argv[1]
	assemblyInstructions = generateAssembly(filePath)
	for instruction in assemblyInstructions:
		print instruction
	

def generateAssembly(filePath):
	assemblyInstructions = []
	with open(filePath, "rb") as f:
		programCounter = 0x200
		opcode = f.read(2)
		while opcode:
			hexOpcode = binascii.hexlify(opcode)
			opcodeInstruction = lookupOpcode(int(hexOpcode, 16))
			opcodeArgsList = findOpcodeArgs(int(hexOpcode, 16))
			opcodeArgs = ""
			for arg in opcodeArgsList:
				opcodeArgs += arg + ", "
			opcodeArgs = opcodeArgs[ : -2]
			assemblyInstructions.append(hex(programCounter) + ":\t" + hexOpcode + "\t\t" + opcodeInstruction + "\t" + opcodeArgs)
			programCounter += 2;
			opcode = f.read(2)
	return assemblyInstructions

def maskOpcode(opcode):
	if (opcode & 0xF000) in [0x0000, 0xE000, 0xF000]:
		opcode &= 0xF0FF
	elif (opcode & 0xF000) in [0x8000]:
		opcode &= 0xF00F
	else:
		opcode &= 0xF000
	return opcode

def lookupOpcode(opcode):
	opcode = maskOpcode(opcode)
	return opcodeTable.get(opcode, "???");

def findOpcodeArgs(opcode):
	maskedOpcode = maskOpcode(opcode)
	return opcodeArgsTable.get(maskedOpcode)(opcode)


if __name__ == '__main__':
	main()