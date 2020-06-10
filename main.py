class GetRequest:
    #def __init__(self):


    def convertGetDate(self,trh):
        turkish={'ğ':'g','Ş':'S','ı':'i','ü':'u'}
        for tmp1,tmp2 in turkish.items():
            trh=trh.replace(tmp1,tmp2)
        tmp = {"Ocak":"01",
            "Subat":"02",
            "Mart":"03",
            "Nisan":"04",
            "Mayis":"05",
            "Haziran":"06",
            "Temmuz":"07",
            "Agustos":"08",
            "Eylul":"09",
            "Ekim":"10",
            "Kasim":"11",
            "Aralik":"12"
                }
        return tmp[trh]

    def getCarAdvert():
        carList=["https://www.MALUMSARISİTE.com/fiat?pagingOffset=",
         "https://www.MALUMSARISİTE.com/hyundai?pagingOffset=",
         "https://www.MALUMSARISİTE.com/ford?pagingOffset=",
         "https://www.MALUMSARISİTE.com/honda?pagingOffset=",
         "https://www.MALUMSARISİTE.com/nissan?pagingOffset=",
         "https://www.MALUMSARISİTE.com/toyota?pagingOffset=",
         "https://www.MALUMSARISİTE.com/arazi-suv-pickup-dacia?pagingOffset=",
         "https://www.MALUMSARISİTE.com/arazi-suv-pickup-hyundai?pagingOffset=",
         "https://www.MALUMSARISİTE.com/arazi-suv-pickup-jeep?pagingOffset=", 
         "https://www.MALUMSARISİTE.com/arazi-suv-pickup-land-rover?pagingOffset=",
         "https://www.MALUMSARISİTE.com/arazi-suv-pickup-nissan?pagingOffset=",
         "https://www.MALUMSARISİTE.com/arazi-suv-pickup-volkswagen?pagingOffset=",
         "https://www.MALUMSARISİTE.com/bmw?pagingOffset=",
         "https://www.MALUMSARISİTE.com/mercedes-benz?pagingOffset=",
         "https://www.MALUMSARISİTE.com/audi?pagingOffset=",
         "https://www.MALUMSARISİTE.com/volkswagen?pagingOffset=",
         "https://www.MALUMSARISİTE.com/renault?pagingOffset="
         
         ]
        criterias=["",
           "&sorting=km-nu_desc",
           "&sorting=price_asc",
           "&sorting=date_desc"
           ]
        import requests
        from time import sleep
        from random import randint
        from bs4 import BeautifulSoup

        for car in carList:
            for criteria in criterias:
                for pageNumber in range(0,1000,50):
                    url=car+str(pageNumber)+"&pagingSize=50"+str(criteria)
                    
                    sleep(randint(10,40))
                    r=requests.get(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"})
                    soup=BeautifulSoup(r.content,"lxml")
                    mainPage,advertType,brand,model=soup.find_all("span",attrs={"itemprop":"name"})
                    allAdvers=soup.find_all("tr",attrs={"data-id" : True})
                    for allId in allAdvers:
                        print("sa")
                        try:
                            carTitle=allId.find_all("a",
                                                    attrs={"class":"classifiedTitle"})
                        except Exception as e:
                            print(str(e))
                            carTitle="NULL"
                        
                        try:
                            carPacket=allId.find_all("td",
                                                    attrs={"class":"searchResultsTagAttributeValue"})
                        except Exception as e:
                            print(str(e))
                            carPacket="NULL"
                    
                        try:
                            carYearKm=allId.find_all("td",
                                                    attrs={"class":"searchResultsAttributeValue"})
                        except Exception as e:
                            print(str(e))
                            carYearKm="NULL"
                        
                        try:
                            carAdDate=allId.find_all("td","searchResultsDateValue")
                        except Exception as e:
                            print(str(e))
                            carAdDate="NULL"
                        
                        try:
                            carPrice=allId.find_all("td","searchResultsPriceValue")
                        except Exception as e:
                            print(str(e))
                            carPrice="NULL"
                        for a,b,c,d,e,f,h,k in zip(carTitle,carPacket[1::3],carPacket[0::3],carYearKm[1::3],carYearKm[0::3],carYearKm[2::3],carAdDate,carPrice):
                            span1,span2=h.find_all("span")
                            print("İlan Id = " + allId['data-id']) ## ilan no
                            print("Marka = " + model.text.strip())
                            print("İlan adi = "+ a.text.strip())
                            print("Seri =" + b.text.strip())
                            print("Model = " + c.text.strip())
                            print("Yıl = " + e.text.strip())
                            print("Km = " + d.text.strip())
                            print("Renk = " + f.text.strip())
        #return self.carTitle, self.carPacket, self.carYearKm, self.carAdDate, self.carPrice

obj=GetRequest
cb=obj.getCarAdvert()
print(cb)
