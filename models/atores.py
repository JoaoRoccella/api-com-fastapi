from pydantic import BaseModel, Field
from typing import Optional
from models.database import Database

class Ator(BaseModel):
    """Classe que representa um ator."""
    
    id: Optional[int] = Field(None, title="ID do ator", description="ID do ator")
    nome: str = Field(..., title="Nome do ator", description="Nome do ator")

    def salvarAtor(self) -> Optional['Ator']:
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
            
        
    