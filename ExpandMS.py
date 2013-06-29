#!/usr/bin/env python
X=5

def fetch_ms(fp):
	ms=[[0 for i in range(X)]for j in range(X)]
	for i in range(X):
		s=fp.readline()
		if s[0]=='':
			return None
		elif s[0]=='-':
			s=fp.readline()
		s=s.split()
		for j in range(X):
			ms[i][j]=int(s[j])
	return ms

def pf_ms(ms, fp):
	for i in range(X):
		for j in range(X):
			fp.write('%3d'%(ms[i][j]))
		fp.write('\n')
	fp.write('-'*12 + '\n')

def copy_ms(destms, ms):
	for i in range(X):
		for j in range(X):
			destms[i][j]=ms[i][j]

def ms_rotate_righ(ms):
	resms=[[0 for i in range(X)]for j in range(X)]
	for i in range(X):
		for j in range(X):
			resms[i][j]=ms[X-1-i][j]
	copy_ms(ms, resms)

def pf_ms_rotating(ms, outfp):
	for i in range(4):
		pf_ms(ms, outfp)
		ms_rotate_righ(ms)

def reverse_ms(ms):
	tmpms=[[0 for i in range(X)]for j in range(X)]
	copy_ms(tmpms, ms)
	for i in range(X):
		for j in range(X):
			ms[i][j]=tmpms[X-1-i][X-1-j]

def mine():
	fp=open('ms%d.txt'%(X), 'r')
	outfp=open('ms%d-FULL.txt'%(X), 'w')
	while True:
		ms=fetch_ms(fp)
		if ms==None:
			break
		pf_ms_rotating(ms, outfp)
		reverse_ms(ms)
		pf_ms_rotating(ms, outfp)
	fp.close()
	outfp.close()

if __name__=='__main__':
	mine()
