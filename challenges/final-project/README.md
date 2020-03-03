# Python Flask Hangman Game

## Estrutura:
 - backend
    - sagger/templates -> Pasta com arquivos de definição da API
    - app.py --> Main app flask
    - data.yaml --> Arquivo de dados principal
    - endpoints.py --> Arquivo de endpoints
    - repository.py --> Codigo de acesso a dados.
    - services.py --> Arquivo principal de regras de negócio

## Tarefas:
1) Endpoint  new => Gerar um novo indenficador para o game 'game_id'
2) Endpoint start => Criar um novo game e sava em arquivo yaml retornando ao front
3) Endpoint handle_guess => Recebe uma letra e um game_id e retorna ao front
4) Endpoint reset => apaga o registro do game
5) Habilitar e acessar o Swagger-UI (Interface de descrição da API)
6) No FrontEnd modificar o método resetButton para chamar o endpoint `reset`

Para cada endponint é necessário um arquivo yaml de definição em (backend > swagger > templates)

### Response
   - endpoints.new
``` 
{ game_id: 76db23b8-5d74-11ea-810b-acde48001122 }
```

   - endpoints.start
``` 
{
   game_id: 76db23b8-5d74-11ea-810b-acde48001122,
   data: {
      'word': Driven By Impact,
      'find': ______ __ ______,
      'tries': 0,
      'result': '' # [win|lose]
	}
}
```
   - endpoints.handle_guess
``` 
{ 
   game_id: 76db23b8-5d74-11ea-810b-acde48001122,
   data: {
      'word': Driven By Impact,
      'find': D_____ __ ______,
      'tries': 1,
      'result': '' ## [win|lose]
   }
}
```


## Iniciando o App
Na pasta backend execute:
```
python app.py
```

Após instalar o frontend (npm install), na pasta frontend basta executar 

```
npm start
```

## Extra:
Validações:
   - Incluir tempo máximo para terminar
   - Remover a palavra final da comunicação back-front
   - Remover o uso de arquivo YAML para usar SQLite
