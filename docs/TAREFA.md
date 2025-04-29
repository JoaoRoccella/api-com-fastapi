

## **"Lista Must Watch"**

Você foi contratado para desenvolver uma API RESTful com Python (FastAPI) e MySQL que permita a gestão de uma lista pessoal de séries que o usuário deseja assistir (tipo “must watch”). Essa API deve permitir o cadastro, consulta, atualização e exclusão de séries, assim como a associação de atores, categorias, motivos para assistir e avaliações pessoais.

O sistema deve contemplar os seguintes recursos:

- Cadastro e listagem de séries;
- Cadastro de atores e associação com séries;
- Classificação por categorias (ex: comédia, drama, ação);
- Inclusão de motivos pessoais para assistir uma série;
- Avaliação pessoal após assistir (nota e comentário).

---

## **Modelo de Dados**

### **Tabela: `serie`**
| Campo         | Tipo           | Descrição                     |
|---------------|----------------|-------------------------------|
| id            | INT (PK)       | Identificador único           |
| titulo        | VARCHAR(100)   | Título da série               |
| descricao     | TEXT           | Sinopse breve                 |
| ano_lancamento| INT            | Ano de estreia                |
| id_categoria  | INT (FK)       | Categoria principal           |

---

### **Tabela: `categoria`**
| Campo      | Tipo         | Descrição                |
|------------|--------------|--------------------------|
| id         | INT (PK)     | Identificador            |
| nome       | VARCHAR(50)  | Nome da categoria        |

---

### **Tabela: `ator`**
| Campo    | Tipo         | Descrição                |
|----------|--------------|--------------------------|
| id       | INT (PK)     | Identificador            |
| nome     | VARCHAR(100) | Nome do ator             |

---

### **Tabela: `ator_serie`** (relacionamento N:N)
| Campo      | Tipo         | Descrição                            |
|------------|--------------|--------------------------------------|
| id_ator    | INT (FK)     | Relacionado à tabela `ator`          |
| id_serie   | INT (FK)     | Relacionado à tabela `serie`         |
| personagem | VARCHAR(100) | Nome do personagem na série          |

---

### **Tabela: `motivo_assistir`**
| Campo      | Tipo        | Descrição                            |
|------------|-------------|--------------------------------------|
| id         | INT (PK)    | Identificador                        |
| id_serie   | INT (FK)    | Série associada                      |
| motivo     | TEXT        | Razão pessoal para assistir          |

---

### **Tabela: `avaliacao_serie`**
| Campo       | Tipo        | Descrição                          |
|-------------|-------------|------------------------------------|
| id          | INT (PK)    | Identificador                      |
| id_serie    | INT (FK)    | Série avaliada                     |
| nota        | INT         | Nota de 0 a 10                     |
| comentario  | TEXT        | Comentário pessoal                 |
| data_avaliacao | DATE     | Data da avaliação                  |

