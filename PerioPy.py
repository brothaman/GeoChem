#!/usr/bin/env python
""" periodic table - interactive periodic table for use of element identification or formula mass calculation"""
'''
Objective Functionality:
	Calculate Molar Mass
	Calculate Mass Composition
	Identify Functional Groups
	Predict Molecular Geometry
	Predict Macro structure i.e. polymeric, metallic, crystalline and Theoretical Moduli associated with them
	[('1s2'),('2s2','2p6'),('3s2','3p6','3d10'),('4s2','4p6','4d10','4f14'),('5s2','5p6','5d10','5f14'),('6s2','6p6','6d10','6f14'),('7s2','7p6','7d10','7f14')]
	[('1s2'),('2s2','2p6'),('3s2','3p6','3d10'),('4s2','4p6','4d10','4f14'),('5s2','5p6','5d10','5f14'),('6s2','6p6','6d10'),('7s2','7p6')]
	[(2),(2,6),(2,6,10),(2,6,10,14),(2,6,10,14),(2,6,10,14),(2,6,10,14)]
	[s,p,d,f]
'''
# Electronic Configurations
HELI = [('1s',2)]
NEON = HELI + [('2s',2),('2p',6)]
ARGO = NEON + [('3s',2),('3p',6)]
KRYP = ARGO + [('3d',10),('4s',2),('4p',6)]
XEON = KRYP + [('4d',10),('5s',2),('5p',6)]
RADO = XEON + [('4f',14),('5d',10),('6s',2),('6p',6)]
UNUN = RADO + [('5f',14),('6d',10),('7s',2),('7p',6)]
# Periodic table dict
Elements = dict(Ac=('Actinium', 89, 227, RADO + [('6d',1),('7s',2)], ),
                Al=('Aluminum', 13, 26.981539, NEON + [('3s',2),('3p',1)], ),
                Am=('Americium', 95, 243, RADO + [('5f',6),('6d',1),('7s',2)], ),
                Sb=('Antimony', 51, 121.75, KRYP + [('4s',10),('5s',2),('5p',3)], ),
                Ar=('Argon', 18, 39.948, ARGO, ),
                As=('Arsenic', 33, 74.92159, ARGO + [('3d',10),('4s',2),('4p',3)], ),
                At=('Astatine', 85, 210, XEON + [('4f',14),('5d',10),('6s',2),('6p',5)], ),
                Ba=('Barium', 56, 137.327, XEON + [('6s',2)], ),
                Bk=('Berkelium', 97, 247, RADO + [('5f',8),('6d',1),('7s',2)] , ),
                Be=('Beryllium', 4, 9.012182, HELI + [('2s',2)], ),
                Bi=('Bismuth', 83, 208.98037, XEON + [('4f',14),('5d',10),('6s',2),('6p',3)], ),
                Bh=('Bohrium', 107, 264, RADO + [('5f',14),('6d',5),('7s',2)], ),
                B=('Boron', 5, 10.811, HELI + [('2s',2),('2p',1)], ),
                Br=('Bromine', 35, 79.904, ARGO + [('3d',10),('4s',2),('4p',5)], ),
                Cd=('Cadmium', 48, 112.411, KRYP + [('4d',10),('5s',2)], ),
                Ca=('Calcium', 20, 40.078, ARGO + [('4s',2)], ),
                Cf=('Californium', 98, 251, RADO + [('5f',9),('6d',1),('7s',2)], ),
                C=('Carbon', 6, 12.011, HELI + [('2s',2),('2p',2)], ),
                Ce=('Cerium', 58, 140.116, XEON + [('4f',1),('5d',1),('6s',2)], ),
                Cs=('Cesium', 55, 13.90543, XEON + [('6s',1)], ),
                Cl=('Chlorine', 17, 35.4527, NEON + [('3s',2),('3p',5)], ),
                Cr=('Chromium', 24, 51.9961, ARGO + [('3d',4),('4s',2)], ),
                Co=('Cobalt', 27, 58.93320, ARGO + [('3d',7),('4s',2)], ),
                Cu=('Copper', 29,63.546, ARGO + [('3d',9),('4s',2)], ),
                Cm=('Curium', 96, 247, RADO + [('5f',7),('6d',1),('7s',2)], ),
                Ds=('Darmstadtium', 110, 281, RADO + [('5f',14),('6d',8),('7s',2)], ),
                Db=('Dubnium', 105, 262, RADO + [('5f',14),('6d',3),('7s',2)], ),
                Dy=('Dysprosium', 66, 162.50, XEON + [('4f',9),('5d',1),('6s',2)], ),
                Es=('Einsteinium', 99, 252, RADO + [('5f',10),('6d',1),('7s',2)], ),
                Er=('Erbium', 68, 167.26, XEON + [('4f',11),('5d',1),('6s',2)], ),
                Eu=('Europium', 63, 151.965, XEON + [('4f',6),('5d',1),('6s',2)], ),
		Fm=('Fermium', 100, 257, RADO + [('5f',11),('6d',1),('7s',2)], ),
                F=('Fluorine', 9, 18.9984032, HELI + [('2s',2),('2p',5)], ),
                Fr=('Francium', 87, 223, RADO + [('7s',1)], ),
                Gd=('Gadolinum', 64, 157.25, XEON + [('4f',7),('5d',1),('6s',2)], ),
                Ga=('Gallium', 31, 69.723, ARGO + [('3d',10),('4s',2),('4p',1)], ),
                Ge=('Germanium', 32, 72.61, ARGO + [('3d',10),('4s',2),('4p',2)], ),
                Au=('Gold', 79, 196.96654, XEON + [('4f',14),('5d',9),('6s',2)], ),
                Hf=('Hafnium', 72, 178.49, XEON + [('4f',14),('5d',2),('6s',2)], ),
                Hs=('Hassium', 108, 277, RADO + [('5f',14),('6d',6),('7s',2)], ),
                He=('Helium', 2, 4.0020602, HELI, ),
                Ho=('Holmium', 67, 164.93032, XEON + [('4f',10),('5d',1),('6s',2)], ),
                H=('Hydrogen', 1, 1.00794, [('1s',1)], ),
                In=('Indium', 49, 114.82, KRYP + [('4d',10),('5s',2),('5p',1)], ),
                I=('Iodine', 53, 126.90447, KRYP + [('4d',10),('5s',2),('5p',5)], ),
                Ir=('Iridium', 77, 192.22, XEON + [('4f',14),('5d',7),('6s',2)], ),
                Fe=('Iron', 26, 55.847, ARGO + [('3d',6),('4s',2)], ),
                Kr=('Krypton', 36, 83.80, KRYP, ),
                La=('Lanthanum', 57, 138.9055, XEON + [('5d',1),('6s',2)], ),
                Lr=('Lawrencium', 103, 262, RADO + [('5f',14),('6d',1),('7s',2)], ),
                Pb=('Lead', 82, 207.2, XEON + [('4f',14),('6d',10),('7s',2),('7p',2)], ),
                Li=('Lithium', 3, 6.941, HELI + [('1s',1)], ),
                Lu=('Lutetium', 71, 174.967, XEON + [('4f',14),('5d',1),('6s',2)], ),
                Mg=('Magnesium', 12, 24.3050, NEON + [('3s',2)], ),
                Mn=('Manganese', 25, 54.93805, ARGO + [('4s',2),('3d',5)], ),
                Mt=('Meitnerium', 109, 268, RADO + [('5f',14),('6d',7),('7s',2)], ),
                Md=('Mendelevium', 101, 258, RADO + [('5f',12),('6d',1),('7s',2)], ),
                Hg=('Mercury', 80, 200.59, XEON + [('4f',14),('5d',10),('6s',2)], ),
                Mo=('Molybdenum', 42, 95.94, KRYP + [('4d',4),('5s',2)], ),
                Nd=('Neodymium', 60, 144.24, XEON + [('4f',3),('5d',1),('6s',2)], ),
                Ne=('Neon', 10, 20.1797, NEON, ),
                Np=('Neptunium', 93, 237, RADO + [('5f',4),('6d',1),('7s',2)], ),
                Ni=('Nickel', 28, 58.69, ARGO + [('3d',8),('4s',2)], ),
                Nb=('Niobium', 41, 92.90638, KRYP + [('4d',3),('5s',2)], ),
                N=('Nitrogen', 7, 14.00674, HELI + [('2s',2),('2p',3)], ),
                No=('Nobelium', 102, 259, RADO + [('5f',13),('6d',1),('7s',2)], ),
                Os=('Osmium', 76, 190.2, XEON + [('4f',14),('5d',6),('6s',2)], ),
                O=('Oxygen', 8, 15.9994, HELI + [('2s',2),('2p',4)], ),
                Pd=('Palladium', 46, 105.42, KRYP + [('4d',8),('5s',2)], ),
                P=('Phosphorus', 15, 30.973762, NEON + [('3s',2),('3p',3)], ),
                Pt=('Platinum', 78, 195.08, XEON + [('4f',14),('5d',8),('6s',2)], ),
                Pu=('Plutonium', 94, 244, RADO + [('5f',5),('6d',1),('7s',2)], ),
                Po=('Polonium', 84, 209, XEON + [('4f',14),('5d',10),('6s',2),('6p',4)], ),
                K=('Potassium', 19, 39.0983, ARGO + [('4s',1)], ),
                Pr=('Praseodymium', 59, 140.90765, XEON + [('4f',2),('5d',1),('6s',2)], ),
                Pm=('Promethium', 61, 145, XEON + [('4f',4),('5d',1),('6s',2)], ),
                Pa=('Protactium', 91, 231.03588, RADO + [('5f',2),('6d',1),('7s',2)], ),
                Ra=('Radium', 88, 226, RADO + [('7s',2)], ),
                Rn=('Radon', 86, 222, RADO, ),
                Re=('Rhenium', 75, 186.207, XEON + [('4f',14),('5d',5),('6s',2)], ),
                Rh=('Rhodium', 45, 102.90550, KRYP + [('4d',7),('5s',2)], ),
                Rb=('Rubidium', 37, 85.4678, KRYP + [('5s',1)], ),
                Ru=('Ruthenium', 44, 101.07, KRYP + [('4d',6),('5s',2)], ),
                Rf=('Rutherfordium', 104, 261, RADO + [('5f',14),('6d',2),('7s',2)], ),
                Sm=('Samarium', 62, 150.36, XEON + [('4f',5),('5d',1),('6s',2)], ),
                Sc=('Scandium', 21, 44.955910, ARGO + [('3d',1),('4s',2)], ),
                Sg=('Seaborgium', 106, 266, RADO + [('5f',14),('6d',4),('7s',2)], ),
                Se=('Selenium', 34, 78.96, ARGO + [('3d',10),('4s',2),('4p',4)], ),
                Si=('Silicon', 14, 28.0855, NEON + [('3s',2),('3p',2)], ),
                Ag=('Silver', 47, 107.8682, KRYP + [('4d',9),('5s',2)], ),
                Na=('Sodium', 11, 22.989768, NEON + [('3s',1)], ),
                Sr=('Strontium', 38, 87.62, KRYP + [('5s',2)], ),
                S=('Sulfur', 16, 32.066, NEON + [('3s',2),('3p',4)], ),
                Ta=('Tantalum', 73, 180.9479, XEON + [('4f',14),('5d',3),('6s',2)], ),
                Tc=('Technetium', 43,98, KRYP + [('4d',5),('5s',2)], ),
                Te=('Tellurium', 52, 127.60, KRYP + [('4d',10),('5s',2),('5p',4)], ),
                Tb=('Terbium', 65, 158.92543, XEON + [('4f',8),('5d',1),('6s',2)], ),
                Tl=('Thallium', 81, 204.3833, XEON + [('4f',14),('5d',10),('6s',2),('6p',1)], ),
                Th=('Thorium', 90, 232.0381, RADO + [('5f',1),('6d',1),('7s',2)], ),
                Tm=('Thulium', 69, 168.93421, XEON + [('4f',12),('5d',1),('6s',2)], ),
                Sn=('Tin', 50, 118.710, KRYP + [('4d',10),('5s',2),('5p',2)], ),
                Ti=('Titanium', 22, 47.88, ARGO + [('3d',2),('4s',2)], ),
                W=('Tungsten', 74, 183.85, XEON + [('4f',14),('5d',4),('6s',2)], ),
                Uub=('Ununbium', 112, 285, RADO + [('5f',14),('6d',10),('7s',2)], ),
                Uuh=('Ununhexium', 116, 293, RADO + [('5f',14),('6d',10),('7s',2),('7p',4)], ),
                Uuo=('Ununoctium', 118, 294, UNUN, ),
                Uup=('Ununpentium', 115, 288, RADO + [('5f',14),('6d',10),('7s',2),('7p',3)], ),
                Uuq=('Ununquadium', 114, 289, RADO + [('5f',14),('6d',10),('7s',2),('7p',2)], ),
                Uus=('Ununseptium', 117, 294, RADO + [('5f',14),('6d',10),('7s',2),('7p',5)], ),
                Uut=('Ununtrium', 113, 284, RADO + [('5f',14),('6d',10),('7s',2),('7p',1)], ),
                Uuu=('Ununium', 111, 280, RADO + [('5f',14),('6d',9),('7s',2)], ),
                U=('Uranium', 92, 238.0289, RADO + [('5f',3),('6d',1),('7s',2)], ),
                V=('Vanadium', 23, 50.9415, ARGO + [('3d',3),('4s',2)], ),
                Xe=('Xenon', 54, 131.29, XEON, ),
                Yb=('Ytterbium', 70, 173.04, XEON + [('4f',13),('5d',1),('6s',2)], ),
                Y=('Yttrium', 39, 88.90585, KRYP + [('4d',1),('5s',2)], ),
                Zn=('Zinc', 30, 65.39, ARGO + [('3d',10),('4s',2)], ),
                Zr=('Zirconium', 40, 91.224, KRYP + [('4d',2),('5s',2)], ),
                )

import sys, re

# user inputs to call specific element identities
def info(element):
	for element in Elements:
		val = 0
		for orbital in Elements[element][3]:
			val = val + orbital[1]
		if val != Elements[element][1]:
			print element
#	print '\n%s has %s protons and a Molar Mass of %s \n' %Elements[element]

# string to number
def sTn(a):
	if a.isdigit():
		return int(a)
	else:
		return a
# capability to replace brackets with in brackets
def resolve(compound):
	polyIon = '\[[^\[][^\]][A-Za-z0-9]*\][0-9]*'
	polyMatch = re.findall(polyIon,compound)
	while polyMatch:
		for val in polyMatch:
			val1 = val.replace('[','\[')
			val1 = val1.replace(']','\]')
			compound = re.sub(val1,extract(val),compound)
		polyMatch = re.findall(polyIon,compound)
	return extract(compound)
# extract polyatomic ion
def extract(compound):
	polyIon = '\[[a-zA-Z0-9]*\][0-9]*'
	a = '[0-9]+$'
	atom_match = '[A-Z][a-z]*[0-9]*'
	coeff, elem, atoms = [], [], []
	polyVec = re.findall(polyIon,compound)
	compound = re.sub(polyIon,'', compound)
	# multiply coefficients by the outer coefficients
	for ion in polyVec:
		if re.search(a,ion):
			co = re.search(a,ion).group()
		else:
			co = '1'
		ion = re.sub(a,"", ion)
		ion = re.sub('\[|\]','',ion)
		atoms = re.findall(atom_match, ion)
		for atom in atoms:
			# loop through atom and right subscript exist multiply it by outer most parenthetic subscript
			if re.search(a,atom):
				match = re.search(a, atom)
				atom = re.sub(a,str(int(match.group())*sTn(co)),atom)
			else:
				atom = atom + '%s'%co
			compound = compound + atom
	# now loop through an find all atoms with out shown subscript and re-write compound with implied ones in place
	atoms = re.findall(atom_match,compound)
	compound  = ''

	for atom in atoms:
		if not re.search(a,atom):
			atom = atom + '1'
		compound = compound + atom
	return compound
# deconstruct 
#def deconstruct(compound):
def percent_comp(compound):
	emperical = resolve(compound)
	elems = re.findall('[A-Z][a-z]*[0-9]*', emperical)
	atom_match = '[A-Z][a-z]*'
	atoms = [re.search(atom_match,elem).group() for elem in elems]
	elements = []
	emp_subs = []
	mass = []
	for atom in atoms:
		if atom not in elements:
			elements.append(atom)
	for element in elements:
		val = 0
		for elem in elems:
			if re.search(atom_match, elem).group() == element:
				val = val + int(re.search('[0-9]*$',elem).group())
		emp_subs.append(val)
	empire = [ (elements[i], emp_subs[i]) for i in range(len(elements))]
	# determine molar composition
	mole = [(val[0], float(val[1])/sum(emp_subs)) for val in empire ]
	mass = [(val[0], float(Elements[val[0]][2])*val[1]/formula_mass(compound)) for val in empire]
	percent_mass_n_mole = [(mole[i][0], emp_subs[i], 100*mass[i][1], 100*mole[i][1]) for i in range(len(mole)) ]
	return percent_mass_n_mole
#	for val in empire:
#		mass.append((val[0], val[1]/sum(emp_subs)
# capability for determining formula mass of compound and elemental ratios
def formula_mass(compound):
	emperical = resolve(compound)
	atom_match = '[A-Z][a-z]*[0-9]*'
	elem_match, subscript_match = '^[A-Z][a-z]*', '[0-9]+$'
	atoms = re.findall(atom_match, emperical)
	mass = 0
	for atom in atoms:
		elem = re.search(elem_match,atom).group()
		subscript = re.search(subscript_match, atom).group()
		mass = mass + Elements[elem][2]*int(subscript)
	return mass
	# loop to use functions
def helpout():
	print '''
	To use PerioPy include the {compound} or {element} in braces as shown
	and include options: i, m for info and/or molar mass
	'''
if __name__ == '__main__':
	compMatch = '\{.*\}'
	clean = '\{|\}'
	compound_vec = []
	for val in sys.argv:
		if re.match(compMatch, val):
			val = re.sub(clean, '', val)
			compound_vec.append(val)
	# task delegation
	while len(sys.argv) > 0:
		if sys.argv[-1][0] == '-':
			for i in range(len(sys.argv[-1])):
				if sys.argv[-1][i] == 'i':
					for compound in compound_vec:
						info(compound)
				elif sys.argv[-1][i] == 'm':
					for compound in compound_vec:
						print '''\nThe Formula Mass of Compound: %s is %s g/mol\n''' %(compound, formula_mass(compound))
				elif sys.argv[-1][i] == 'c':
					for compound in compound_vec:
						print '%s is' %compound
						for val in percent_comp(compound):
							print '    %s%% %s by Mass' %(val[2], Elements[val[0]][0])
						print ''
						for val in percent_comp(compound):
							print '    %s%% %s by Molar Ratio' %(val[3], Elements[val[0]][0])
		elif sys.argv[-1] == 'help':
			helpout()
		sys.argv.pop(-1)
