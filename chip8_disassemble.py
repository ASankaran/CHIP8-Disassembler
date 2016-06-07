import sys
import binascii


def main() :
	if len(sys.argv) < 2:
		print "Incorrect arguements."
		exit()

	filePath = sys.argv[1]
	with open(filePath, "rb") as f:
		opcode = f.read(2)
		while opcode:
			hexOpcode = binascii.hexlify(opcode)
			print hexOpcode
			opcode = f.read(2)

if __name__ == '__main__':
	main()