from pydantic import BaseModel, Field
from typing import Optional
from models.database import Database

class Categoria(BaseModel):
    """Classe que representa uma categoria."""
    
    id: Optional[int] = Field(None, title="ID da categoria", description="ID da categoria")
    nome: str = Field(..., title="Nome da categoria", description="Nome da categoria")

    def salvar_categoria(self) -> Optional['Categoria']:
        """Método para salvar a categoria no banco de dados."""
        try:
            with Database() as db:
                sql = "INSERT INTO categoria (nome) VALUES (%s)"
                params = (self.nome,)

                if not db.executar(sql, params):
                    raise Exception(f"Erro ao executar inserção da categoria '{self.nome}' no banco de dados.")
                
        except Exception as e:
            raise e
        
        return self
    
    def buscar_id_categoria_por_nome(self) -> Optional[int]:
        """Método para buscar o ID da categoria no banco de dados."""
        try:
            with Database() as db:
                sql = "SELECT id_categoria FROM categoria WHERE nome = %s limit 1"
                params = (self.nome,)

                resultado = db.executar(sql, params)
                
                if resultado:
                    return resultado[0]['id_categoria']
                else:
                    self.salvar_categoria()
                    return self.buscar_id_categoria_por_nome()
        
        except Exception as e:
            raise e
        
    
    @staticmethod
    def buscar_nome_categoria_por_id(id_categoria: int) -> Optional[str]:
        """Busca o nome da categoria dado um ID."""
        
        try:
            with Database() as db:
                sql = "SELECT nome FROM categoria WHERE id_categoria = %s LIMIT 1"
                params = (id_categoria,)
                resultado = db.executar(sql, params)

                if resultado:
                    return resultado[0]['nome']
        
        except Exception as e:
            raise e
