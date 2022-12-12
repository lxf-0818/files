def toAscii(binary_int): 
	# hack from https://www.geeksforgeeks.org/python-program-to-convert-binary-to-ascii/
	# Getting the byte number
	byte_number = binary_int.bit_length() + 7 // 8
 
	# Getting an array of bytes
	binary_array = binary_int.to_bytes(byte_number, "big")
 
	# Converting the array into ASCII text
	ascii_text = binary_array.decode()
 
	# Getting the ASCII value
	print(ascii_text,end="")

with open('foo_asc.txt') as f:
	
	while True:
		line = f.read(8)
		if  len(line) < 8:  # eof(0x0a)?
			print()
			break			# bye
		toAscii(int(line.strip(),2))
