from pop import Population

if __name__ == '__main__':
    p = Population(1000,'sanket cool')
    while(not p.done):
        p.evaluate()
        p.select()
