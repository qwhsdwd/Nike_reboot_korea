def str_to_json(string):

    L=string.split("\n")

    result=dict()

    for i in range(len(L)):
        d1,d2=L[i].replace(" ","").split(":")
        result[d1]=d2

    return result

if __name__ == '__main__':


    print(str_to_json("""address.isoCountryAlpha2: US
    isSearchAddress: true
    address.fullName: quweihao
    address.phonePrimary.phoneNumber: xxxxxxx
    address.addressLine1: 서울특별시 xxxxxxxxxxx
    address.addressLine2: 302호
    address.postalCode: 04030
    selectPersonalMessage: 
    personalMessageText: 
    fulfillmentOptionId: 1
    csrfToken: KCFF-YOKV-H98U-MT55-PAN0-8LRW-KH1H-xxxx"""))
