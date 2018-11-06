
import scrapy
from get_data.items import CarItem


class CarsSpider(scrapy.Spider):
    name = 'cars'
    allowed_domains = ['mercadolibre.com.co']
    start_urls = ['https://carros.mercadolibre.com.co//']

    def parse(self, response):
        items = response.xpath("//*[contains(@class, 'results-item')]")

        for item in items:
            #Iterates over each result
            link = item.xpath('.//*[@class="images-viewer"]/@item-url').extract_first()
            yield scrapy.Request(link, callback=self.parse_items)
        next_page = response.xpath('//*[text()[contains(., "Siguiente")]]/../@href').extract_first()
        if next_page:
            yield scrapy.Request(next_page)

    def parse_items(self, response):
        carItem = CarItem()
        carItem['id']           = ''.join(response.url.split('/')[-1].split('-')[:2])
        carItem['color']        = response.xpath('//*[text()[contains(., "Color")]]/../span/text()').extract_first()
        carItem['fuel']         = response.xpath('//*[text()[contains(., "Combustible")]]/../span/text()').extract_first()
        carItem['mileage']      = response.xpath('//*[text()[contains(., "Recorrido")]]/../span/text()').extract_first()
        carItem['brand']        = response.xpath('//*[text()[contains(., "Marca")]]/../span/text()').extract_first()
        carItem['model']        = response.xpath('//*[text()[contains(., "Modelo")]]/../span/text()').extract_first()
        carItem['onlyOwner']    = response.xpath('//*[text()[contains(., "Único dueño")]]/../span/text()').extract_first()
        carItem['year']         = response.xpath('//*[text()[contains(., "Año")]]/../span/text()').extract_first()
        carItem['steering']     = response.xpath('//*[text()[contains(., "Dirección")]]/../span/text()').extract_first()
        carItem['engine']       = response.xpath('//*[text()[contains(., "Motor")]]/../span/text()').extract_first()
        carItem['traction']     = response.xpath('//*[text()[contains(., "Tracción")]]/../span/text()').extract_first()
        carItem['transmission'] = response.xpath('//*[text()[contains(., "Transmisión")]]/../span/text()').extract_first()
        carItem['location']     = response.xpath('//*[@class="location-info"]/text()').extract()[1].strip()
        carItem['image_urls']   = response.xpath('//figure[1]/a/img/@src').extract()
        carItem['price']        = response.xpath('//*[@class="price-tag price-tag-motors"]/span[2]/text()').extract_first()
        yield carItem
