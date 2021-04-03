# +
import requests
import pandas as pd
import time
import json

def GetCryptoPortfolio(year, cryptoCurrencies, inFiatCurrency):
    """
    This function returns the value of the crypto currency
    on the first day of the year. This can help in reporting crypto portfolio in Norway.
    
    Thanks to Coingecko for an amazing free API.
    
    """
    date = "01-01-"+year
    
    apiData = {"Date" : [],
               "Cryptocurrency": [],
               "Position":[],
               "Price in {0}".format(inFiatCurrency.upper()): []}  # Creating a dictionary 
    for i in cryptoCurrencies.keys():
        """ 
        This loop sends API calls and retrieves the values and updated the apiData dictionary
        """
        url ="https://api.coingecko.com/api/v3/coins/{0}/history?date={1}".format(i.lower(), date)
        x = requests.get(url)
        response = x.json()
        priceinCurrency = round(response["market_data"]["current_price"][inFiatCurrency.lower()],2)
        apiData["Date"].append(date)
        apiData["Cryptocurrency"].append(i)
        apiData["Position"].append(cryptoCurrencies[i])
        apiData["Price in {0}".format(inFiatCurrency.upper())].append(priceinCurrency) 
        time.sleep(5)  #avoiding multiple requests to the api in a short time scale
    df = pd.DataFrame(apiData)
    df["CryptoValue in {}".format(inFiatCurrency.upper())] =  round((df["Price in {0}".format(inFiatCurrency.upper())] * df["Position"]), 2)
    df.to_csv(r"output/CryptoPortfolio.csv", index=False)  # Save as a CSV
    return df  # Return the resulting dataframe


# +
# Testing : GetCryptoPortfolio
#year = "2021"
#cryptos = {"Bitcoin": 2,"Ethereum": 4}
#fiat = "nok"
#df = GetCryptoPortfolio(year, cryptos, fiat)
#df
# -
def CreatePortfolioPieChart(fiatCurrency):
    import matplotlib.pyplot as plt
    import pandas as pd
    df = pd.read_csv("output/CryptoPortfolio.csv")
    plt.figure()
    plt.rcParams["figure.figsize"] = (10,3)
    plt.rcParams['font.size'] = 8
    
    values = df.iloc[:, 4].to_list()
    labels = df.iloc[:, 1].to_list()

    explode = (0.08,) * df.iloc[:, 4].count()
    colors = ['#008DB8', '#00AAAA', '#00C69C', '#00E28E', '#00FF80', '#191970', '#001CF0', '#0038E2', '#0055D4', '#0071C6', ]
    colors = colors[0:df.iloc[:, 4].count()]

    def make_autopct(values):
        def my_autopct(pct):
            total = sum(values)
            val = int(round(pct*total/100.0))
            return fiatCurrency.upper() +' {v:d}'.format(v=val)
        return my_autopct

    fig1, ax1= plt.subplots()
    ax1.pie(values, colors=colors, explode=explode,
            autopct=make_autopct(values), 
            shadow=False, startangle=30)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title("Crypto Portfolio as of {0}".format(df.iat[0,0]))
    plt.legend(labels=labels, loc="best")
    plt.tight_layout()
    plt.savefig('output/CryptoPortfolioPieChart.png', dpi=200)


# +
# Testing : CreatePortfolioPieChart
#CreatePortfolioPieChart("nok")
# -

def CreatePortfolioTreeMapChart(fiatCurrency):
    import matplotlib.pyplot as plt
    import pandas as pd
    import squarify
    df = pd.read_csv("output/CryptoPortfolio.csv")
    plt.figure()
    plt.rcParams["figure.figsize"] = (10,3)
    plt.rcParams['font.size'] = 8

    labels =[]
    colors = ['#008DB8', '#00AAAA', '#00C69C', '#00E28E', '#00FF80', '#191970', '#001CF0', '#0038E2', '#0055D4', '#0071C6', ]
    colors = colors[0:df.iloc[:, 4].count()]
    for index, row in df.iterrows():
        labels.append(row["Cryptocurrency"] + "\n"+fiatCurrency.upper()+" "+str(row["CryptoValue in {}".format(fiatCurrency.upper())]))

    values = df.iloc[:, 4].to_list()
    squarify.plot(sizes=values, label=labels, color=colors, alpha=0.6)
    plt.title("Crypto Portfolio as of {0}".format(df.iat[0,0]))
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('output/CryptoPortfolioTreeMapChart.png', dpi=200)

# +
# Testing : CreatePortfolioTreeMapChart
#CreatePortfolioTreeMapChart("nok")
# -


