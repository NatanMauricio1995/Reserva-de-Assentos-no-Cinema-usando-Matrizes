# 🎬 Sistema de Reserva de Cinema

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Status](https://img.shields.io/badge/Status-Concluído-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

Sistema desenvolvido em Python para gerenciar reservas de assentos em um cinema com **5 fileiras** e **10 assentos** por fileira (50 assentos totais).

## 📋 Descrição do Projeto

Este sistema foi desenvolvido como parte dos estudos em **estruturas de dados** e **programação procedural** em Python. O projeto simula um sistema real de cinema onde usuários podem visualizar a disponibilidade de assentos e fazer reservas.

### 🎯 Problema Resolvido
- **Cenário:** Cinema pequeno precisa de sistema simples para controle de reservas
- **Solução:** Interface de linha de comando intuitiva para visualização e reserva
- **Resultado:** Sistema funcional com validações e tratamento de erros

## ⚡ Funcionalidades

- ✅ **Visualização de Poltronas:** Exibe mapa completo do cinema em tempo real
- ✅ **Reserva de Assentos:** Sistema de reserva com validação de entrada
- ✅ **Interface Visual:** Uso de emojis para melhor experiência do usuário
- ✅ **Tratamento de Erros:** Validação robusta para entradas inválidas
- ✅ **Prevenção de Conflitos:** Impede reserva de assentos já ocupados
- ✅ **Menu Interativo:** Navegação simples e intuitiva

## 🛠️ Tecnologias

- **Python 3.x**
- **Estruturas de Dados:** Matrizes (listas bidimensionais)
- **Programação Procedural**
- **Tratamento de Exceções**

## 🚀 Como Executar

### Pré-requisitos
- Python 3.6 ou superior instalado

### Passos
1. **Clone o repositório:**
   ```bash
   git clone https://github.com/NatanMauricio1995/sistema-cinema-python.git
   cd sistema-cinema-python
   ```

2. **Execute o programa:**
   ```bash
   python cinema_melhorado.py
   ```

3. **Interaja com o menu:**
   - Digite `1` para ver as poltronas
   - Digite `2` para reservar um assento
   - Digite `3` para sair

## 📸 Preview do Sistema

```
------------------------------------------------------------
                     🎬 CINEMA SYSTEM 🎬
------------------------------------------------------------
1 - Exibir poltronas
2 - Reservar poltrona
3 - Sair
------------------------------------------------------------

==================================================
                  🎭 TELA DO CINEMA 🎭
==================================================
     1  2  3  4  5  6  7  8  9 10
1:  🟢 🟢 🔴 🟢 🟢 🟢 🔴 🟢 🟢 🟢
2:  🟢 🔴 🟢 🟢 🟢 🟢 🟢 🟢 🔴 🟢
3:  🟢 🟢 🟢 🟢 🟢 🟢 🟢 🟢 🟢 🟢
4:  🔴 🟢 🟢 🟢 🟢 🟢 🟢 🟢 🟢 🟢
5:  🟢 🟢 🟢 🟢 🟢 🟢 🟢 🟢 🟢 🟢

🟢 Disponível  🔴 Reservado  ⚫ Ocupado
==================================================
```

## 💻 Estrutura do Código

### Arquivos Principais
- **`cinema.py`** - Versão inicial funcional
- **`cinema_melhorado.py`** - Versão otimizada com melhorias de UX

### Principais Funções
```python
def inicializar_cinema()    # Cria matriz 5x10 com assentos disponíveis
def exibir_menu()          # Interface principal do sistema  
def obter_opcao()          # Validação de entrada do usuário
def exibir_poltronas()     # Visualização do mapa de assentos
def reservar_poltrona()    # Lógica de reserva com validações
def main()                 # Fluxo principal do programa
```

## 🧠 Conceitos Aplicados

### Estruturas de Dados
- **Matrizes (Listas 2D):** Representação do cinema como matriz 5x10
- **Manipulação de Índices:** Conversão entre interface usuário (1-10) e código (0-9)

### Programação Procedural
- **Modularização:** Divisão em funções específicas
- **Separação de Responsabilidades:** Cada função tem um propósito claro

### Tratamento de Erros
- **Try/Except:** Captura de entradas inválidas
- **Validação de Range:** Verificação de limites (fileiras 1-5, assentos 1-10)

### Experiência do Usuário
- **Interface Visual:** Emojis para representar estados dos assentos
- **Feedback Claro:** Mensagens informativas sobre operações

## 📈 Evolução do Projeto

| Versão | Melhorias Implementadas |
|--------|------------------------|
| **v1.0** | Funcionalidade básica, interface textual simples |
| **v2.0** | Interface visual com emojis, melhor UX, código mais limpo |

### Próximas Melhorias Planejadas
- [ ] Persistência de dados (salvar em arquivo)
- [ ] Diferentes tipos de assento (VIP, comum)
- [ ] Sistema de preços e cálculo de total
- [ ] Histórico de reservas
- [ ] Interface gráfica com Tkinter

## 🎓 Aprendizados

Este projeto consolidou conhecimentos em:
- **Estruturas de dados bidimensionais**
- **Validação robusta de entrada**
- **Design de interface de usuário em terminal**
- **Organização e modularização de código**
- **Boas práticas de programação Python**

## 📊 Especificações Técnicas

- **Capacidade:** 50 assentos (5 fileiras × 10 assentos)
- **Estados dos Assentos:** Disponível (D), Reservado (R), Ocupado (O)
- **Validações:** Entrada numérica, range de valores, disponibilidade
- **Compatibilidade:** Multiplataforma (Windows, Linux, macOS)

## 🤝 Contribuições

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📧 Contato

**Natan Maurício Santos**
- 📧 Email: natanmauriciosantos@hotmail.com
- 💼 LinkedIn: [linkedin.com/in/natan-mauricio-santos](https://linkedin.com/in/natan-mauricio-santos)
- 🐙 GitHub: [github.com/NatanMauricio1995](https://github.com/NatanMauricio1995)

---

⭐ **Se este projeto te ajudou, deixe uma estrela!**

*Desenvolvido com 💙 durante os estudos de Tecnologia da Informação*
