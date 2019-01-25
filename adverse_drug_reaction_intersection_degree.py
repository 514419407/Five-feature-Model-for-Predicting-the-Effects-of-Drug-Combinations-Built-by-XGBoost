def get_info(drug, info_dict):
    drug_feature =[]
    if drug in info_dict:
        drug_feature = info_dict[drug]
    return  drug_feature

def adverse_drug_reaction_intersection_degree(drug_adr, druga, drugb):
    druga_adr = get_info(druga, drug_adr)
    drugb_adr = get_info(drugb, drug_adr)
    if druga_adr and drugb_adr:
        adr_similar = len(set(druga_adr) & set(drugb_adr))/len(set(druga_adr) | set(drugb_adr))
    else:
        adr_similar = 'null'
    return adr_similar
