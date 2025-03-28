# CRUD Microservice - Order Details

Este microserviço fornece uma API CRUD para a tabela `order_details` do banco de dados PostgreSQL. Ele permite criar, ler, atualizar e deletar detalhes de pedidos.

## Estrutura da Tabela

A tabela `order_details` possui os seguintes campos:

- `order_id` (int2) - ID do pedido
- `product_id` (int2) - ID do produto
- `unit_price` (float4) - Preço unitário
- `quantity` (int2) - Quantidade
- `discount` (float4) - Desconto

## Endpoints Disponíveis

### 1. Criar Detalhe de Pedido (CREATE)

```bash
curl -X POST http://localhost:5000/order-details \
-H "Content-Type: application/json" \
-d '{
    "order_id": 10248,
    "product_id": 77,
    "unit_price": 14.00,
    "quantity": 12,
    "discount": 0.0
}'
```

### 2. Buscar Detalhes Específicos (READ)

```bash
# Buscar por order_id e product_id específicos
curl -X GET http://localhost:5000/order-details/10248/77

# Buscar todos os detalhes de um pedido específico
curl -X GET http://localhost:5000/order-details/10248
```

### 3. Atualizar Detalhe de Pedido (UPDATE)

```bash
curl -X PUT http://localhost:5000/order-details/10248/77 \
-H "Content-Type: application/json" \
-d '{
    "unit_price": 15.00,
    "quantity": 15,
    "discount": 0.1
}'
```

### 4. Deletar Detalhe de Pedido (DELETE)

```bash
curl -X DELETE http://localhost:5000/order-details/10248/77
```

## Exemplos de Respostas

### Criar (POST /order-details)

```json
{
    "message": "Order detail created successfully"
}
```

### Buscar (GET /order-details//)

```json
{
  "discount": 0,
  "order_id": 10248,
  "product_id": 77,
  "quantity": 12,
  "unit_price": 14
}
```

### Buscar Todos do Pedido (GET /order-details/)

```json
[
  {
    "discount": 0,
    "order_id": 10248,
    "product_id": 11,
    "quantity": 12,
    "unit_price": 14
  },
  {
    "discount": 0,
    "order_id": 10248,
    "product_id": 42,
    "quantity": 10,
    "unit_price": 9.8
  },
  {
    "discount": 0,
    "order_id": 10248,
    "product_id": 72,
    "quantity": 5,
    "unit_price": 34.8
  },
  {
    "discount": 0,
    "order_id": 10248,
    "product_id": 77,
    "quantity": 12,
    "unit_price": 14
  }
]
```

### Atualizar (PUT /order-details//)

```json
{
    "message": "Order detail updated successfully"
}
```

### Deletar (DELETE /order-details//)

```json
{
    "message": "Order detail deleted successfully"
}
```

## Códigos de Status HTTP

- 200: Sucesso (GET, PUT, DELETE)
- 201: Criado com sucesso (POST)
- 400: Erro na requisição
- 404: Recurso não encontrado

## Como Executar o Serviço

1. Certifique-se de que o PostgreSQL está rodando e acessível
2. Configure as credenciais do banco em `app/Util/paramsBD.yml`
3. Execute o serviço:

```bash
export FLASK_APP=crudOrderDetails.py
flask run --host=0.0.0.0 --port=5000
```
