def location1():
    try:
        import geocoder
        import geopy
        from geopy.geocoders import Nominatim
        add = input("Enter the IP Address: ")
        ip = geocoder.ip(add)
        x = ip.latlng
        latitude = x[0]
        longitude = x[1]
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.reverse("{m}, {n}".format(m = latitude, n = longitude))
        print(f'{location}, {x}')
    except Exception as e:
        print(e)

def url_surf():
    try:
        import urllib
        from urllib.request import urlopen
        url = str(input("Enter the url: "))
        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("UTF-8")
        print(html)
    except Exception as e:
        print(e)

class math_ones:

    def first():
        import numpy as np
        import matplotlib.pyplot as plt
  
        x = np.linspace(0, 10, 1000)
        fig, ax = plt.subplots()
  
        ax.plot(x, np.sin(x), '--b', label ='Sine')
        ax.plot(x, np.cos(x), c ='r', label ='Cosine')
        ax.axis('equal')
  
        leg = ax.legend(loc ="lower left")
        plt.show()

    def second():
        import matplotlib.pyplot as plt
        import matplotlib.patches as mpatches
        import scipy.stats
        import numpy as np
        x_min = 0.0
        x_max = 50.0
        fig = plt.figure(figsize = (16, 9)) 
        mean = 12.0 
        std = 3.0
        x = np.linspace(x_min, x_max, 100)
        y = scipy.stats.norm.pdf(x,mean,std)
        plt.plot(x,y, color='red')
        plt.fill_between(x, y, color='#CE5D45', alpha=1.0)
        mean = 18.0 
        std = 6.0
        x = np.linspace(x_min, x_max, 100)
        y = scipy.stats.norm.pdf(x,mean,std)
        plt.plot(x,y, color='green')
        plt.fill_between(x, y, color='#5DC83F', alpha=1.0)
        pop_a = mpatches.Patch(color='#5DC83F', label='Population Dataset 1')
        pop_b = mpatches.Patch(color='#CE5D45', label='Population Dataset 2')
        plt.legend(handles=[pop_a,pop_b])
        plt.grid()
        plt.xlim(x_min,x_max)
        plt.ylim(0,0.25)
        plt.title('simple legend example',fontsize=12)
        plt.xlabel('')
        plt.ylabel('Probability Distribution')
        plt.show()

if __name__ == "__main__":
    location1()
