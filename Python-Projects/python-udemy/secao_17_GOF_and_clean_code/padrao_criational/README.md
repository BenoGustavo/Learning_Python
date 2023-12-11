## PADRÕES CRIACIONAIS

Tem como objetivo criar objetos seguindo como base padrões de projetos bem vistos dentro da area de desenvolvimento.

### Tipos de Padrões Criacionais

#### Singleton

O Singleton tem a intenção de garantir que uma classe tenha somente
uma instância e fornece um ponto global de acesso para a mesma (Na minha opniao não serve pra muita coisa).

#### Monostate

Monostate (ou Borg) - É uma variação do Singleton proposto
por Alex Martelli que tem a intenção de garantir que o
estado do objeto seja igual para todas as instâncias.

#### Builder

Builder é um padrão de criação que tem a intenção
de separar a construção de um objeto complexo
da sua representação, de modo que o mesmo processo
de construção possa criar diferentes representações.

Builder te da a possibilidade de criar objetos passo-a-passo
e isso já é possível no Python sem este padrão
(Aquele bgl de deixar como um parametro como **None** depois criar um setter pra definir uma coisa depois).

Geralmente o builder aceita o encadeamento de métodos
(method chaining).

#### Factories

-   O que é uma factory?

    Factory method é um padrão de criação que permite definir uma interface para
    criar objetos, mas deixa as subclasses decidirem quais objetos criar. O
    Factory method permite adiar a instanciação para as subclasses, garantindo o
    baixo acoplamento entre classes.

-   AbstractFactory

    Abstract Factory é um padrão de criação que fornece uma interface para criar
    famílias de objetos relacionados ou dependentes sem especificar suas classes
    concretas. Geralmente Abstract Factory conta com um ou mais Factory Methods
    para criar seus objetos.

    Uma diferença importante entre Factory Method e Abstract Factory é que o
    Factory Method usa herança, enquanto Abstract Factory usa a composição.

    Princípio: programe para interfaces, não para implementações

-   SimpleFactory

    Na programação POO, o termo factory (fábrica) refere-se a uma classe ou método
    que é responsável por criar objetos.

    Vantagens:
    Permitem criar um sistema com baixo acoplamento entre classes porque
    ocultam as classes que criam os objetos do código cliente.

          Facilitam a adição de novas classes ao código, porque o cliente não
          conhece e nem utiliza a implementação da classe (utiliza a factory).

          Podem facilitar o processo de "cache" ou criação de "singletons" porque a
          fábrica pode retornar um objeto já criado para o cliente, ao invés de criar
          novos objetos sempre que o cliente precisar.

    Desvantagens:
    Podem introduzir muitas classes no código

    Simple Factory pode não ser considerado um padrão de projeto por si só
    Simple Factory pode quebrar princípios do SOLID

#### Prototype

Especificar os tipos de objetos a serem criados
usando uma instância-protótipo e criar novos objetos
pela cópia desse protótipo.

#### Dados mutaveis e imutaveis em python

Mutáveis: [list,set,dict,class (o usuário pode mudar isso)]

Imutáveis: [ bool,int,float,tuple,str]
