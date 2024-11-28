### Problema das rainhas

Solução utilizando Python.

Pseudocódigo
```
Função posiciona_rainhas (l, c, tab, faltantes, rainhas_posicionadas) 

    Se não há mais faltantes, retorna tab 
    
    Se tab nas diagonais, linhas e colunas do posição atual está livre: 
    
        tab[l][c] = “r” 
        
        rainhas_posicionadas = (l,c) 
        
        faltantes -= 1 
    
            Se estamos na última coluna: 
    
                    posiciona_rainhas(l=l+1, c=0, ...) 
    
            Se não: 
    
                    posiciona_rainhas(l, c=+1, ...) 
    
    Se não: 
    
            Se já passamos por todo o tabuleiro: 
    
                    Pegue a posição da última rainha posicionada 
    
                    Retire o “r” do tab desta posição 
    
                    Adicione +1 nas faltantes 
    
                    Se a última posicao da rainha já estava na última coluna: 
    
                            posiciona_rainhas(l=l+1, c=0, ...) 
    
                    Se não: 
    
                            posiciona_rainhas(l, c=c+1, ...) 
    
            Se a última posição da rainha já estava na última coluna: 
    
                posiciona_rainhas(l=l+1, c=0, ...) 
    
            Se não estava na última coluna: 
    
                posiciona_rainhas(l, c=c+1, ...) 
``
