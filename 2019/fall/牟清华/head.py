# -*- coding: UTF-8 -*-
opcode = {
    "LUI":0x37,
    "AUIPC":0x17,
    "JAL":0x6F,
    "JALR":0x67,
    
    "BEQ":0x63,
    "BNE":0x63|(1<<12),
    "BLT":0x63|(4<<12),
    "BGE":0x63|(5<<12),
    "BLTU":0x63|(6<<12),
    "BGEU":0x63|(7<<12),
        
    #LOAD STORE指令
    "LB":0x03,
    "LH":0x03|(1<<12),
    "LW":0x03|(2<<12),
    "LBU":0x03|(4<<12),
    "LHU":0x03|(5<<12),
    
    "SB":0x23,
    "SH":0x23|(1<<12),
    "SW":0x23|(2<<12),
    
    "ADDI":0x13,
    "SLTI":0x13|(2<<12),
    "SLTIU":0x13|(3<<12),
    "XORI":0x13|(4<<12),
    "ORI":0x13|(6<<12),
    "ANDI":0x13|(7<<12),
    "SLLI":0x13|(1<<12),  
    "SRLI":0x13|(5<<12),
    "SRAI":0x13|(5<<12)|(1<<30),
    
    #整数运算指令
    "ADD":0x33,
    "SUB":0x33|(1<<30),
    "SLL":0x33|(1<<12),
    "SLT":0x33|(2<<12),
    "SLTU":0x33|(3<<12),
    "XOR":0x33|(4<<12),
    "OR":0x33|(6<<12),
    "AND":0x33|(7<<12),
    "SRL":0x33|(5<<12),
    "SRA":0x33|(5<<12)|(1<<30),
    
    "FENCE":0x0F,
    "FENCE_I":0x0F|(1<<12),
    
    "ECALL":0x73,
    "EBREAK":0x73|(1<<20),
    "CSRRW":0x73|(1<<12),
    "CSRRS":0x73|(2<<12),
    "CSRRC":0x73|(3<<12),
    "CSRRWI":0x73|(5<<12),
    "CSRRSI":0x73|(6<<12),
    "CSRRCI":0x73|(7<<12)
}
