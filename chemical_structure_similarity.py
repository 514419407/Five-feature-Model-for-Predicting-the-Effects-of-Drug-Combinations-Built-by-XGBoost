def smiles_similarity(drug_smiles, druga, drugb, Chem, DataStructs):
    druga_smiles = get_info(druga, drug_smiles)
    drugb_smiles = get_info(drugb, drug_smiles)
    if druga_smiles and drugb_smiles:
        mol1 = Chem.MolFromSmiles(druga_smiles)
        mol2 = Chem.MolFromSmiles(drugb_smiles)
        if mol1 and mol2:
        # the default fingerprint is path-based:
            fp1 = Chem.RDKFingerprint(mol1)
            fp2 = Chem.RDKFingerprint(mol2)
            smiles_similar = DataStructs.TanimotoSimilarity(fp1, fp2)
        else:
            smiles_similar = 'null'
    else:
        smiles_similar = 'null'
    return smiles_similar
