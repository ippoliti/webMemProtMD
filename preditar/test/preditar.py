# -*- coding: utf-8 -*-

home_folder = "/home/user/naeem/scikit/new/preditar/"
#home_folder = "C:Users/Sujit/Desktop/preditar/"

import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit import DataStructs
from sklearn.externals import joblib

import argparse
__author__ = 'Naeem Shaikh'

parser = argparse.ArgumentParser(description='PredTar is the script is to identify potential drug target fot given compound/s')
parser.add_argument('-i', '--input', help='input filename containing query compound/s.', required=True)
parser.add_argument('-smi', '--smi', help='flag for smiles string input for query compound/s.', type=int, default=0, choices=[0, 1])
parser.add_argument('-n', '--jobname', help='will be Output filename initial', default = "Results")
parser.add_argument('-p', '--prob', help='probability cut-off for prediction', default=0.85, type=float)
parser.add_argument('-m', '--mode', help='enter 3 for 3D classifier, 2 for 2D classifier and 1 for combo', default=3, type=int, choices=[3, 2, 1])

def cutoff_limit(x):
    if x < 0.5:
        raise argparse.ArgumentTypeError("Minimum cutoff is 0.5")
    if x > 0.95:
        raise argparse.ArgumentTypeError("Maximum cutoff is 0.95")
    return x
    
def readSMIfile(fObj):
   mols=[]
   for line in fObj:
      smi, name = line.strip().split()
      m = Chem.MolFromSmiles(smi)
      if m:
         m.SetProp("_Name",name)
         mols.append(m)
   return mols

args = parser.parse_args()
mode = args.mode
cutoff = cutoff_limit(args.prob)
inF = args.input
smi_flag = args.smi
outF = args.jobname

#inF = home_folder+"example/amf-5f.sdf" 
#mols = [x for x in  Chem.SDMolSupplier(inF) if x is not None]

if smi_flag:
   from StringIO import StringIO
   temp = StringIO(inF)
   mols = readSMIfile(temp)

elif inF.endswith(".sdf") or inF.endswith(".sd"):
   mols = [x for x in  Chem.SDMolSupplier(inF) if x is not None]
elif inF.endswith(".mol"):
   mols = Chem.MolFromMolFile(inF)
elif inF.endswith(".mol2"):
   mols = Chem.MolFromMol2File(inF)
elif inF.endswith(".smi"):
   temp = open(inF, "r")
   mols = readSMIfile(temp)
   temp.close()

print 'no. compunds for target prediction : ', len(mols)		# 1502

with open(home_folder+"imp_files/Tpositive.txt", "r") as annotTP:
    smiTP, scpdbTP, uniprotTP = zip(*(line.strip().split() for line in annotTP))
    
'''
with open(home_folder+"imp_files/Tnegative.txt", "r") as annotTN:
    smiTN, scpdbTN, uniprotTN = zip(*(line.strip().split() for line in annotTN))

temp = np.asarray(smiTP + smiTN)
newID = np.genfromtxt(home_folder+"imp_files/newIDC.txt", dtype=int)
newID = newID.astype(np.bool)
smiT = temp[newID]

# check and remove compunds similar to training ligands
fp_T = []   
for smi in smiT:
   m = Chem.MolFromSmiles(smi)
   if m:
      fp = AllChem.GetMorganFingerprint(m, 2)
      fp_T.append(fp)

from rdkit import DataStructs
for m in mols:
   fp = AllChem.GetMorganFingerprint(m, 2)
   sim_T = DataStructs.BulkTanimotoSimilarity(fp, fp_T)
   if max(sim_T) > 0.90:
      mols.remove(m)
print 'no. compunds different from training data', len(mols)		# 1446
'''
print 'loading required descriptors file and classifiers, it may takes half a min.'

imp_feat_lig3 = np.genfromtxt(home_folder+'imp_files/imp_feat_lig3.txt', dtype=int)
imp_feat_lig2 = np.genfromtxt(home_folder+'imp_files/imp_feat_lig2.txt', dtype=int)

prodes3 = np.genfromtxt(home_folder+'imp_files/prodes3.txt')
prodes2 = np.genfromtxt(home_folder+'imp_files/prodes2.txt')
# classifiers
clfRF3 = joblib.load(home_folder+"clf_files/clfRF.pkl")
clfRF2 = joblib.load(home_folder+"clf_files/clfRF2.pkl")

uniT = []
temp = []

for i in set(uniprotTP):
   uniT.append(i)
   temp.append(uniprotTP.index(i))

idx = np.asarray(temp)
pd2 = prodes2[idx]		#(1473, 35)

from collections import defaultdict
r2 = defaultdict(lambda : defaultdict(float))
r3 = defaultdict(lambda : defaultdict(float))

from datetime import datetime
print "Your job started at ", datetime.now()
t1 = datetime.now()

mode = 'combo'
cutoff = 0.7

for m in mols:
   #lig = m.GetProp('DATABASE_ID')
   lig = m.GetProp('_Name')
   print 'Compound_ID ', lig
   fp = AllChem.GetMorganFingerprintAsBitVect(m, 2, nBits=1024)
   fp_array = np.zeros((1,))
   DataStructs.ConvertToNumpyArray(fp, fp_array)
   
   if mode in ('3d', 'combo'):
	fp_array3 = fp_array[imp_feat_lig3]
	temp = np.tile(fp_array3, (prodes3.shape[0],1))
	x3 = np.concatenate((prodes3, temp), axis=1)
	p3 = clfRF3.predict_proba(x3)[:,1]

	for i, pdb in enumerate(scpdbTP):
	   if p3[i] > cutoff:
	      r3[lig][pdb] = p3[i]   
   
   if mode in ('2d', 'combo'):
	fp_array2 = fp_array[imp_feat_lig2]
	temp = np.tile(fp_array2, (pd2.shape[0],1))
	x2 = np.concatenate((pd2, temp), axis=1)
	p2 = clfRF2.predict_proba(x2)[:,1]

	for i, uni in enumerate(uniT):
	   if p2[i] > cutoff:
	      r2[lig][uni] = p2[i]

print "target predicted in : ", (datetime.now()-t1)

import csv

if mode=='3d':
   f1 = open(outF+"_PrediTar_3d.csv","wb")
   writer = csv.writer(f1, delimiter=";", quotechar=' ')
   title_line = ["lig_name", "PDB_id", "het_id", "probability", "link"]
   writer.writerow(title_line)
   for lig, pred in r3.iteritems():
      writer.writerow([lig])
      for pdb, prob3 in pred.iteritems():
         pro, het = pdb.split('-')
         link = 'http://www.rcsb.org/pdb/explore.do?structureId=%s' %(pdb)
         writer.writerow(['', pro, het, prob3, link])
   f1.close()
   print "predicted targets are saved in `%_PrediTars_3d.csv` file" %(outF)

if mode=='2d':
   f2 = open(outF+"_PrediTar_2d.csv","wb")
   writer = csv.writer(f2, delimiter=";", quotechar=' ')
   title_line = ["lig_name", "uniprot_acc", "probability"]
   writer.writerow(title_line)
   for lig, pred in r2.iteritems():
      writer.writerow([lig])
      for uni, prob2 in pred.iteritems():
         writer.writerow(['', uni, prob2])
   f2.close()
   print "predicted targets are saved in `%s_PrediTar_2d.csv` file" %(outF)
   
if mode=='combo':
   f2 = open(outF+"_PrediTar_combo.csv","wb")
   writer = csv.writer(f2, delimiter=";", quotechar=' ')
   title_line = ["lig_name", "PDB_id",  "het_id", "prob3", "uniprot_acc", "prob2"]
   writer.writerow(title_line)
   for lig, pred in r3.iteritems():
      writer.writerow([lig])
      for pdb, prob3 in pred.iteritems():
         pro, het = pdb.split('-')
         pos = scpdbTP.index(pdb)
         uni = uniprotTP[pos]
         prob2 = r2[lig][uni]
         writer.writerow(['', pro, het, prob3, uni, prob2])
   f2.close()
   print "predicted targets are saved in `%s_PrediTar_combo.csv` file" %(outF)   

annotTP.close()
#annotTN.close()
