def get0x00E0Args(opcode):
	args = []
	return args

def get0x00EEArgs(opcode):
	args = []
	return args

def get0x0000Args(opcode):
	args = []
	return args

def get0x1000Args(opcode):
	args = []
	args.append(str(hex(opcode & 0x0FFF)))
	return args

def get0x2000Args(opcode):
	args = []
	args.append(str(hex(opcode & 0x0FFF)))
	return args

def get0x3000Args(opcode):
	args = []
	args.append(str(hex((opcode & 0x0F00) >> 8)))
	args.append(str(hex(opcode & 0x00FF)))
	return args

def get0x4000Args(opcode):
	args = []
	args.append(str(hex((opcode & 0x0F00) >> 8)))
	args.append(str(hex(opcode & 0x00FF)))
	return args

def get0x5000Args(opcode):
	args = []
	args.append(str(hex((opcode & 0x0F00) >> 8)))
	args.append(str(hex((opcode & 0x00F0) >> 4)))
	return args

def get0x6000Args(opcode):
	args = []
	args.append(str(hex((opcode & 0x0F00) >> 8)))
	args.append(str(hex(opcode & 0x00FF)))
	return args

def get0x7000Args(opcode):
	args = []
	args.append(str(hex((opcode & 0x0F00) >> 8)))
	args.append(str(hex(opcode & 0x00FF)))
	return args

def get0x8000Args(opcode):
	args = []
	args.append(str(hex((opcode & 0x0F00) >> 8)))
	args.append(str(hex((opcode & 0x00F0) >> 4)))
	return args

def get0x8001Args(opcode):
	args = []
	args.append(str(hex((opcode & 0x0F00) >> 8)))
	args.append(str(hex((opcode & 0x00F0) >> 4)))
	return args

def get0x8002Args(opcode):
	args = []
	args.append(str(hex((opcode & 0x0F00) >> 8)))
	args.append(str(hex((opcode & 0x00F0) >> 4)))
	return args

def get0x8003Args(opcode):
	args = []
	args.append(str(hex((opcode & 0x0F00) >> 8)))
	args.append(str(hex((opcode & 0x00F0) >> 4)))
	return args

def get0x8004Args(opcode):
	args = []
	args.append(str(hex((opcode & 0x0F00) >> 8)))
	args.append(str(hex((opcode & 0x00F0) >> 4)))
	return args

def get0x8005Args(opcode):
	args = []
	args.append(str(hex((opcode & 0x0F00) >> 8)))
	args.append(str(hex((opcode & 0x00F0) >> 4)))
	return args

def get0x8006Args(opcode):
	args = []
	args.append(str(hex((opcode & 0x0F00) >> 8)))
	args.append(str(hex((opcode & 0x00F0) >> 4)))
	return args

def get0x8007Args(opcode):
	args = []
	args.append(str(hex((opcode & 0x0F00) >> 8)))
	args.append(str(hex((opcode & 0x00F0) >> 4)))
	return args

def get0x800EArgs(opcode):
	args = []
	args.append(str(hex((opcode & 0x0F00) >> 8)))
	args.append(str(hex((opcode & 0x00F0) >> 4)))
	return args

def get0x9000Args(opcode):
	args = []
	args.append(str(hex((opcode & 0x0F00) >> 8)))
	args.append(str(hex((opcode & 0x00F0) >> 4)))
	return args

def get0xA000Args(opcode):
	args = []
	args.append("I")
	args.append(str(hex(opcode & 0x0FFF)))
	return args

def get0xB000Args(opcode):
	args = []
	args.append("V0")
	args.append(str(hex(opcode & 0x0FFF)))
	return args

def get0xC000Args(opcode):
	args = []
	args.append(str(hex((opcode & 0x0F00) >> 8)))
	args.append(str(hex(opcode & 0x00FF)))
	return args

def get0xD000Args(opcode):
	args = []
	args.append(str(hex((opcode & 0x0F00) >> 8)))
	args.append(str(hex((opcode & 0x00F0) >> 4)))
	args.append(str(hex(opcode & 0x000F)))
	return args

def get0xE09EArgs(opcode):
	args = []
	args.append(str(hex((opcode & 0x0F00) >> 8)))
	return args

def get0xE0A1Args(opcode):
	args = []
	args.append(str(hex((opcode & 0x0F00) >> 8)))
	return args

def get0xF007Args(opcode):
	args = []
	args.append(str(hex((opcode & 0x0F00) >> 8)))
	args.append("DT")
	return args

def get0xF00AArgs(opcode):
	args = []
	args.append(str(hex((opcode & 0x0F00) >> 8)))
	args.append("K")
	return args

def get0xF015Args(opcode):
	args = []
	args.append("DT")
	args.append(str(hex((opcode & 0x0F00) >> 8)))
	return args

def get0xF018Args(opcode):
	args = []
	args.append("ST")
	args.append(str(hex((opcode & 0x0F00) >> 8)))
	return args

def get0xF01EArgs(opcode):
	args = []
	args.append("I")
	args.append(str(hex((opcode & 0x0F00) >> 8)))
	return args

def get0xF029Args(opcode):
	args = []
	args.append("F")
	args.append(str(hex((opcode & 0x0F00) >> 8)))
	return args

def get0xF033Args(opcode):
	args = []
	args.append("B")
	args.append(str(hex((opcode & 0x0F00) >> 8)))
	return args

def get0xF055Args(opcode):
	args = []
	args.append("[I]")
	args.append(str(hex((opcode & 0x0F00) >> 8)))
	return args

def get0xF065Args(opcode):
	args = []
	args.append(str(hex((opcode & 0x0F00) >> 8)))
	args.append("[I]")
	return args


opcodeArgsTable = {
	0x00E0 : get0x00E0Args,
	0x00EE : get0x00EEArgs,
	0x0000 : get0x0000Args,
	0x1000 : get0x1000Args,
	0x2000 : get0x2000Args,
	0x3000 : get0x3000Args,
	0x4000 : get0x4000Args,
	0x5000 : get0x5000Args,
	0x6000 : get0x6000Args,
	0x7000 : get0x7000Args,
	0x8000 : get0x8000Args,
	0x8001 : get0x8001Args,
	0x8002 : get0x8002Args,
	0x8003 : get0x8003Args,
	0x8004 : get0x8004Args,
	0x8005 : get0x8005Args,
	0x8006 : get0x8006Args,
	0x8007 : get0x8007Args,
	0x800E : get0x800EArgs,
	0x9000 : get0x9000Args,
	0xA000 : get0xA000Args,
	0xB000 : get0xB000Args,
	0xC000 : get0xC000Args,
	0xD000 : get0xD000Args,
	0xE09E : get0xE09EArgs,
	0xE0A1 : get0xE0A1Args,
	0xF007 : get0xF007Args,
	0xF00A : get0xF00AArgs,
	0xF015 : get0xF015Args,
	0xF018 : get0xF018Args,
	0xF01E : get0xF01EArgs,
	0xF029 : get0xF029Args,
	0xF033 : get0xF033Args,
	0xF055 : get0xF055Args,
	0xF065 : get0xF065Args
}
