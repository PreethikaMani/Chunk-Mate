# Web API Checklist

- [x] Use RESTful design
- [x] Add rate limiting
- [ ] Implement caching
- [x] Include Swagger/OpenAPI docs

## Sample Request

```bash
curl -X POST http://localhost:8000/api/chunk/ \
-H "Content-Type: application/json" \
-d '{"text": "Split this document"}'
```

## Response

```json
{
  "chunks": [
    "Split this",
    "document"
  ]
}
```
