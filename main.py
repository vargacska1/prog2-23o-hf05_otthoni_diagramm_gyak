import os
import json
import matplotlib.pyplot as plt


def albums_by_years():
    num_albums_by_years = {}
    for band in os.listdir('albums'):
        for album in os.listdir(os.path.join('albums', band)):
            try:
                with open(os.path.join('albums', band, album)) as f:
                    datas = json.load(f)
            except json.JSONDecodeError:
                continue
            try:
                num_albums_by_years[datas['year']] += 1
            except KeyError:
                num_albums_by_years[datas['year']] = 1
    num_albums_by_years = dict(sorted(num_albums_by_years.items()))
    plt.scatter(num_albums_by_years.keys(), num_albums_by_years.values())
    plt.plot(num_albums_by_years.keys(), num_albums_by_years.values())
    plt.savefig('yearly_albums1.png')

def most_common_first_names():
    names_num={}
    used_names=[]
    for band in os.listdir('albums'):
        for album in os.listdir(os.path.join('albums', band)):
            try:
                with open(os.path.join('albums', band, album)) as f:
                    datas = json.load(f)
            except json.JSONDecodeError:
                continue
            try:
                for person in datas['personnel']:
                    first_name = person.split(' ')[0]
                    if person not in used_names:
                        try:
                            names_num[first_name] += 1
                        except KeyError:
                            names_num[first_name] = 1
                        used_names.append(person)
            except KeyError:
                continue
    minimum_10={}
    for name, num in names_num.items():
        if num > 10:
            minimum_10[name] = num
    minimum_10=dict(sorted(minimum_10.items(), key=lambda item: item[1]))
    x = list(minimum_10.values())
    y = list(minimum_10.keys())
    plt.barh(y, x)
    plt.savefig('first_names1.png')
    
    
def band_album_sizes():
    bands_numbers={}
    for i in range(1,8):
        try:
            bands_numbers[i]=0
        except KeyError:
            continue
    bands_numbers['8+']=0
    for band in os.listdir('albums'):
        people = set()
        for file in os.listdir(os.path.join('albums',band)):
            try:
                with open(os.path.join('albums', band, file)) as f:
                    datas=json.load(f)
                    people.update(datas['personnel'])  
            except:
                continue
        if len(people) < 8:
            try:
                bands_numbers[len(people)] += 1
            except KeyError:
                continue
        else:
            bands_numbers['8+'] += 1
    fig, ax= plt.subplots(2)
    ax[0] = plt.pie(bands_numbers.values(), labels=bands_numbers.keys())
    fig.savefig('piechart.png')

if __name__ == '__main__':
    band_album_sizes()