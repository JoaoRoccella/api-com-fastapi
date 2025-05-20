from pydantic import BaseModel, Field
from typing import Optional, OrderedDict
from models.database import Database

class Ator(BaseModel):
    """Classe que representa um ator."""
    
    id_ator: Optional[int] = Field(None, title="ID do ator", description="ID do ator")
    nome: str = Field(..., title="Nome do ator", description="Nome do ator")

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 0,
                "nome": "Robert Downey Jr.",
            }
        }
    }

    def salvar_ator(self) -> Optional['Ator']:
        """Método para salvar o ator no banco de dados."""
        # Aqui você deve implementar a lógica para salvar o ator no banco de dados
        # Exemplo: db.add(self)
        
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
                sql = "SELECT * FROM ator WHERE id = %s"
                params = (id,)
                result = db.buscar(sql, params)
                
                if result:
                    return Ator(**result[0])
                else:
                    print(f'Ator com ID {id} não encontrado!')
                    return None
        except Exception as e:
            print(f'Erro ao buscar o ator: {e}')
            return None
            
        
    