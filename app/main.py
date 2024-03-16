from fastapi import FastAPI, APIRouter

app = FastAPI(openapi_url="/api/v1/companies/openapi.json", docs_url="/api/v1/companies/docs")

companies_router = APIRouter()

companies = [
    {'companies_id': 1, 'name': 'Альфа-Банк',
     'descrption': 'Крупнейшее финансово-кредитное учреждение с универсальным подходом к ведению бизнеса',
     'industry': 'Economy', 'age': '34'},
    {'companies_id': 2, 'name': 'Ozon',
     'descrption': 'Ведущая мультикатегорийная платформа электронной коммерции и одна из крупнейших интернет-компаний в России',
     'industry': 'MarketPlace', 'age': '26'},
    {'companies_id': 3, 'name': 'Apple',
     'descrption': 'Американская корпорация, разработчик персональных и планшетных компьютеров, аудиоплееров, смартфонов, программного обеспечения и цифрового контента',
     'industry': 'Electronic Device', 'age': '47'}
]


@companies_router.get("/")
async def read_companies():
    return companies

@companies_router.get("/{companies_id}")
async def read_company(companies_id: int):
    for company in companies:
        if company['companies_id'] == companies_id:
            return company
    return None

app.include_router(companies_router, prefix='/api/v1/companies', tags=['companies'])

if __name__ == '__main__':
    import uvicorn
    import os
    try:
        PORT = int(os.environ['PORT'])
    except KeyError as keyerr:
        PORT = 80
    uvicorn.run(app, host='0.0.0.0', port=PORT)