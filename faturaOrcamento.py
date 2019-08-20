# encoding: utf-8
import xmlrpclib

server_budget = xmlrpclib.ServerProxy("http://localhost:8000/")
server_stock = xmlrpclib.ServerProxy("http://localhost:8888/")

def get_budget(budget_id, new_status):
	budget = server_budget.retornaOrcamento(budget_id)
	if len(budget) > 0:
		if(server_budget.atualizarStatus(budget_id, new_status)):
			return budget[2]

	return []

def get_budget_status(budget_id):
	budget = server_budget.retornaOrcamento(budget_id)
	if len(budget) > 0:
		return budget[1]


def cash_budget(budget_id):
	stock_list = get_budget(budget_id, 1)

	if len(stock_list) > 0:
		for i in stock_list:
			if server_stock.faturaProduto(i[0], i[1]) == 1:
				return True
	return False
