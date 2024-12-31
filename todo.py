import os

tarefas = ['lutar judô', 'treinar musculação', 'estudar programação']

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def addTarefa():
    clear()
    tarefa = input('digite sua terafa: ')
    tarefas.append(tarefa)
    print(f'tarefa: {tarefa} adicionada!')

def listTarefas():
    clear()
    if not tarefas:
        print('nao existe tarefas :(')
    else:
        print('TAREFAS: ')
        for index, tarefa in enumerate(tarefas):
            print(f'tarefa {index}. {tarefa}')
clear()

def deletTarefa():
    listTarefas()
    try:
        tarefaParaDeletar = int(input('escolha o numero da tarefa para deletar: '))
        if tarefaParaDeletar < len(tarefas):
            tarefas.pop(tarefaParaDeletar)
            print(f'a tarefa {tarefaParaDeletar} foi deletada')
        else:
            print(f'tarefa {tarefaParaDeletar} nao foi encontrada')
    except:
        print('invalido')


if __name__ == '__main__':
    # criar o loop
    print('\nBem-vindo ao app lista de tarefas :)')
    while True:
        print('\n')
        print('Selecione uma opção')
        print('*************************')
        print('1 - adicionar uma nova tarefa.')
        print('2 - visualizar lista.')
        print('3 - deletar tarefa.')
        print('4 - sair.')
        print('*************************')
        choice = input('Escolha uma opção: ')
        
        if choice == '1':
            clear()
            addTarefa()
        elif choice == '2':
            clear()
            listTarefas()
        elif choice == '3':
            deletTarefa()
            clear()
        else:
            break