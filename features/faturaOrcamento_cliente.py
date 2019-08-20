import faturaOrcamento as proxy

def getStatus(id):
    result = proxy.get_budget_status(id)
    return result

def baixaSaldo(id):
    if(proxy.cash_budget(id)):
        return "success"
    else:
        return "fail"

def getOrcamento(id, status):
    if(len(proxy.get_budget(id, status)) > 0):
        return "success"
    else:
        return "fail"
