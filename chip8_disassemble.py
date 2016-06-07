import sys
import binascii

from opcode_table import opcodeTable

def main() :
	if len(sys.argv) < 2:
		print "Incorrect arguements."
		exit()

	filePath = sys.argv[1]
	with open(filePath, "rb") as f:
		opcode = f.read(2)
		while opcode:
			hexOpcode = binascii.hexlify(opcode)
			opcodeInstruction = lookupOpcode(int(hexOpcode, 16))
			print hexOpcode + " : " + opcodeInstruction
			opcode = f.read(2)


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


if __name__ == '__main__':
	main()