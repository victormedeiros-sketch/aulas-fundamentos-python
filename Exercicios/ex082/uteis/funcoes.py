def titulo(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

def ajuda(comando):
    titulo(f"Acedendo ao manual do comando: '{comando}'")
    help(comando)