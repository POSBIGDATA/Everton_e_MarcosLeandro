# MapRecude

<strong>Equipe</strong><br />
<a href="https://github.com/Marcos-Leandro" target="blank">Marcos Leandro</a><br />
<a href="https://github.com/evertonlf" target="blank">Everton Fernandes</a>
<br />
<br />
<strong>Atividade</strong>
<br />
Encontrar as 1500 palavras mais usadas em 1 determinado livro.
<br />
<br  />
<strong>Executar passos na raiz deste projeto</strong><br />
Instalar o python3<br />
Instalar o  bs4<br />
Configurar no arquivos "extract_text.py" o caminho do diretório do livro, o diretório de saída e o nome do arquivo de saída<br />
<br />
O script pode ser executada de duas formas:<br />
Forma 1:<br />
Executar os seguintes comandos no terminal no diretório dos arquivos<br />
1 - python3.4 extract_text.py<br />
-----(extrai e salva somente o conteúdo do arquivo)<br />
2 - cat livros.txt | python  map.py | sort | python reduce.py > output.txt<br />
-----(pega o arquivo gerado faz o "map", o "reduce" e salva no arquivo de saída)<br />
3 - Visualizar o arquivo de saída "output.txt" no diretório dos arquivos.
<br />
<br />
Foma 2:<br />
Executar os seguintes comandos no terminal no diretório dos arquivos<br />
1 - python3.4 extract_text.py<br />
-----(extrai e salva somente o conteúdo do arquivo)<br />
2 - hdfs dfs -put /home/cloudera/Documents/python/livros.txt /user/cloudera/arquivos/<br />
-----(coloca o arquivo gerado dentro do hdfs)<br />
3 - hadoop     jar /usr/lib/hadoop-mapreduce/hadoop-streaming-*.jar     -D mapred.job.name="Hadoop_Streaming_UP"     -mapper "python /home/cloudera/Documents/python/map.py"     -reducer "python /home/cloudera/Documents/python/reduce.py"     -input "arquivos/livrosForHdfs.txt"     -output "arquivos/saidaHdfs"<br />
-----parametros:<br />
-----seleciona a biblioteca hadoop-streaming-*.jar<br />
-----define um nome para o job<br />
-----seleciona o arquivo de map<br />
-----seleciona o arquivo de reduce<br />
-----arquivo de entrada dentro do hdfs<br />
-----diretório de saída dentro do hdfs<br />
4 - Visualizar dentro do hdfs o arquivo de saída.
<br />
<br />
A diferença entre as duas formas é que a primeira executa o map reduce sem utilizar o hdfs, já a segunda utiliza o streaming do hdfs.
