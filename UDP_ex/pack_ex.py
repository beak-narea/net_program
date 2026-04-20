import struct

class Udphdr:
    def __init__(self, src_port, dst_port, length, checksum):
        self.src_port = src_port
        self.dst_port = dst_port
        self.length = length
        self.checksum = checksum

    def pack_Udphdr(self):
        packed = struct.pack('!4H', self.src_port, self.dst_port, self.length, self.checksum)
        return packed
    
    def unpack_Udphdr(buffer):
        unpacked = struct.unpack('!4H', buffer)
        return unpacked
    
    def getSrcPort(unpacked_Udphdr):
        return unpacked_Udphdr[0]
    
    def getDestPort(unpacked_Udphdr):
        return unpacked_Udphdr[1]
    
    def getLength(unpacked_Udphdr):
        return unpacked_Udphdr[2]
    
    def getChecksum(unpacked_Udphdr):
        return unpacked_Udphdr[3]
    
udp = Udphdr(5555, 80, 1000, 0xFFFF)
packed_udp = udp.pack_Udphdr()
print(packed_udp)
print("b'"+str(packed_udp.hex()))
unpacked_udp = Udphdr.unpack_Udphdr(packed_udp)
print(unpacked_udp)
print(f"Source Port: {Udphdr.getSrcPort(unpacked_udp)} Destination: {Udphdr.getDestPort(unpacked_udp)} Length: {Udphdr.getLength(unpacked_udp)} Checksum: {Udphdr.getChecksum(unpacked_udp)}")