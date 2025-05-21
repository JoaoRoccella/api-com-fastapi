from pydantic import BaseModel, Field
from typing import Optional, List
from models.database import Database

class Ator(BaseModel):
    """Classe que representa um ator."""
    
    id_ator: Optional[int] = Field(None, title="ID do ator", description="ID do ator")
    nome: Optional[str] = Field(None, title="Nome do ator", description="Nome do ator")

    model_config = {
        "json_schema_extra": {
            "example": {
                "id_ator": 0,
                "nome": "Robert Downey Jr.",
            }
        }
    }

    def salvar_ator(self) -> Optional['Ator']:
        """Método para salvar o ator no banco de dados."""
        
        try:
            with Database() as db:
                sql = "INSERT INTO ator (nome) VALUES (%s)"
                params = (self.nome,)

                if db.executar(sql, params):
                    print(f'Ator {self.nome} salvo com sucesso!')
                else:
                    print(f'Erro ao salvar o ator {self.nome}!')
        except Exception as e:
            print(f'Erro ao salvar o ator: {e}')
            return None
        
        return self
    
    def buscar_ator_pelo_id(self, id: int) -> Optional['Ator']:
        """Método para buscar um ator pelo ID."""
        
        try:
            with Database() as db:
                sql = "SELECT * FROM ator WHERE id_ator = %s"
                params = (id,)
                result = db.executar(sql, params)
                
                if result:
                    return Ator(**result[0])
                else:
                    print(f'Ator com ID {id} não encontrado!')
                    return None
        except Exception as e:
            print(f'Erro ao buscar o ator: {e}')
            return None
            
        
    @staticmethod
    def buscar_atores() -> Optional[List['Ator']]:
        """Método para buscar todos os atores."""
        
        try:
            with Database() as db:
                sql = "SELECT * FROM ator"
                result = db.executar(sql)
                return result if result else None
        except Exception as e:
            print(f'Erro ao buscar os atores: {e}')
            return None