import sys
import time
import random
import os

class Ports(object):
	ssl=[636,443,1311,2381,9043,993,995,4343,9443,3170]
	mail=[25,110,143,993,995]
	db2=[523,50000,6789]
	vpn=[1723]
	high_risk=[22,23,10000]
	common=high_risk+[25,80,443,22,21,23,445,111,79,53,515,1433,13722,389,8009,6101,6106,8080]
	oracle=[1521,1522,2100]
	no_probe=[9373,9100]
	db=[1433,3306,5432,3060]+oracle+db2 # mssql, mysql, postgress, firebird(interbase)
	other=[2049,41523,6000,113,119] # nfs, arcserver,xwin,auth,nntp