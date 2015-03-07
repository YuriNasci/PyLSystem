""" -*- iso-8859-1 -*-
LSystem.py
Módulo para LSystems """
import re
import random

class LSystem:
    __axiom = __productions = ''
    """ @func init: Construtor da classe LSystem
    @param axiom: Palavra inicial do L-System
    @param productions: Regras de produção """ 
    def __init__(self, axiom, productions):
        self.__axiom = axiom
        self.__productions = self.__validateProductions(productions)
    
    def getAxiom(self):
        return self.__axiom
    
    def getProductions(self):
        return self.__productions
    
    """ @func __produce: Realiza uma etapa de derivação
    @param w: axioma """
    def __produce(self, w):
        output = ""
        for i in w:
            output += self.__productions.get(i, i)
        return output
    
    """ @func iterate: Realiza sucessivas etapas derivações e retorna a string resultado
    @param iteractions: Numero de etapas
    @param axiom: axioma """
    def iterate(self, iteractions, axiom = ''):
        if not axiom:
            axiom = self.__axiom
        
        if iteractions > 0:
            axiom = self.__produce(axiom)
            return self.iterate(iteractions - 1, axiom)

        return axiom
    
    @staticmethod
    def __validateProductions(productions):
        LETTER = '[^\d→:,()<>]'
        
        productions = re.sub('->', '→', productions)
        productions = re.sub('\s*', '', productions)
        
        PRODUCTION_RULE = '^' + LETTER + '→' + LETTER + '+' + '(,'+ LETTER + '→' + LETTER + '+' +')*' + '$' 
        
        if (re.compile(PRODUCTION_RULE).search(productions)):
            dic = {}
            look = ''
            for i in range(len(productions)):
                if (re.compile(LETTER).search(productions[i])):
                    look += productions[i]
                elif (productions[i] == '→'):
                    state = look
                    if (not dic.get(state)): dic[state] = ''
                    look = ''
                elif (productions[i] == ','):
                    dic[state] = look
                    look = ''

            dic[state] = look
            return dic
        else:
            print('Erro: Definição de produções inválida!')
            exit()
# Fim da classe LSystems
