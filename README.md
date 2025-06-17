
# Padrões de Projeto GoF em Python

Este repositório contém implementações didáticas dos padrões de projeto da "Gang of Four" (GoF), focando nos padrões da categoria Criacional: Singleton, Factory Method e Abstract Factory.

---

## Conteúdo

- **Singleton**: Garante que uma classe tenha apenas uma instância e fornece um ponto global de acesso a ela.
- **Factory Method**: Define uma interface para criação de um objeto, mas deixa as subclasses decidirem qual classe instanciar.
- **Abstract Factory**: Fornece uma interface para criar famílias de objetos relacionados sem especificar suas classes concretas.

---

## Como usar

1. Clone o repositório:

```bash
git clone https://github.com/wesley-zorzolli/padroes-de-projeto-gof-python.git
cd padroes-de-projeto-gof-python
```

2. Navegue até a pasta do padrão desejado e execute o arquivo Python correspondente:

### Singleton

```bash
cd singleton
python sem_singleton.py
python com_singleton.py
```

### Factory Method

```bash
cd ../factory_method
python sem_factory.py
python com_factory.py
```

### Abstract Factory

```bash
cd ../abstract_factory
python sem_abstract_factory.py
python com_abstract_factory.py
```

---

## Detalhes dos padrões

### Singleton

- Garante que uma classe tenha somente uma instância.
- Útil para gerenciar recursos compartilhados, como conexões de banco de dados ou geradores de logs.

| Aspecto           | Sem Singleton                | Com Singleton                   |
|-------------------|-----------------------------|--------------------------------|
| Instâncias únicas  | ❌ Não garantido             | ✅ Garantido                   |
| Facilidade de acesso | ❌ Difícil acessar globalmente | ✅ Fácil acesso global         |
| Risco de bugs      | ❌ Múltiplas instâncias podem causar inconsistências | ✅ Controle total           |

---

### Factory Method

- Define uma interface para criação de objetos, delegando a criação às subclasses.

| Aspecto           | Sem Factory Method          | Com Factory Method              |
|-------------------|----------------------------|--------------------------------|
| Flexibilidade     | ❌ Rígido                   | ✅ Flexível e escalável         |
| Acoplamento       | ❌ Alto                    | ✅ Baixo                       |
| Testabilidade     | ⚠️ Média                   | ✅ Alta                        |
| Extensão          | ⚠️ Requer if/else          | ✅ Nova classe sem alterar código |

---

### Abstract Factory

- Cria famílias de objetos relacionados sem especificar suas classes concretas.

| Aspecto           | Sem Abstract Factory        | Com Abstract Factory            |
|-------------------|----------------------------|--------------------------------|
| Coesão            | ❌ Mistura criação e uso    | ✅ Criação isolada             |
| Escalabilidade    | ❌ Difícil adicionar famílias | ✅ Fácil adicionar famílias    |
| Testabilidade     | ⚠️ Média                   | ✅ Alta                        |
| Manutenção        | ❌ Mais frágil              | ✅ Mais robusta                |

---

## Conclusão

O uso de padrões de projeto ajuda a tornar o código mais organizado, flexível e fácil de manter. Em projetos reais, aplicar esses conceitos pode evitar problemas comuns como acoplamento excessivo e dificuldade de manutenção.

---

## Autor

Wesley Santos - [GitHub](https://github.com/seu_usuario)

---

## Referências

- "Design Patterns: Elements of Reusable Object-Oriented Software" - Erich Gamma et al.
- Documentação oficial Python
