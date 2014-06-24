#########################################################################
# File Name: dict.py
# Author: WangWeilong
# Company: Baidu
#########################################################################
#!/home/work/safe_psqa/python/bin/python
# coding=utf-8

first = [1,2,3,4]
second = [11,12,13,14]
third = [21,22,23,24]
forth = [31,32,33,34]
ab = {
		'Aa' : first,
		'Bb' : second,
		'Cc' : third,
		'Dd' : forth
}

cd ={
		'Aa' : '',
		'Bb' : third
}

dd='Ee'

def test(str, dict):
	print dict[str]

print ab.get('Aa')
print ab['Aa']
ab['Fire'] = 'fire!'
print ab['Fire']
ab['Aa'].append(5)
print ab['Aa']
if 'Ee' in ab:
	ab['Ee'].append(41)
else:
	ab.setdefault('Ee',[41])
	print type(ab['Ee'])
print ab['Ee']
ab['Ee'].append(42)
print ab['Ee']
ab['Ee'][1] = 55
print ab['Ee']
print len(ab[dd])
ff = 'Fire'
cd={}
cd.setdefault(ab.get(ff), dd)
print cd
print cd[ab.get(ff)]
test(ab.get(ff), cd)
str = "08cdcc84d651e4e504728ae941f7c888"
if cd.get(str) is None:
	cd.setdefault(str, "nice")
print cd
print len(ab)
print len(ab['Aa'])
print len(ab['Bb'])
for x in ab:
	print type(x)
	print x

print cd.get('Aa')
if cd.get('Aa') == "":
	print "yes"
