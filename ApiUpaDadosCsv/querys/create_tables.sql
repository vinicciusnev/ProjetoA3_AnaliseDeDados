CREATE TABLE Faturamento_Por_Item (
ID_ITEM INT AUTO_INCREMENT PRIMARY KEY,
DT_EMISSAO date,
VL_ACRESCIMO_NOTA DECIMAL(20,2),
VL_DESCONTO_NOTA DECIMAL(20,2),
DS_PRO_FAT varchar(300),
DS_UNIDADE varchar(300),
NM_SETOR varchar(300),
VL_ITFAT_NF DECIMAL(20,2),
VL_RECEBIDO DECIMAL(20,2),
VL_GLOSA DECIMAL(20,2),
DS_GRU_PRO varchar(300)
);