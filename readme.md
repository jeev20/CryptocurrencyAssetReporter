# Crypto Asset Report - Tax Return
## Why use this robot? 
In Norway, the government mandates that al cryptocurrency holdings are reported in the yearly tax return statement. 
However, unlike the stock market or bank accounts, the value of cryptocurrencies are volatile. The requirement is that individuals report the value of the asset as of the 1st day of the new year. To do this manually is not worth the time, what if we can automate it? 

## Solution
Through this Robocorp Robot script, I have tried to make the process of calculating the portfolio value a little less difficult. 

## What does GetCryptoPortfolio.py script do?
- The Robot uses the CoinGecko Historial Dataset API to poll the values of each input cryptocurrency. 
- The API calls are written in standard python functions in the "GetCryptoPortfolio.py" file
- The function GetCryptoPortfolio takes three inputs, namely year (the year you are trying to get the data for), cryptoCurrencies (dictonary of cryptocurrencies and your positions), inFiatCurrency (the fiat currency you want to get the value in)
- The function CreatePortfolioPieChart takes "FiatCurrency" as input and saves a pie chart of the value in /output/CryptoPortfolioPieChart.png
- The function CreatePortfolioTreeMapChart takes "FiatCurrency" as input and saves a TreeMap chart of the value in /output/CryptoPortfolioTreeMap.png

## What does tasts.robot script do?
- Sets the variables, settings and keywords. 
- Keywords are essentialy a wrapper to the functions in GetCryptoPortfolio.py
- Tasks invoke the keywords in the required order.
- The output .csv and .png files are stored in the "/output" folder.

## Preconditions 
Ensure you setup your Robocorp Lab instance to be able to run this robot in attended mode. 
Clone this repository and ensure your RCC in Robocorp lab is connected to your python instance. Robocorp Lab will parse the conda.yaml file to install all dependecies for this project using pip. 


## Running the script 

Step 1. Copy or Clone the contents of this repository 

Step 2. Open the project in Robcorp Lab and open the tasks.robot file 

Step 3. Change the variables as required 
         year (string), 
         cryptoCurrencies (dictionary), 
         inFiatCurrency (string)
```
*** Variables ***
${year}  2021
&{cryptoCurrencies}    Bitcoin=${2}  Cardano=${3000}   Ethereum=${23.093898}  Monero=${13}
${inFiatCurrency}  nok  # any fiat currency supported by CoinGecko
```

Step 4. Execute the tasks.robot file and the output files will then be found in this following relative path in the project. 
```
/output/CryptoPortfolio.csv
/output/CryptoPortfolioPieChart.png
/output/CryptoPortfolioTreeMap.png
```

![CryptoPortfolioTable](https://github.com/jeev20/CryptoAssetReport/blob/main/output/CryptoPortfolio.csv)



![PieChart](https://github.com/jeev20/CryptoAssetReport/blob/main/output/CryptoPortfolioPieChart.png)



![TreeMapChart](https://github.com/jeev20/CryptoAssetReport/blob/main/output/CryptoPortfolioTreeMapChart.png)


## Thanks to 
* [CoinGecko API](https://www.coingecko.com/en/api)
* [Robocorp](https://robocorp.com)
* [RobotFramework](https://robotframework.org/)


## Contributors
* [jeev20]("https://github.com/jeev20")
