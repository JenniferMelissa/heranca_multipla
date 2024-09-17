#heranca/generalizacao)
#herança multipla
#classes herdam metrodos e atributos de outra classe, ou mais de uma classe

from modulo import *

if __name__ == '__main__':
    #instancia objeto da classe
    h = Filho('','','','',0.0,0.0,'')

    #entrada de dados
    h.nome = input('Informe o nome: ')
    h.email = input('Informe o email: ')
    h.profissao = input('Informe a profissao: ')
    h.olhos = input('Informe a cor dos olhos: ')
    h.peso = float(input('Informe o peso: ').replace(',','.'))
    h.altura =  float(input('Informe a altura: ').replace(',','.'))
    h.cor_cabelo = input('Informe a cor do cabelo: ')

    #saida de dados
    h.exibir_cartao_visitas()
    h.exibir_fisico()