# ex2
# 문자를 유니코드로 변환

a = ord('a')
print(a)
a = ord('A')
print(a)

mark = 0x0F
print(mark)
print("%x & %x = %x" %(a, mark, a & mark))
print("%X & %X = %X" %(a, mark, a | mark))

mask = ord('a') - ord('A')
print(mask)

b = a ^ mask
print("%c ^ %d = %c" %(a, mask, b))
a = b ^ mask
print("%c ^ %d = %c" %(b, mask, a))
