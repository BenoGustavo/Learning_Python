VENV

Criando o ambiente virtual

python -m venv {nomedoambiente}

-=-=-=-=-=-=-=-=-

Mostra qual executavel do python está sendo utilizado

gcm python -Syntax

-=-=-=-=-=-=-==-

Ativando um ambiente virtual

local da pasta\ pasta \ activate


-=-=-=-=-=-=-=-=-=

Desativando um ambiente virtual

deactivate

-=-=-=-=-=-=-=-=-=-

Instala pacotes de fora do python

pip install {nome do pacote}

Instala uma versão especifica

pip install {nome do pacote}=={versao}

-=-=-=-=-=-=-=-=--=-=-

Desinstala pacotes

pip uninstall {nome do pacote}

-=-=-=-=-=-=-=-=-=-=-=-=

Ver pacotes instalados

pip freeze

Manda todos os pacotes instalados para um txt, assim conseguindo deixar 
mais facil upar em repositorios sem carregar muitas coisas

requiremente.txt é tudo que é necessario para carregar o arquivo

pip freeze > requirementes.txt

Instala tudo que existe dentro de requirementes.txt

pip install -r .\requirementes.txt
