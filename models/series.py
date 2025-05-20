from pydantic import BaseModel, Field, model_validator
from typing import Optional
from collections import OrderedDict
from models.database import Database
from models.categorias import Categoria

class Serie(BaseModel):
    """Classe que representa uma série."""

    id_serie: Optional[int] = Field(None, title="ID da série", description="ID da série")
    titulo: str = Field(..., title="Título da série", description="Título da série")
    descricao: str = Field(..., title="Descrição da série", description="Descrição da série")
    ano_lancamento: int = Field(..., title="Ano de lançamento", description="Ano de lançamento da série")
    id_categoria: Optional[int] = Field(None, title="ID da categoria", description="ID da categoria da série, se conhecido")
    nome_categoria: Optional[str] = Field(None, title="Nome da categoria", description="Nome da categoria da série")

    model_config = {
        "json_schema_extra": {
            "example": {
                "id_serie": 42,
                "titulo": "Stranger Things",
                "descricao": "Série de ficção científica e terror ambientada nos anos 80.",
                "ano_lancamento": 2016,
                "id_categoria": 3,
                "nome_categoria": "Ficção Científica",
            }
        }
    }
    
    @model_validator(mode="after")
    def validar_categoria(self):
        """Garante que ao menos id_categoria ou nome_categoria esteja presente."""
        if not self.id_categoria and not self.nome_categoria:
            raise ValueError("É necessário fornecer 'id_categoria' ou 'nome_categoria'.")
        
        if self.id_categoria and self.nome_categoria:
            nome_esperado = Categoria.buscar_nome_categoria_por_id(self.id_categoria)

            if nome_esperado and (nome_esperado.strip().lower() != self.nome_categoria.strip().lower()):
                raise ValueError(
                    f"Inconsistência: 'id_categoria: {self.id_categoria}' corresponde a '{nome_esperado}', "
                    f"mas foi informado o nome '{self.nome_categoria}'."
                )
        
        return self

    
    def salvar_serie(self) -> Optional['Serie']:
        """Método para salvar a série no banco de dados."""
        try:
            with Database() as db:
                if not self.id_categoria:
                    # Buscar ou criar a categoria com base no nome
                    categoria = Categoria(nome=self.nome_categoria)
                    self.id_categoria = categoria.buscar_id_categoria_por_nome()
                
                sql = "INSERT INTO serie (titulo, descricao, ano_lancamento, id_categoria) VALUES (%s, %s, %s, %s)"
                params = (self.titulo, self.descricao, self.ano_lancamento, self.id_categoria)

                if not db.executar(sql, params):
                    raise Exception(f"Erro ao executar inserção da série '{self.titulo}' no banco de dados.")
                
                print(f"Série '{self.titulo}' salva com sucesso!")
        except Exception as e:
            raise e

        return self
