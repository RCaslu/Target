import time

def descobrir_interruptores():
    lampadas = {'A': 'apagada', 'B': 'apagada', 'C': 'apagada'}
    
    lampadas['A'] = 'acesa'
    
    lampadas['A'] = 'apagada'
    lampadas['B'] = 'acesa'
    
    resultado = {}
    for lampada, estado in lampadas.items():
        if estado == 'acesa':
            resultado['B'] = lampada
        elif estado == 'apagada' and lampada == 'A':
            resultado['A'] = lampada
        else:
            resultado['C'] = lampada
    
    return resultado

resultado = descobrir_interruptores()
print("Interruptor A controla a lâmpada:", resultado['A'])
print("Interruptor B controla a lâmpada:", resultado['B'])
print("Interruptor C controla a lâmpada:", resultado['C'])