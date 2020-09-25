import re
import requests
import urllib3
from bs4 import BeautifulSoup as bs



def defining_search(depth, keyword):
	
	usable_links = []

	if depth == 1:
		url = (f'https://busca.saraiva.com.br/busca?q={keyword}')
		content = requests.get(url)
		soup = bs(content.text, 'html5lib')

		products = [a.text for a in soup.find_all('a', class_='nm-product-name')]
		prices = [a.text.strip() for a in soup.find_all('div', class_='nm-price-container')]

		ugly_description = [a.text for a in soup.find_all('a', class_='nm-description')]
		pretty_description = []
		for i in ugly_description:
			before_i = i.replace('\n            ', '')
			after_i = before_i.replace('\n        ', '')
			pretty_description.append(after_i)

		products_text_list = []

		for i in products:
			for j in prices:
				for k in pretty_description:
					full_product_info = i + '; ' + j + '; ' + k
					products_text_list.append(full_product_info)

		its_inside = False
		for product in products_text_list:
			its_inside = False
			if keyword in product.lower():
				its_inside = True
		if its_inside == True:
			print('Link: '+url)

	elif depth == 2:
		url = (f'https://busca.saraiva.com.br/busca?q={keyword}')
		content = requests.get(url)
		soup = bs(content.text, 'html5lib')


		products = [a.text for a in soup.find_all('a', class_='nm-product-name')]
		prices = [a.text.strip() for a in soup.find_all('div', class_='nm-price-container')]

		ugly_description = [a.text for a in soup.find_all('a', class_='nm-description')]
		pretty_description = []
		for i in ugly_description:
			before_i = i.replace('\n            ', '')
			after_i = before_i.replace('\n        ', '')
			pretty_description.append(after_i)

		products_text_list = []

		for i in products:
			for j in prices:
				for k in pretty_description:
					full_product_info = i + '; ' + j + '; ' + k
					products_text_list.append(full_product_info)
		
		its_inside = False
		for product in products_text_list:
			its_inside = False
			if keyword in product.lower():
				its_inside = True
			if its_inside == True:
				page_full_info = [url, product]
				usable_links.append(page_full_info)
		
		links = [a['href'] for a in soup.find_all('a') if 'href' in a.attrs] #moving to depth 2
		

		for link in links:
			if '.com' in link[0:35]:
				if not(str(link)[0:6] == 'https:') and (str(link)[0:5] != 'http:'):
					new_link = '{0}{1}'.format('https:', str(link))
					
					url = requests.get(new_link)
					soup = bs(url.text, 'html5lib')

					products_text_list_2 = []

					products_2 = [a.text for a in soup.find_all('a', class_='nm-product-name')]
					prices_2 = [a.text.strip() for a in soup.find_all('div', class_='nm-price-container')]

					ugly_description_2 = [a.text for a in soup.find_all('a', class_='nm-description')]
					pretty_description_2 = []
					
					for i in ugly_description_2:
						before_i = i.replace('\n            ', '')
						after_i = before_i.replace('\n        ', '')
						pretty_description_2.append(after_i)

					if len(products_2) > 0:
						for i in products_2:
							for j in prices_2:
								for k in pretty_description_2:
									products_text_list_2.append(i+'; '+j+'; '+ k)

					its_inside_2 = False
					for product in products_text_list_2:
						its_inside_2 = False
						if keyword in product.lower():
							its_inside_2 = True
						if its_inside_2 == True:
							product_full = [new_link, product]
							usable_links.append(product_full)
					
				else:
					url = requests.get(str(link))
					soup = bs(url.text, 'html5lib')

					products_text_list_2 = []

					products_2 = [a.text for a in soup.find_all('a', class_='nm-product-name')]
					prices_2 = [a.text.strip() for a in soup.find_all('div', class_='nm-price-container')]

					ugly_description_2 = [a.text for a in soup.find_all('a', class_='nm-description')]
					pretty_description_2 = []
					
					for i in ugly_description_2:
						before_i = i.replace('\n            ', '')
						after_i = before_i.replace('\n        ', '')
						pretty_description_2.append(after_i)

					if len(products_2) > 0:

						for i in products_2:
							for j in prices_2:
								for k in pretty_description_2:
									products_text_list_2.append(i+'; '+j+'; '+ k)

					its_inside_2 = False
					for product in products_text_list_2:
						its_inside_2 = False
						if keyword in product.lower():
							its_inside_2 = True
						if its_inside_2 == True:
							product_full = [link, product]
							usable_links.append(product_full)

	elif depth == 3:
		url = (f'https://busca.saraiva.com.br/busca?q={keyword}')
		content = requests.get(url)
		soup = bs(content.text, 'html5lib')


		products = [a.text for a in soup.find_all('a', class_='nm-product-name')]
		prices = [a.text.strip() for a in soup.find_all('div', class_='nm-price-container')]

		ugly_description = [a.text for a in soup.find_all('a', class_='nm-description')]
		pretty_description = []
		for i in ugly_description:
			before_i = i.replace('\n            ', '')
			after_i = before_i.replace('\n        ', '')
			pretty_description.append(after_i)

		products_text_list = []

		for i in products:
			for j in prices:
				for k in pretty_description:
					full_product_info = i + '; ' + j + '; ' + k
					products_text_list.append(full_product_info)
		
		its_inside = False
		for product in products_text_list:
			its_inside = False
			if keyword in product.lower():
				its_inside = True
			if its_inside == True:
				page_full_info = [url, product]
				usable_links.append(page_full_info)
		
		links = [a['href'] for a in soup.find_all('a') if 'href' in a.attrs] #moving to depth 2
		
		depth_links_3 = []

		for link in links:
			if '.com' in link[0:35]:
				if not(str(link)[0:6] == 'https:') and (str(link)[0:5] != 'http:'):
					new_link = '{0}{1}'.format('https:', str(link))
					
					url = requests.get(new_link)
					soup = bs(url.text, 'html5lib')

					products_text_list_3 = []

					products_2 = [a.text for a in soup.find_all('a', class_='nm-product-name')]
					prices_2 = [a.text.strip() for a in soup.find_all('div', class_='nm-price-container')]

					ugly_description_2 = [a.text for a in soup.find_all('a', class_='nm-description')]
					pretty_description_2 = []
					
					for i in ugly_description_2:
						before_i = i.replace('\n            ', '')
						after_i = before_i.replace('\n        ', '')
						pretty_description_2.append(after_i)

					if len(products_2) > 0:

						for i in products_2:
							for j in prices_2:
								for k in pretty_description_2:
									products_text_list_3.append(i+'; '+j+'; '+ k)

					its_inside_2 = False
					for product in products_text_list_3:
						its_inside_2 = False
						if keyword in product.lower():
							its_inside_2 = True
						if its_inside_2 == True:
							product_full = [new_link, product]
							usable_links.append(product_full)

					requested_usual_links = [a['href'] for a in soup.find_all('a') if 'href' in a.attrs]
					depth_links_3.append(requested_usual_links) #taking links from depth 2
				
				else:
					url = requests.get(str(link))
					soup = bs(url.text, 'html5lib')

					products_text_list_3 = []

					products_2 = [a.text for a in soup.find_all('a', class_='nm-product-name')]
					prices_2 = [a.text.strip() for a in soup.find_all('div', class_='nm-price-container')]

					ugly_description_2 = [a.text for a in soup.find_all('a', class_='nm-description')]
					pretty_description_2 = []
					
					for i in ugly_description_2:
						before_i = i.replace('\n            ', '')
						after_i = before_i.replace('\n        ', '')
						pretty_description_2.append(after_i)

					if len(products_2) > 0:
						for i in products_2:
							for j in prices_2:
								for k in pretty_description_2:
									products_text_list_3.append(i+'; '+j+'; '+ k)

					its_inside_2 = False
					for product in products_text_list_3:
						its_inside_2 = False
						if keyword in product.lower():
							its_inside_2 = True
						if its_inside_2 == True:
							product_full = [link, product]
							usable_links.append(product_full)

					requested_links = [a['href'] for a in soup.find_all('a') if 'href' in a.attrs]
					depth_links_3.append(requested_links)#taking links from depth 2
		

		for link in depth_links_3: #moving to depth 3
			if '.com' in link[0:35]:
				if not(str(link)[0:6] == 'https:') and (str(link)[0:5] != 'http:'):
					new_link = '{0}{1}'.format('https:', str(link))
					
					url = requests.get(new_link)

					soup = bs(url.text, 'html5lib')

					products_3 = [a.text for a in soup.find_all('a', class_='nm-product-name')]
					prices_3 = [a.text.strip() for a in soup.find_all('div', class_='nm-price-container')]

					ugly_description_3 = [a.text for a in soup.find_all('a', class_='nm-description')]
					pretty_description_3 = []
					
					for i in ugly_description_3:
						before_i = i.replace('\n            ', '')
						after_i = before_i.replace('\n        ', '')
						pretty_description_3.append(after_i)

					if len(products_3) > 0:
						for i in products_3:
							for j in prices_3:
								for k in pretty_description_3:
									products_text_list_3.append(i+'; '+j+'; '+ k)

					its_inside_3 = False
					for product in products_text_list_3:
						its_inside_3 = False
						if keyword in product.lower():
							its_inside_3 = True
						if its_inside_3 == True:
							product_full = [new_link, product]
							usable_links.append(product_full)
				else:
					url = requests.get(str(link))

					soup = bs(url.text, 'html5lib')

					products_3 = [a.text for a in soup.find_all('a', class_='nm-product-name')]
					prices_3 = [a.text.strip() for a in soup.find_all('div', class_='nm-price-container')]

					ugly_description_3 = [a.text for a in soup.find_all('a', class_='nm-description')]
					pretty_description_3 = []
					
					for i in ugly_description_3:
						before_i = i.replace('\n            ', '')
						after_i = before_i.replace('\n        ', '')
						pretty_description_3.append(after_i)

					if len(products_3) > 0:
						for i in products_3:
							for j in prices_3:
								for k in pretty_description_3:
									products_text_list_3.append(i+'; '+j+'; '+ k)

					its_inside_3 = False
					for product in products_text_list_3:
						its_inside_3 = False
						if keyword in product.lower():
							its_inside_3 = True
						if its_inside_3 == True:
							product_full = [link, product]
							usable_links.append(product_full)
	
	return usable_links

def sorting_links(usable_links):
	for i in range(len(usable_links)):
		
		minIndex = i

		for j in range(i+1, len(usable_links)):
			if len(usable_links[minIndex][1]) > len(usable_links[j][1]):
				minIndex = j

		aux = usable_links[i]
		usable_links[i] = usable_links[minIndex]
		usable_links[minIndex] = aux
	
	return usable_links


if __name__ == '__main__':

	depth = int(input('search depth: '))
	keyword = input('keyword: ').lower()

	list_of_links = defining_search(depth, keyword)
	priority_links = sorting_links(list_of_links)

	for i in range(len(priority_links)):
		print(priority_links[i][0])

	print(len(priority_links))