# MapRecude

### Equipe

  - [Marcos Leandro]
  - [Everton Fernandes]

Atividade:
Encontrar as 1500 palavras mais usadas em 1 determinado livro.
### Requisitos
  - Instalar o python3
  - Instalar o  bs4
  - Configurar no arquivos "extract_text.py" o caminho do diretório do livro, o diretório de saída e o nome do arquivo de saída

O script pode ser executada de duas formas:
###### Forma 1:
  - Executar os seguintes comandos no terminal no diretório dos arquivos
```sh
python3.4 extract_text.py
cat livros.txt | python  map.py | sort | python reduce.py > output.txt
```

  - Visualizar o arquivo de saída "output.txt" no diretório dos arquivos

| Linha | Descrição |
| ------ | ------ |
| Linha 1 | extrai e salva somente o conteúdo do livro em um novo arquivo |
| Linha 2 | pega o arquivo gerado faz o "map", o "reduce" e salva no arquivo de saída |

###### Forma 2:
  - Executar os seguintes comandos no terminal no diretório dos arquivos
```sh
python3.4 extract_text.py
hdfs dfs -put /home/cloudera/Documents/python/livros.txt /user/cloudera/arquivos/
hadoop  jar /usr/lib/hadoop-mapreduce/hadoop-streaming-*.jar     
        -D mapred.job.name="Hadoop_Streaming_UP"
        -mapper "python /home/cloudera/Documents/python/map.py"
        -reducer "python /home/cloudera/Documents/python/reduce.py"
        -input "arquivos/livrosForHdfs.txt"
        -output "arquivos/saidaHdfs"
```
  - Visualizar dentro do hdfs o arquivo de saída

| Linha | Descrição |
| ------ | ------ |
| Linha 1 | extrai e salva somente o conteúdo do livro em um novo arquivo |
| Linha 2 | coloca o arquivo gerado dentro do hdfs |
| Linha 3 | Comando para executar o map reduce |
| Linha 3: Parâmetro 1 | biblioteca hadoop-streaming-*.jar |
| Linha 3: Parâmetro 2 | define um nome para o job |
| Linha 3: Parâmetro 3 | seleciona o arquivo de map |
| Linha 3: Parâmetro 4 | seleciona o arquivo de reduce |
| Linha 3: Parâmetro 5 | arquivo de entrada dentro do hdfs |
| Linha 3: Parâmetro 6 | diretório de saída dentro do hdfs |

Obs.: A diferença entre as duas formas é que a primeira executa o map reducer sem utilizar o hdfs, já a segunda utiliza o streaming do hdfs.

   [Marcos Leandro]: <https://github.com/Marcos-Leandro>
   [Everton Fernandes]: <https://github.com/evertonlf>
