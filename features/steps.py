from lettuce import *
import faturaOrcamento_cliente

@step('I see the text "([^"]*)"')
def check_operation(step, expected):
    assert (expected == world.result)

@step('I have the budget id (\d+)')
def i_have_id_for_budget(step, id):
    world.id_orc = int(id)

@step('I have the new status (\d+)')
def have_status(step, new_status):
	world.new_status = int(new_status)

@step('I get the budget')
def get_budget(step):
    world.result = str(faturaOrcamento_cliente.getOrcamento(world.id_orc, world.new_status))

@step('I see the new status (\d+)')
def get_new_status(step, expected):
	assert (int(expected) == int(faturaOrcamento_cliente.getStatus(world.id_orc)))

@step('I cash the budget')
def cash_budget(step):
	world.result = str(faturaOrcamento_cliente.baixaSaldo(world.id_orc))

#Failure States
@step('I do not see the text "([^"]*)"')
def check_operation(step, expected):
    assert not (expected == world.result)

@step('I do not see the new status (\d+)')
def get_new_status_fail(step, expected):
	assert not (int(expected) == int(faturaOrcamento_cliente.getStatus(world.id_orc)))
