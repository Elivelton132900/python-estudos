from importlib import metadata


print(metadata.version('pip'))
print(list(metadados_pip := metadata.metadata('pip')))
print(metadados_pip['Home-page'])
print('')
print(len(metadata.files('pip')))
