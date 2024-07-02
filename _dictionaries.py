class dictionary: 
    merchant_id: dict[str, int] = {
        'UK' : 9 ,
        'DE' : 10,
        'FR' : 11,
        'IT' : 755690533, 
        'ES' : 695831032,
        'NL' : 7067781925,
        'PL' : 54402072512,
        'SE' : 54402660112,
        'TR' : 14311485635,
    }

    marketplace_id : dict[str, int] = {
        'UK' : 3 ,
        'DE' : 4,
        'FR' : 5,
        'IT' : 35691, 
        'ES' : 44551,
        'NL' : 328451,
        'PL' : 712115121,
        'SE' : 704403121,
        'TR' : 338851,
    }

    owner_id : dict[int, int] = {

        3 : 7 ,
        4 : 8,
        5 : 9,
        35691 : 75, 
        44551 : 85,
        328451 : 79,
        712115121 : 82,
        704403121 : 125,
        338851 : 98,
    }

    
    available_mps : list[str] = ['UK','DE','FR','IT','ES','NL','PL','SE','TR']


