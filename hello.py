from azureml.core import Workspace

ws = Workspace.create(name='mm-aml-dev"', # provide a name for your workspace
                      subscription_id='5da07161-3770-4a4b-aa43-418cbbb627cf', # provide your subscription ID
                      resource_group='mm-machine-learning-dev-rg', # provide a resource group name
                      create_resource_group=True,
                      location='eastus2') # For example: 'westeurope' or 'eastus2' or 'westus2' or 'southeastasia'.

# write out the workspace details to a configuration file: .azureml/config.json
#ws.write_config(path='.azureml')



print('hello')