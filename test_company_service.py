import requests

def test_get_all_companies(url: str):
    res = requests.get(url).json()
    assert(res == [{'companies_id': 1, 'name': 'Альфа-Банк',
     'descrption': 'Крупнейшее финансово-кредитное учреждение с универсальным подходом к ведению бизнеса',
     'industry': 'Economy', 'age': '34'},
    {'companies_id': 2, 'name': 'Ozon',
     'descrption': 'Ведущая мультикатегорийная платформа электронной коммерции и одна из крупнейших интернет-компаний в России',
     'industry': 'MarketPlace', 'age': '26'},
    {'companies_id': 3, 'name': 'Apple',
     'descrption': 'Американская корпорация, разработчик персональных и планшетных компьютеров, аудиоплееров, смартфонов, программного обеспечения и цифрового контента',
     'industry': 'Electronic Device', 'age': '47'}])


def test_get_company_by_id(url: str):
    res = requests.get(url).json()
    assert(res == {'companies_id': 1, 'name': 'Альфа-Банк',
     'descrption': 'Крупнейшее финансово-кредитное учреждение с универсальным подходом к ведению бизнеса',
     'industry': 'Economy', 'age': '34'})


if __name__ == '__main__':
    URL = 'http://127.0.0.1:80/api/v1/companies/'
    test_get_company_by_id(URL + '1')
    test_get_all_companies(URL)