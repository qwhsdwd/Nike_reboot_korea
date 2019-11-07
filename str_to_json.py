def str_to_json(string):

    # print(string.count("\n"))
    L=string.split("\n")

    result=dict()

    for i in range(len(L)):
        d1,d2=L[i].replace(" ","").split(":")
        result[d1]=d2
    print(result)



str_to_json("""address.isoCountryAlpha2: US
isSearchAddress: true
address.fullName: quweihao
address.phonePrimary.phoneNumber: 01029972828
address.addressLine1: 서울특별시 마포구 동교로22길 22
address.addressLine2: 302호
address.postalCode: 04030
selectPersonalMessage: 
personalMessageText: 
fulfillmentOptionId: 1
csrfToken: KCFF-YOKV-H98U-MT55-PAN0-8LRW-KH1H-HZML""")