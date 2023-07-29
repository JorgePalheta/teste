import sys

cep = sys.argv[1]
cep = cep.replace("-","").replace(".","").replace(" ","").replace("  ","").replace("_","").replace("oi")

print(cep)
