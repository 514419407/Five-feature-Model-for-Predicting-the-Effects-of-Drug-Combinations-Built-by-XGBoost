def inner_separation(drugx_targets, drugy_targets, targets_matrix, boolean):
    target_score = []
    x = float('inf')
    for target_i in drugx_targets:
        target_i_score = []
        for target_j in drugy_targets:
            if (boolean == True and target_i != target_j) or (boolean == False):
                try:
                    target_distance = targets_matrix.ix[target_i,target_j]
                    if target_distance != x:
                        target_i_score.append(target_distance)
                except Exception,e:
                    pass
        try:
            i_min_target = min(target_i_score)
            target_score.append(i_min_target)
        except ValueError, e:
            pass
    if target_score:
        return target_score
    else:
        return None

def network_separation(druga_targets, drugb_targets, targets_matrix):
    targeta_score = inner_separation(druga_targets, druga_targets, targets_matrix, True)
    #print targeta_score
    targetb_score = inner_separation(drugb_targets, drugb_targets, targets_matrix, True)
    #print targetb_score
    targeta2b_score = inner_separation(druga_targets, drugb_targets, targets_matrix, False)
    #print targeta2b_score
    targetb2a_score = inner_separation(drugb_targets, druga_targets, targets_matrix, False)
    #print targetb2a_score
    if targeta2b_score and targetb2a_score:
        targetab_inter_score = targeta2b_score + targetb2a_score
    else:
        targetab_inter_score = None
    if targeta_score and targetb_score and targetab_inter_score:
        targeta_mean_score = sum(targeta_score) / len(targeta_score)
        targetb_mean_score = sum(targetb_score) / len(targetb_score)
        targetab_inter_mean_score = sum(targetab_inter_score) / len(targetab_inter_score)
        separation_score = targetab_inter_mean_score - 1/2 * (targeta_mean_score + targetb_mean_score)
    else:
        separation_score = 'null'
    return separation_score
