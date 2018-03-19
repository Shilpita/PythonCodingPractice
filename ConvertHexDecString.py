
def HexStr2Bin(hexstring, separator='-'):
  """Python function to convert a hexadecimal string into a binary stream."""
  if not separator:
    raise ValueError('Missing separator.')
  bytestring = ''
  for hexchar in hexstring.split(separator):
    bytestring += hexchar.decode('hex')

  return bytestring


def HexStr2Guid(hexstring, separator=' '):
  """Python function to convert a hexadecimal string into a GUID string."""
  if not separator:
    raise ValueError('Missing separator.')
  hexlist = [int(x, 16) for x in hexstring.split(separator)]
  return '{3:02x}{2:02x}{1:02x}{0:02x}-{5:02x}{4:02x}-{7:02x}{6:02x}' \
         '-{8:02x}{9:02x}-{10:02x}{11:02x}{12:02x}{13:02x}{14:02x}{15:02x}'.format(*hexlist)


if __name__ == '__main__':
   # print(MACprettyprint(randomMAC()))
    print(HexStr2Bin('34ffed35','-'))