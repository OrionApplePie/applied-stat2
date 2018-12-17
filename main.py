def get_zet_ex(mx1, mx2, dv1, dv2, n1, n2):

    ss1 = (n1 / (n1 - 1)) * dv1
    ss2 = (n2 / (n2 - 1)) * dv2
    res = (mx1 - mx2) / ((ss1 / n1 + ss2 / n2) ** 0.5)
    return res

if __name__ == "__main__":
    res = get_zet_ex(
        mx1=22.3,
        mx2=21.9,
        dv1=0.9216,
        dv2=0.6241,
        n1=1572,
        n2=91
    )
    
    print(res)
    
    data = [
        {
            'name': 'all',
            'data': { 'n': 1572, 'x_average': 22.3, 'dv': .9216}
        }, {
            'name': '1st',
            'data': { 'n': 91, 'x_average': 21.9, 'dv': .6241}
        }, {
            'name': '2nd',
            'data': { 'n': 115, 'x_average': 22.4, 'dv': .5776}
        }, {
            'name': '3rd',
            'data': { 'n': 58, 'x_average': 22.6, 'dv': .7396}
        }
    ]
    
    for item in data:
        for inner_item in data:
            if item['name'] != inner_item['name']:
                res = get_zet_ex(
                    mx1=item['data']['x_average'],
                    mx2=inner_item['data']['x_average'],
                    dv1=item['data']['dv'],
                    dv2=inner_item['data']['dv'],
                    n1=item['data']['n'],
                    n2=inner_item['data']['n'],
                )
                print('{0} with {1} : res = {2}'.format(
                    item['name'],
                    inner_item['name'],
                    res
                    )
                )

    